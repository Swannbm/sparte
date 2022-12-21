import logging
import pandas as pd

from django.contrib.gis.db.models import Union
from django.core.management.base import BaseCommand

from tqdm.notebook import tqdm

from public_data.models import Scot, Region, Departement, Commune
from public_data.storages import DataStorage


logger = logging.getLogger("management.commands")


class Command(BaseCommand):
    help = "Charge les SCoTs"

    def init_data(self):
        self.scot_id_list = list()
        self.region_list = {r.name: r for r in Region.objects.all()} | {
            "Bourgogne-Franche-Comte": Region.objects.get(
                name="Bourgogne-Franche-Comté"
            ),
            "Ile-de-France": Region.objects.get(name="Île-de-France"),
            "Auvergne-Rhone-Alpes": Region.objects.get(name="Auvergne-Rhône-Alpes"),
            "Provence-Alpes-Cote d'Azur": Region.objects.get(
                name="Provence-Alpes-Côte d'Azur"
            ),
        }
        self.dept_list = {d.name: d for d in Departement.objects.all()}
        with DataStorage().open("scote_et_communes.xlsx") as file_stream:
            self.df_scot = pd.read_excel(file_stream, sheet_name="Liste des SCoT")
            self.df_scot = self.df_scot.dropna()
            self.df_city = pd.read_excel(file_stream, sheet_name="Communes Scot")

    def handle(self, *args, **options):
        logger.info("Start loading SCoTs")
        self.init_data()
        self.create_or_update_scot()
        self.link_commune_to_scot()
        self.calculate_scot_mpoly_field()
        logger.info("End loading SCoTs")

    def create_or_update_scot(self):
        for index, row in tqdm(self.df_scot.iterrows(), total=len(self.df_scot.index)):
            if row["Région"] not in self.region_list:
                # ignore DOMTOM
                continue
            try:
                scot = Scot.objects.get(id=row["IDSCoT\n"])
            except Scot.DoesNotExist:
                scot = Scot(id=row["IDSCoT\n"])
            scot.name = row["Nom"]
            scot.region = self.region_list[row["Région"]]
            scot.departement = self.dept_list[row["Département"]]
            scot.is_inter_departement = row["interdépartemental (Oui/non)"] == "Oui"
            scot.state_statut = row["Libellé Etat simplifié"]
            scot.detailed_state_statut = row["Libellé Etat détaillé\n"]
            scot.date_published_perimeter = row["publication du Pèrimetre"]
            scot.date_acting = row["engagement"]
            scot.date_stop = row["Arrêt de projet"]
            scot.date_validation = row["approbation"]
            scot.date_end = row["Fin échéance"]
            scot.is_ene_law = row["Intégration disposition loi ENE"] == "Oui"
            scot.scot_type = row["Type"]
            scot.siren = row["Siren"]
            scot.save()
            self.scot_id_list.append(scot.id)

    def link_commune_to_scot(self):
        logger.info("link_commune_to_scot")
        for index, row in tqdm(self.df_city.iterrows(), total=len(self.df_city.index)):
            try:
                if row["id"] in self.scot_id_list:
                    # keep only cities in keeped SCoT (ie. remove islands)
                    city = Commune.objects.get(insee=row["insee"])
                    city.scot_id = row["id"]
                    city.save()
            except Commune.DoesNotExist:
                logger.error("%s insee is unknown in commune", row["insee"])

    def calculate_scot_mpoly_field(self):
        logger.info("calculate_scot_mpoly_field")
        qs = Commune.objects.values("scot__id").annotate(union_mpoly=Union("mpoly"))
        for row in tqdm(qs, total=qs.count()):
            Scot.objects.filter(id=row["scot__id"]).update(mpoly=row["union_mpoly"])

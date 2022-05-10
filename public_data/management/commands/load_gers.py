import logging

from django.core.management.base import BaseCommand

from public_data.models import (
    Ocsge,
    Departement,
    OcsgeDiff,
    ZoneConstruite,
    CouvertureUsageMatrix,
)


logger = logging.getLogger("management.commands")


class GersOcsge(Ocsge):
    class Meta:
        proxy = True

    mapping = {
        "id_source": "ID",
        "couverture": "CODE_CS",
        "usage": "CODE_US",
        "millesime_source": "MILLESIME",
        "source": "SOURCE",
        "ossature": "OSSATURE",
        "id_origine": "ID_ORIGINE",
        "code_or": "CODE_OR",
        "mpoly": "MULTIPOLYGON",
    }
    default_color = "Chocolate"

    matrix_list = {
        (item.couverture.code_prefix, item.usage.code_prefix): item
        for item in CouvertureUsageMatrix.objects.all().select_related(
            "usage", "couverture"
        )
    }

    def save(self, *args, **kwargs):
        key = (self.couverture, self.usage)
        self.matrix = self.__class__.matrix_list[key]
        self.is_artificial = bool(self.matrix.is_artificial)
        self.couverture_label = self.matrix.couverture.label
        self.usage_label = self.matrix.usage.label
        self.year = self.__class__.year
        return super().save(*args, **kwargs)

    @classmethod
    def clean_data(cls, clean_queryset=None):
        """Delete only data with year=2015"""
        gers = Departement.objects.get(id=33)
        # select only data covered by Gers
        qs = cls.objects.filter(mpoly__intersects=gers.mpoly)
        # only current millesime
        qs = qs.filter(year=cls.year)
        qs.delete()


class GersOcsge2016(GersOcsge):
    class Meta:
        proxy = True

    shape_file_path = "gers_ocsge_2016.zip"
    year = 2016


class GersOcsge2019(GersOcsge):
    class Meta:
        proxy = True

    shape_file_path = "gers_ocsge_2019.zip"
    year = 2019


class GersOcsgeDiff(OcsgeDiff):
    class Meta:
        proxy = True

    _year_new = 2019
    _year_old = 2016

    shape_file_path = "gers_diff_2016_2019.zip"

    matrix_list = {
        (item.couverture.code_prefix, item.usage.code_prefix): item
        for item in CouvertureUsageMatrix.objects.all().select_related(
            "usage", "couverture"
        )
    }

    def save(self, *args, **kwargs):
        self.year_new = self.__class__._year_new
        self.year_old = self.__class__._year_old
        try:
            self.new_matrix = self.__class__.matrix_list[(self.cs_new, self.us_new)]
            self.cs_new_label = self.new_matrix.couverture.label
            self.us_new_label = self.new_matrix.usage.label
            self.new_is_artif = bool(self.new_matrix.is_artificial)
        except KeyError:
            self.new_is_artif = False

        try:
            self.old_matrix = self.__class__.matrix_list[(self.cs_old, self.us_old)]
            self.cs_old_label = self.old_matrix.couverture.label
            self.us_old_label = self.old_matrix.usage.label
            self.old_is_artif = bool(self.old_matrix.is_artificial)
        except KeyError:
            self.old_is_artif = False

        self.is_new_artif = not self.old_is_artif and self.new_is_artif
        self.is_new_natural = self.old_is_artif and not self.new_is_artif

        return super().save(*args, **kwargs)

    @classmethod
    def clean_data(cls, clean_queryset=None):
        gers = Departement.objects.get(id=33)
        # select only data covered by Gers
        qs = cls.objects.filter(mpoly__intersects=gers.mpoly)
        # only current millesime
        qs = qs.filter(year_new=cls._year_new, year_old=cls._year_old)
        qs.delete()


class ZoneConstruite2016(ZoneConstruite):
    _year = 2016
    shape_file_path = "gers_zone_construite_2016.zip"

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.year = self._year
        return super().save(*args, **kwargs)

    @classmethod
    def clean_data(cls, clean_queryset=None):
        gers = Departement.objects.get(id=33)
        # select only data covered by Gers
        qs = cls.objects.filter(mpoly__intersects=gers.mpoly)
        # only current millesime
        qs = qs.filter(year=cls._year)
        qs.delete()


class ZoneConstruite2019(ZoneConstruite2016):
    _year = 2019
    shape_file_path = "gers_zone_construite_2019.zip"

    class Meta:
        proxy = True


class Command(BaseCommand):
    help = "Load all data from gers territory"

    def add_arguments(self, parser):
        parser.add_argument(
            "--item",
            type=str,
            help="item that you want to load ex: GersOcsge2016, ZoneConstruite2019...",
        )

    def handle(self, *args, **options):
        logger.info("Load Gers OCSGE")
        self.load(item=options["item"])
        logger.info("End loading Gers OCSGE")

    def test(self):
        logger.info("MODE TEST")
        # GersOcsge2016.load(shp_file="media/gers/OCCUPATION_SOL_2016.shp", verbose=True)
        # GersOcsge2019.load(shp_file="media/gers/OCCUPATION_SOL_2019.shp", verbose=True)
        # GersOcsgeDiff.load(shp_file="media/gers/DIFF_2016_2019.shp", verbose=True)
        ZoneConstruite2019.load(shp_file="media/gers/ZONE_CONSTRUITE_2019.shp")

    def load(self, item=None):
        gers_model_list = [
            GersOcsge2016,
            GersOcsge2019,
            GersOcsgeDiff,
            ZoneConstruite2016,
            ZoneConstruite2019,
        ]
        for gers_model in gers_model_list:
            if not item or gers_model.__name__ == item:
                logger.info(f"process: {gers_model.__name__}")
                gers_model.load()

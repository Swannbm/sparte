from django.contrib.gis.geos import Polygon
from django.db.models import F, FloatField, Max, OuterRef, Subquery, Sum
from django.db.models.functions import Cast
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView
from jenkspy import jenks_breaks

from project.models import Project
from project.serializers import CityArtifMapSerializer, CitySpaceConsoMapSerializer
from public_data.models import Cerema, CouvertureSol, UsageSol
from utils.colors import get_dark_blue_gradient, get_yellow2red_gradient

from .mixins import GroupMixin


class ProjectMapView(GroupMixin, DetailView):
    queryset = Project.objects.all()
    template_name = "carto/full_carto.html"
    context_object_name = "project"

    def get_context_breadcrumbs(self):
        breadcrumbs = super().get_context_breadcrumbs()
        breadcrumbs.append({"href": None, "title": "Carte intéractive"})
        return breadcrumbs

    def get_context_data(self, **kwargs):
        # UPGRADE: add center and zoom fields on project model
        # values would be infered when emprise is loaded
        center = self.object.get_centroid()
        kwargs.update(
            {
                # center map on France
                "carto_name": "Project",
                "center_lat": center.y,
                "center_lng": center.x,
                "default_zoom": 10,
                "layer_list": [
                    {
                        "name": "Communes",
                        "url": reverse_lazy("project:project-communes", args=[self.object.id]),
                        "display": False,  # afficher par défaut ou non
                        "level": "2",
                        "style": "style_communes",
                    },
                    {
                        "name": "Emprise du projet",
                        "url": reverse_lazy("project:emprise-list") + f"?id={self.object.pk}",
                        "display": True,
                        "style": "style_emprise",
                        "fit_map": True,
                        "level": "5",
                    },
                    {
                        "name": "Arcachon: Couverture 2015",
                        "url": (f'{reverse_lazy("public_data:ocsge-optimized")}' "?year=2015&color=couverture"),
                        "display": False,
                        "color_property_name": "map_color",
                        "style": "get_color_from_property",
                        "level": "1",
                    },
                    {
                        "name": "Arcachon: Couverture 2018",
                        "url": (f'{reverse_lazy("public_data:ocsge-optimized")}' "?year=2018&color=couverture"),
                        "display": False,
                        "color_property_name": "map_color",
                        "style": "get_color_from_property",
                        "level": "1",
                    },
                    {
                        "name": "Arcachon: Usage 2015",
                        "url": (f'{reverse_lazy("public_data:ocsge-optimized")}' "?year=2015&color=usage"),
                        "display": False,
                        "color_property_name": "map_color",
                        "style": "get_color_from_property",
                        "level": "1",
                    },
                    {
                        "name": "Arcachon: Usage 2018",
                        "url": (f'{reverse_lazy("public_data:ocsge-optimized")}' "?year=2018&color=usage"),
                        "display": False,
                        "color_property_name": "map_color",
                        "style": "get_color_from_property",
                        "level": "1",
                    },
                    {
                        "name": "Archachon : artificialisation 2015 à 2018",
                        "url": (
                            f'{reverse_lazy("public_data:ocsgediff-optimized")}'
                            "?year_old=2015&year_new=2018&is_new_artif=true"
                        ),
                        "display": False,
                        "style": "get_color_for_ocsge_diff",
                        "level": "7",
                    },
                    {
                        "name": "Arcachon : renaturation de 2015 à 2018",
                        "url": (
                            f'{reverse_lazy("public_data:ocsgediff-optimized")}'
                            "?year_old=2015&year_new=2018&is_new_natural=true"
                        ),
                        "style": "get_color_for_ocsge_diff",
                        "level": "7",
                        "display": False,
                    },
                    {
                        "name": "Arcachon: zones artificielles 2015",
                        "url": (f'{reverse_lazy("public_data:artificialarea-optimized")}' "?year=2015"),
                        "display": False,
                        "level": "3",
                        "style": "style_zone_artificielle",
                    },
                    {
                        "name": "Arcachon: zones artificielles 2018",
                        "url": (f'{reverse_lazy("public_data:artificialarea-optimized")}' "?year=2018"),
                        "display": False,
                        "level": "3",
                        "style": "style_zone_artificielle",
                    },
                    {
                        "name": "Gers: Couverture 2016",
                        "url": (f'{reverse_lazy("public_data:ocsge-optimized")}' "?year=2016&color=couverture"),
                        "display": False,
                        "color_property_name": "map_color",
                        "style": "get_color_from_property",
                        "level": "1",
                    },
                    {
                        "name": "Gers: Couverture 2019",
                        "url": (f'{reverse_lazy("public_data:ocsge-optimized")}' "?year=2019&color=couverture"),
                        "display": False,
                        "color_property_name": "map_color",
                        "style": "get_color_from_property",
                        "level": "1",
                    },
                    {
                        "name": "Gers: Usage 2016",
                        "url": (f'{reverse_lazy("public_data:ocsge-optimized")}' "?year=2016&color=usage"),
                        "display": False,
                        "color_property_name": "map_color",
                        "style": "get_color_from_property",
                        "level": "1",
                    },
                    {
                        "name": "Gers: Usage 2019",
                        "url": (f'{reverse_lazy("public_data:ocsge-optimized")}' "?year=2019&color=usage"),
                        "display": False,
                        "color_property_name": "map_color",
                        "style": "get_color_from_property",
                        "level": "1",
                    },
                    {
                        "name": "Gers: artificialisation 2016 à 2019",
                        "url": (
                            f'{reverse_lazy("public_data:ocsgediff-optimized")}'
                            "?year_old=2016&year_new=2019&is_new_artif=true"
                        ),
                        "display": False,
                        "style": "get_color_for_ocsge_diff",
                        "level": "7",
                    },
                    {
                        "name": "Gers: renaturation 2016 à 2019",
                        "url": (
                            f'{reverse_lazy("public_data:ocsgediff-optimized")}'
                            "?year_old=2016&year_new=2019&is_new_natural=true"
                        ),
                        "display": False,
                        "style": "get_color_for_ocsge_diff",
                        "level": "7",
                    },
                    {
                        "name": "Gers: zones construites 2016",
                        "url": (f'{reverse_lazy("public_data:zoneconstruite-optimized")}' "?year=2016"),
                        "display": False,
                        "style": "style_zone_artificielle",
                        "level": "3",
                    },
                    {
                        "name": "Gers: zones construites 2019",
                        "url": (f'{reverse_lazy("public_data:zoneconstruite-optimized")}' "?year=2019"),
                        "display": False,
                        "style": "style_zone_artificielle",
                        "level": "3",
                    },
                    {
                        "name": "Gers: zones artificielles 2016",
                        "url": (f'{reverse_lazy("public_data:artificialarea-optimized")}' "?year=2016"),
                        "display": False,
                        "style": "style_zone_artificielle",
                        "level": "3",
                    },
                    {
                        "name": "Gers: zones artificielles 2019",
                        "url": (f'{reverse_lazy("public_data:artificialarea-optimized")}' "?year=2019"),
                        "display": False,
                        "style": "style_zone_artificielle",
                        "level": "3",
                    },
                ],
            }
        )
        return super().get_context_data(**kwargs)


class MapV2View(GroupMixin, DetailView):
    queryset = Project.objects.all()
    template_name = "carto/map_v2.html"
    context_object_name = "project"

    def get_context_breadcrumbs(self):
        breadcrumbs = super().get_context_breadcrumbs()
        breadcrumbs.append({"href": None, "title": "Carte intéractive"})
        return breadcrumbs

    def get_context_data(self, **kwargs):
        # UPGRADE: add center and zoom fields on project model
        # values would be infered when emprise is loaded
        center = self.object.get_centroid()
        # available_millesimes = self.object.get_available_millesimes(commit=True)
        all_zoom = list(range(6, 19))
        kwargs.update(
            {
                # center map on France
                "carto_name": "Project",
                "map_name": "Explorateur zones d'urbanismes",
                "project_id": self.object.pk,
                "center_lat": center.y,
                "center_lng": center.x,
                "default_zoom": 15,
                "couv_leafs": CouvertureSol.get_leafs(),
                "usa_leafs": UsageSol.get_leafs(),
                "layer_list": [
                    {
                        "name": "Fond de carte",
                        "key": "fond-de-carte",
                        "type": "tile",
                        "url": [
                            {
                                "value": "https://wxs.ign.fr/ortho/geoportail/wmts",
                                "zoom_available": all_zoom,  # Tile layers should always have all zoom available for now
                            }
                        ],
                        "url_params": {
                            "REQUEST": "GetTile",
                            "SERVICE": "WMTS",
                            "VERSION": "1.0.0",
                            "TILEMATRIXSET": "PM",
                            "LAYER": "ORTHOIMAGERY.ORTHOPHOTOS",
                            "STYLE": "normal",
                            "FORMAT": "image/jpeg",
                            "TILECOL": "{x}",
                            "TILEROW": "{y}",
                            "TILEMATRIX": "{z}",
                        },
                        "z_index": 0,
                        "is_optimized": 0,
                        "is_interactive": 0,
                        "filters": [
                            {
                                "name": "Fond de carte",
                                "type": "visible",
                                "value": "true",
                                "triggers": [
                                    {
                                        "method": "toggleVisibile",
                                        "layer": "fond-de-carte"
                                    }
                                ]
                            },
                            {
                                "name": "Visibilité du fond de carte",
                                "type": "opacity",
                                "value": 1,
                                "triggers": [
                                    {
                                        "method": "changeOpacity",
                                        "layer": "fond-de-carte"
                                    }
                                ]
                            },
                        ]
                    },
                    {
                        "name": "Limites administratives",
                        "key": "limites-administratives",
                        "type": "geojson",
                        "url": [
                            {
                                "value": reverse_lazy("public_data:commune-optimized"),
                                "zoom_available": [12, 13, 14, 15],
                            },
                            {
                                "value": reverse_lazy("public_data:epci-optimized"),
                                "zoom_available": [10, 11],
                            },
                            {
                                "value": reverse_lazy("public_data:scot-optimized"),
                                "zoom_available": [9],
                            },
                            {
                                "value": reverse_lazy("public_data:departement-optimized"),
                                "zoom_available": [8],
                            },
                            {
                                "value": reverse_lazy("public_data:region-optimized"),
                                "zoom_available": [6, 7],
                            }
                        ],
                        "style_key": "style_limites_administratives",
                        "z_index": 1,
                        "is_optimized": 1,
                        "is_interactive": 0,
                        "filters": [
                            {
                                "name": "Limites administratives",
                                "type": "visible",
                                "value": "true",
                                "triggers": [
                                    {
                                        "method": "toggleVisibile",
                                        "layer": "limites-administratives"
                                    }
                                ]
                            },
                        ]
                    },
                    {
                        "name": "Emprise du territoire",
                        "key": "emprise-du-territoire",
                        "type": "geojson",
                        "url": [
                            {
                                "value": reverse_lazy("project:emprise-list"),
                                "zoom_available": all_zoom,
                            }
                        ],
                        "url_params": {
                            "id": self.object.pk,
                        },
                        "style_key": "style_emprise",
                        "z_index": 10,
                        "is_optimized": 0,
                        "is_interactive": 0,
                        "filters": [
                            {
                                "name": "Emprise du territoire",
                                "type": "visible",
                                "value": "true",
                                "triggers": [
                                    {
                                        "method": "toggleVisibile",
                                        "layer": "emprise-du-territoire"
                                    }
                                ]
                            },
                        ]
                    },
                    {
                        "name": "Zones urbaines",
                        "key": "zones-urbaines",
                        "type": "geojson",
                        "url": [
                            {
                                "value": reverse_lazy("public_data:zoneurba-optimized"),
                                "zoom_available": list(range(12, 19)),
                            }
                        ],
                        "url_params": {
                            "type_zone": "AUc, AUs, Ah, Nd, A, N, Nh, U",
                        },
                        "label": {
                            "key": "typezone"
                        },
                        "style_key": "style_zone_urbaines",
                        "z_index": 5,
                        "is_optimized": 1,
                        "is_interactive": 1,
                        "legend": [
                            # {
                            #     "name": "ID",
                            #     "key": "id"
                            # },
                            {
                                "name": "Libellé",
                                "key": "libelle"
                            },
                            {
                                "name": "Libellé long",
                                "key": "libelong"
                            },
                            {
                                "name": "Type de zone",
                                "key": "typezone"
                            }
                        ],
                        "filters": [
                            {
                                "name": "Zonages des documents d&rsquo;urbanisme",
                                "type": "visible",
                                "value": "true",
                                "triggers": [
                                    {
                                        "method": "toggleVisibile",
                                        "layer": "zones-urbaines"
                                    }
                                ]
                            },
                            {
                                "name": "",
                                "type": "tag",
                                "value": ["AUc", "AUs", "U", "A", "N"],
                                "options": [
                                    {
                                        "name": "AUc",
                                        "value": "AUc",
                                    },
                                    {
                                        "name": "AUs",
                                        "value": "AUs",
                                    },
                                    {
                                        "name": "U",
                                        "value": "U",
                                    },
                                    {
                                        "name": "A",
                                        "value": "A",
                                    },
                                    {
                                        "name": "N",
                                        "value": "N",
                                    },
                                ],
                                "triggers": [
                                    {
                                        "method": "updateData",
                                        "param": "type_zone",
                                        "layer": "zones-urbaines"
                                    }
                                ]
                            }
                        ],
                    },
                    {
                        "name": "OCS GE",
                        "key": "ocs-ge",
                        "type": "geojson",
                        "url": [
                            {
                                "value": reverse_lazy("public_data:ocsge-optimized"),
                                "zoom_available": list(range(15, 19)),
                            }
                        ],
                        "url_params": {
                            "year": 2019,
                            "is_artificial": 1,
                        },
                        "style_key": "style_ocsge_couverture",
                        "z_index": 4,
                        "is_optimized": 1,
                        "is_interactive": 1,
                        "legend": [
                            {
                                "name": "Code couverture",
                                "key": "code_couverture"
                            },
                            {
                                "name": "Code usage",
                                "key": "code_usage"
                            },
                            {
                                "name": "Libellé couverture",
                                "key": "couverture_label_short"
                            },
                            {
                                "name": "Libellé usage",
                                "key": "usage_label_short"
                            },
                            {
                                "name": "Surface",
                                "key": "surface",
                                "formatter": ["number", ["fr-FR", "unit", "hectare", 2]]
                            },
                            {
                                "name": "Millésime",
                                "key": "year"
                            }
                        ],
                        "filters": [
                            {
                                "name": "OCS GE",
                                "type": "visible",
                                "value": "true",
                                "triggers": [
                                    {
                                        "method": "toggleVisibile",
                                        "layer": "ocs-ge"
                                    }
                                ]
                            },
                            {
                                "name": "Nomemclature",
                                "type": "select",
                                "value": "style_ocsge_couv",
                                "options": [
                                    {
                                        "name": "Couverture",
                                        "value": "style_ocsge_couverture",
                                    },
                                    {
                                        "name": "Usage",
                                        "value": "style_ocsge_usage",
                                    }
                                ],
                                "triggers": [
                                    {
                                        "method": "updateStyleKey",
                                        "layer": "ocs-ge"
                                    }
                                ]
                            },
                            {
                                "name": "Millésime",
                                "type": "select",
                                "value": 2019,
                                "options": [
                                    {
                                        "name": 2016,
                                        "value": 2016,
                                    },
                                    {
                                        "name": 2019,
                                        "value": 2019,
                                    }
                                ],
                                "triggers": [
                                    {
                                        "method": "updateData",
                                        "param": "year",
                                        "layer": "ocs-ge"
                                    }
                                ]
                            }
                        ]
                    },
                ],
            }
        )
        return super().get_context_data(**kwargs)


class UrbanZonesMapView(GroupMixin, DetailView):
    queryset = Project.objects.all()
    template_name = "carto/map_urban_zones.html"
    context_object_name = "project"

    def get_context_breadcrumbs(self):
        breadcrumbs = super().get_context_breadcrumbs()
        breadcrumbs.append({"href": None, "title": "Explorateur des zonages d'urbanisme"})
        return breadcrumbs

    def get_context_data(self, **kwargs):
        # UPGRADE: add center and zoom fields on project model
        # values would be infered when emprise is loaded
        center = self.object.get_centroid()
        # available_millesimes = self.object.get_available_millesimes(commit=True)
        all_zoom = list(range(6, 19))
        kwargs.update(
            {
                # center map on France
                "carto_name": "Project",
                "map_name": "Explorateur des zonages d'urbanisme",
                "project_id": self.object.pk,
                "center_lat": center.y,
                "center_lng": center.x,
                "default_zoom": 15,
                "couv_leafs": CouvertureSol.get_leafs(),
                "usa_leafs": UsageSol.get_leafs(),
                "layer_list": [
                    {
                        "name": "Fond de carte",
                        "key": "fond-de-carte",
                        "type": "tile",
                        "url": [
                            {
                                "value": "https://wxs.ign.fr/ortho/geoportail/wmts",
                                "zoom_available": all_zoom,  # Tile layers should always have all zoom available for now
                            }
                        ],
                        "url_params": {
                            "REQUEST": "GetTile",
                            "SERVICE": "WMTS",
                            "VERSION": "1.0.0",
                            "TILEMATRIXSET": "PM",
                            "LAYER": "ORTHOIMAGERY.ORTHOPHOTOS",
                            "STYLE": "normal",
                            "FORMAT": "image/jpeg",
                            "TILECOL": "{x}",
                            "TILEROW": "{y}",
                            "TILEMATRIX": "{z}",
                        },
                        "z_index": 0,
                        "is_optimized": 0,
                        "is_interactive": 0,
                        "filters": [
                            {
                                "name": "Fond de carte",
                                "type": "visible",
                                "value": "true",
                                "triggers": [
                                    {
                                        "method": "toggleVisibile",
                                        "layer": "fond-de-carte"
                                    }
                                ]
                            },
                            {
                                "name": "Visibilité du fond de carte",
                                "type": "opacity",
                                "value": 1,
                                "triggers": [
                                    {
                                        "method": "changeOpacity",
                                        "layer": "fond-de-carte"
                                    }
                                ]
                            },
                        ]
                    },
                    {
                        "name": "Limites administratives",
                        "key": "limites-administratives",
                        "type": "geojson",
                        "url": [
                            {
                                "value": reverse_lazy("public_data:commune-optimized"),
                                "zoom_available": [12, 13, 14, 15],
                            },
                            {
                                "value": reverse_lazy("public_data:epci-optimized"),
                                "zoom_available": [10, 11],
                            },
                            {
                                "value": reverse_lazy("public_data:scot-optimized"),
                                "zoom_available": [9],
                            },
                            {
                                "value": reverse_lazy("public_data:departement-optimized"),
                                "zoom_available": [8],
                            },
                            {
                                "value": reverse_lazy("public_data:region-optimized"),
                                "zoom_available": [6, 7],
                            }
                        ],
                        "style_key": "style_limites_administratives",
                        "z_index": 1,
                        "is_optimized": 1,
                        "is_interactive": 0,
                        "filters": [
                            {
                                "name": "Limites administratives",
                                "type": "visible",
                                "value": "true",
                                "triggers": [
                                    {
                                        "method": "toggleVisibile",
                                        "layer": "limites-administratives"
                                    }
                                ]
                            },
                        ]
                    },
                    {
                        "name": "Emprise du territoire",
                        "key": "emprise-du-territoire",
                        "type": "geojson",
                        "url": [
                            {
                                "value": reverse_lazy("project:emprise-list"),
                                "zoom_available": all_zoom,
                            }
                        ],
                        "url_params": {
                            "id": self.object.pk,
                        },
                        "style_key": "style_emprise",
                        "z_index": 10,
                        "is_optimized": 0,
                        "is_interactive": 0,
                        "filters": [
                            {
                                "name": "Emprise du territoire",
                                "type": "visible",
                                "value": "true",
                                "triggers": [
                                    {
                                        "method": "toggleVisibile",
                                        "layer": "emprise-du-territoire"
                                    }
                                ]
                            },
                        ]
                    },
                    {
                        "name": "Zones urbaines",
                        "key": "zones-urbaines",
                        "type": "geojson",
                        "url": [
                            {
                                "value": reverse_lazy("public_data:zoneurba-optimized"),
                                "zoom_available": list(range(12, 19)),
                            }
                        ],
                        "url_params": {
                            "type_zone": "AUc, AUs, Ah, Nd, A, N, Nh, U",
                        },
                        "label": {
                            "key": "typezone"
                        },
                        "style_key": "style_zone_urbaines",
                        "z_index": 5,
                        "is_optimized": 1,
                        "is_interactive": 1,
                        "legend": [
                            # {
                            #     "name": "ID",
                            #     "key": "id"
                            # },
                            {
                                "name": "Libellé",
                                "key": "libelle"
                            },
                            {
                                "name": "Libellé long",
                                "key": "libelong"
                            },
                            {
                                "name": "Type de zone",
                                "key": "typezone"
                            }
                        ],
                        "filters": [
                            {
                                "name": "Zonages des documents d&rsquo;urbanisme",
                                "type": "visible",
                                "value": "true",
                                "triggers": [
                                    {
                                        "method": "toggleVisibile",
                                        "layer": "zones-urbaines"
                                    }
                                ]
                            },
                            {
                                "name": "",
                                "type": "tag",
                                "value": ["AUc", "AUs", "U", "A", "N"],
                                "options": [
                                    {
                                        "name": "AUc",
                                        "value": "AUc",
                                    },
                                    {
                                        "name": "AUs",
                                        "value": "AUs",
                                    },
                                    {
                                        "name": "U",
                                        "value": "U",
                                    },
                                    {
                                        "name": "A",
                                        "value": "A",
                                    },
                                    {
                                        "name": "N",
                                        "value": "N",
                                    },
                                ],
                                "triggers": [
                                    {
                                        "method": "updateData",
                                        "param": "type_zone",
                                        "layer": "zones-urbaines"
                                    }
                                ]
                            }
                        ],
                    },
                    {
                        "name": "OCS GE",
                        "key": "ocs-ge",
                        "type": "geojson",
                        "url": [
                            {
                                "value": reverse_lazy("public_data:ocsge-optimized"),
                                "zoom_available": list(range(15, 19)),
                            }
                        ],
                        "url_params": {
                            "year": 2019,
                            "is_artificial": 1,
                        },
                        "style_key": "style_ocsge_couverture",
                        "z_index": 4,
                        "is_optimized": 1,
                        "is_interactive": 1,
                        "legend": [
                            {
                                "name": "Code couverture",
                                "key": "code_couverture"
                            },
                            {
                                "name": "Code usage",
                                "key": "code_usage"
                            },
                            {
                                "name": "Libellé couverture",
                                "key": "couverture_label_short"
                            },
                            {
                                "name": "Libellé usage",
                                "key": "usage_label_short"
                            },
                            {
                                "name": "Surface",
                                "key": "surface",
                                "formatter": ["number", ["fr-FR", "unit", "hectare", 2]]
                            },
                            {
                                "name": "Millésime",
                                "key": "year"
                            }
                        ],
                        "filters": [
                            {
                                "name": "OCS GE",
                                "type": "visible",
                                "value": "true",
                                "triggers": [
                                    {
                                        "method": "toggleVisibile",
                                        "layer": "ocs-ge"
                                    }
                                ]
                            },
                            {
                                "name": "Nomemclature",
                                "type": "select",
                                "value": "style_ocsge_couv",
                                "options": [
                                    {
                                        "name": "Couverture",
                                        "value": "style_ocsge_couverture",
                                    },
                                    {
                                        "name": "Usage",
                                        "value": "style_ocsge_usage",
                                    }
                                ],
                                "triggers": [
                                    {
                                        "method": "updateStyleKey",
                                        "layer": "ocs-ge"
                                    }
                                ]
                            },
                            {
                                "name": "Millésime",
                                "type": "select",
                                "value": 2019,
                                "options": [
                                    {
                                        "name": 2016,
                                        "value": 2016,
                                    },
                                    {
                                        "name": 2019,
                                        "value": 2019,
                                    }
                                ],
                                "triggers": [
                                    {
                                        "method": "updateData",
                                        "param": "year",
                                        "layer": "ocs-ge"
                                    }
                                ]
                            }
                        ]
                    },
                ],
            }
        )
        return super().get_context_data(**kwargs)


class BaseThemeMap(GroupMixin, DetailView):
    """This is a base class for thematic map. It group together layer definition, data
    provider and gradient provider.

    Main methods:
    =============
    * get_data: return GeoJson of the features to display
    * get_data_url: return endpoint url to retrieve feature to display in the map
    * get_gradient: return JSON of the coloring scale
    * get_gradient_url: return endpoint url of the coloring scale (inc. colors)
    * get_layers_list: define the layer to be display in the map
    """

    queryset = Project.objects.all()
    template_name = "carto/theme_map.html"
    context_object_name = "project"
    scale_size = 5
    title = "To be set"
    url_name = "to be set"

    def get_data_url(self):
        start = reverse_lazy(f"project:{self.url_name}", args=[self.object.id])
        return f"{start}?data=1"

    def get_gradient_url(self):
        start = reverse_lazy(f"project:{self.url_name}", args=[self.object.id])
        return f"{start}?gradient=1"

    def get_context_breadcrumbs(self):
        breadcrumbs = super().get_context_breadcrumbs()
        breadcrumbs += [
            {"title": self.title},
        ]
        return breadcrumbs

    def get_gradient(self):
        raise NotImplementedError("You need build gradient scale.")

    def get_data(self):
        raise NotImplementedError("You need build gradient scale.")

    def get_layers_list(self, *layers):
        layers = [
            {
                "name": "Emprise du projet",
                "url": (f'{reverse_lazy("project:emprise-list")}' f"?id={self.object.pk}"),
                "display": True,
                "style": "style_emprise",
                "fit_map": True,
                "level": "5",
            },
        ] + list(layers)
        return layers

    def get_context_data(self, **kwargs):
        center = self.object.get_centroid()
        kwargs.update(
            {
                # center map on France
                "map_name": self.title,
                "center_lat": center.y,
                "center_lng": center.x,
                "default_zoom": 12,
                "layer_list": self.get_layers_list(),
            }
        )
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if "gradient" in self.request.GET:
            return self.get_gradient()
        elif "data" in self.request.GET:
            return self.get_data()
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)


class MyArtifMapView(BaseThemeMap):
    title = "Comprendre l'artificialisation du territoire"

    def get_layers_list(self, *layers):
        years = (
            self.object.cities.all().first().communediff_set.all().aggregate(old=Max("year_old"), new=Max("year_new"))
        )
        layers = list(layers) + [
            {
                "name": "Artificialisation",
                "url": (
                    f'{reverse_lazy("public_data:ocsgediff-optimized")}'
                    f"?year_old={years['old']}&year_new={years['new']}"
                    f"&is_new_artif=true&project_id={self.object.id}"
                ),
                "display": True,
                "style": "get_color_for_ocsge_diff",
                "level": "7",
            },
            {
                "name": "Renaturation",
                "url": (
                    f'{reverse_lazy("public_data:ocsgediff-optimized")}'
                    f"?year_old={years['old']}&year_new={years['new']}"
                    f"&is_new_natural=true&project_id={self.object.id}"
                ),
                "display": True,
                "style": "get_color_for_ocsge_diff",
                "level": "7",
            },
            {
                "name": "Zones artificielles",
                "url": (
                    f'{reverse_lazy("public_data:artificialarea-optimized")}'
                    f"?year={years['new']}&project_id={self.object.id}"
                ),
                "display": True,
                "style": "style_zone_artificielle",
                "level": "3",
            },
        ]
        return super().get_layers_list(*layers)


class CitySpaceConsoMapView(BaseThemeMap):
    title = "Consommation d'espaces des communes de mon territoire"
    url_name = "theme-city-conso"

    def get_layers_list(self, *layers):
        layers = [
            {
                "name": "Consommation des communes",
                "url": self.get_data_url(),
                "display": True,
                "gradient_url": self.get_gradient_url(),
                "level": "2",
                "color_property_name": "artif_area",
            }
        ] + list(layers)
        return super().get_layers_list(*layers)

    def get_data(self):
        project = self.get_object()
        fields = Cerema.get_art_field(project.analyse_start_date, project.analyse_end_date)
        qs = Cerema.objects.annotate(artif_area=sum(F(f) for f in fields))
        queryset = project.cities.all().annotate(
            artif_area=Subquery(qs.filter(city_insee=OuterRef("insee")).values("artif_area")[:1]) / 10000
        )
        bbox = self.request.GET.get("bbox", None)
        if bbox is not None and len(bbox) > 0:
            polygon_box = Polygon.from_bbox(bbox.split(","))
            queryset = queryset.filter(mpoly__within=polygon_box)
        serializer = CitySpaceConsoMapSerializer(queryset, many=True)
        return JsonResponse(serializer.data, status=200)

    def get_gradient(self):
        fields = Cerema.get_art_field(self.object.analyse_start_date, self.object.analyse_end_date)
        qs = (
            self.object.get_cerema_cities()
            .annotate(conso=sum([F(f) for f in fields]) / 10000)
            .values("city_name")
            .annotate(conso=Sum(F("conso")))
            .order_by("conso")
        )
        if qs.count() <= self.scale_size:
            boundaries = sorted([i["conso"] for i in qs])
        else:
            boundaries = jenks_breaks([i["conso"] for i in qs], n_classes=self.scale_size)[1:]
        data = [{"value": v, "color": c.hex_l} for v, c in zip(boundaries, get_dark_blue_gradient(len(boundaries)))]
        return JsonResponse(data, safe=False)


class CityArtifMapView(BaseThemeMap):
    title = "Artificialisation des communes de mon territoire"
    url_name = "theme-city-artif"

    def get_layers_list(self, *layers):
        layers = [
            {
                "name": self.title,
                "url": self.get_data_url(),
                "display": True,
                "gradient_url": self.get_gradient_url(),
                "level": "2",
                "color_property_name": "surface_artif",
            },
        ] + list(layers)
        return super().get_layers_list(*layers)

    def get_gradient(self):
        boundaries = (
            self.object.cities.all()
            .filter(surface_artif__isnull=False)
            .annotate(artif=Cast("surface_artif", output_field=FloatField()))
            .order_by("artif")
            .values_list("artif", flat=True)
        )
        if len(boundaries) == 0:
            boundaries = [1]
        elif len(boundaries) > self.scale_size:
            boundaries = jenks_breaks(boundaries, n_classes=self.scale_size)[1:]
        data = [{"value": v, "color": c.hex_l} for v, c in zip(boundaries, get_yellow2red_gradient(len(boundaries)))]
        return JsonResponse(data, safe=False)

    def get_data(self):
        queryset = self.object.cities.all()
        bbox = self.request.GET.get("bbox", None)
        if bbox is not None and len(bbox) > 0:
            polygon_box = Polygon.from_bbox(bbox.split(","))
            queryset = queryset.filter(mpoly__within=polygon_box)
        serializer = CityArtifMapSerializer(queryset, many=True)
        return JsonResponse(serializer.data, status=200)

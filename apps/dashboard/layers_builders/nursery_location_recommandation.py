import json
import random
from operator import itemgetter
import folium
import geojson
import jellyfish
from area import area
from django.db.models import Sum
from shapely.geometry import shape, Point
from unidecode import unidecode
import traceback
from apps.dashboard.models import Nursery, AlteiaData, BeninYield, SpecialTuple
from apps.dashboard import utils
from apps.dashboard import models


default_number_of_tree_per_ha = 177


def __highlight_function(feature):
    return {"fillColor": "#ffaf00", "color": "green", "weight": 3, "dashArray": "1, 1"}


def get_good_shapfiles_codes(temp_geojson_a):
    polygons = []
    good_codes = []
    for feature in temp_geojson_a.data["features"]:
        code = feature["properties"]["plantation_code"]
        current_polygon = shape(feature["geometry"])
        intersect = False
        for polygon in polygons:
            if current_polygon.intersects(polygon):
                intersect = True
                break
        if intersect is False:
            polygons.append(current_polygon)
            good_codes.append(code)

    return good_codes


def get_plantation_size(feature):
    plantation_size = area(feature["geometry"]) / 10000
    plantation_size = round(plantation_size, 1)
    return plantation_size


def get_satellite_estimation_data(code: str, country: str):
    tree_ha_pred_plant = round(
        round(
            AlteiaData.objects.using(country)
            .filter(plantation_code=code)[0]
            .cashew_tree_cover
            / 10000,
            2,
        ),
        1,
    )

    return {
        "cashew_surface_area": tree_ha_pred_plant,
    }


# commune name filters
# TODO Should be in a caching function
commune_name = []
for db in utils.Countries.active():
    commune_name.extend([item.commune for item in BeninYield.objects.using(db).all()])
commune_name = list(set(commune_name))
commune_name = sorted(commune_name)


def number_of_sick_tree(commune, code: str, country: str):
    """Compute number of sick trees"""
    main_commune = None
    similarity_percentage = [
        jellyfish.jaro_similarity(unidecode(commune), unidecode(item))
        for item in commune_name
    ]
    for item in commune_name:
        if jellyfish.jaro_similarity(unidecode(commune), unidecode(item)) == max(
            similarity_percentage
        ):
            main_commune = item

    sick_tree_number = (
        BeninYield.objects.using(country)
        .filter(commune=main_commune, plantation_code__in=code)
        .aggregate(Sum("total_sick_trees"))
    )
    try:
        if sick_tree_number["total_sick_trees__sum"]:
            sick_tree_number = int(sick_tree_number["total_sick_trees__sum"])
        else:
            sick_tree_number = 0
    except Exception:
        sick_tree_number = 0
    return sick_tree_number


def number_of_dead_tree(country: str, commune, code):
    main_commune = None
    similarity_percentage = [
        jellyfish.jaro_similarity(unidecode(commune), unidecode(item))
        for item in commune_name
    ]
    for item in commune_name:
        if jellyfish.jaro_similarity(unidecode(commune), unidecode(item)) == max(
            similarity_percentage
        ):
            main_commune = item

    dead_tree_number = (
        BeninYield.objects.using(country)
        .filter(commune=main_commune, plantation_code__in=code)
        .aggregate(Sum("total_dead_trees"))
    )
    try:
        if dead_tree_number["total_dead_trees__sum"]:
            dead_tree_number = int(round(dead_tree_number["total_dead_trees__sum"], 2))
        else:
            dead_tree_number = 0
    except Exception:
        dead_tree_number = 0
    return dead_tree_number


def number_of_tree_on_the_plantation(country, commune, code):
    main_commune = None
    similarity_percentage = [
        jellyfish.jaro_similarity(unidecode(commune), unidecode(item))
        for item in commune_name
    ]
    for item in commune_name:
        if jellyfish.jaro_similarity(unidecode(commune), unidecode(item)) == max(
            similarity_percentage
        ):
            main_commune = item

    tree_number_on_the_plantation = (
        BeninYield.objects.using(country)
        .filter(commune=main_commune, plantation_code__in=code)
        .aggregate(Sum("total_number_trees"))
    )
    try:
        if tree_number_on_the_plantation["total_number_trees__sum"]:
            tree_number_on_the_plantation = int(
                tree_number_on_the_plantation["total_number_trees__sum"]
            )
        else:
            tree_number_on_the_plantation = 0
    except Exception:
        tree_number_on_the_plantation = 0
    return tree_number_on_the_plantation


def number_of_nurseries_plants(country: str, commune):
    main_commune = None
    communes_name = [item.commune for item in Nursery.objects.using(country).filter()]
    communes_name = list(set(communes_name))
    communes_name = sorted(communes_name)
    similarity_percentage = [
        jellyfish.jaro_similarity(unidecode(commune), unidecode(item))
        for item in communes_name
    ]
    for item in communes_name:
        if jellyfish.jaro_similarity(unidecode(commune), unidecode(item)) == max(
            similarity_percentage
        ):
            main_commune = item

    number_of_nurseries_plant = (
        Nursery.objects.using(country)
        .filter(commune=main_commune)
        .aggregate(Sum("number_of_plants"))
    )
    try:
        number_of_nurseries_plant = int(
            number_of_nurseries_plant["number_of_plants__sum"]
        )
    except Exception:
        number_of_nurseries_plant = 0
    return number_of_nurseries_plant


# Defining the randomization generator
def polygon_random_points(poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
        random_point = Point(
            [random.uniform(min_x, max_x), random.uniform(min_y, max_y)]
        )
        if random_point.within(poly):
            points.append(random_point)
    return points


def get_plantations_details(country: models.Country):
    try:
        # Get all plantations with available GeoJSON Geometry polygons
        alteia_json = utils.Fetcher.country_plantations(
            country=country.country_name
        ).geo
        # GeoJSON Init
        temp_geojson_a = folium.GeoJson(
            data=alteia_json,
            name="Alteia Plantation Data 2",
            highlight_function=__highlight_function,
        )
        not_overlapping_plantation = []
        not_overlapping_plantation_not_alteia = []
        not_overlapping_plantation_codes = get_good_shapfiles_codes(temp_geojson_a)
        for feature in temp_geojson_a.data["features"]:
            code = feature["properties"]["plantation_code"]
            if code in not_overlapping_plantation_codes:
                not_overlapping_plantation_not_alteia.append(feature)
                if code in [
                    item.alteia_id
                    for item in SpecialTuple.objects.using(
                        country.country_name
                    ).filter()
                ]:
                    not_overlapping_plantation.append(feature)
        all_communes = [
            feature["properties"]["admin_level_2"]
            for feature in not_overlapping_plantation_not_alteia
        ]
        all_communes = list(set(all_communes))
        all_communes = sorted(all_communes)

        all_plantations_size = [
            {
                "plantation_size": get_plantation_size(feature=feature),
                "commune": feature["properties"]["admin_level_2"].capitalize(),
            }
            for feature in not_overlapping_plantation_not_alteia
        ]
        # print(all_plantations_size, "all_plantations_size")
        all_plantations_size = sorted(all_plantations_size, key=itemgetter("commune"))

        # Convert plantation into a list of dictionaries
        plantations = [
            {
                "plantation_code": SpecialTuple.objects.using(country.country_name)
                .filter(
                    alteia_id=feature["properties"]["plantation_code"],
                )[0]
                .plantation_id,
                "plantation_alteia_code": SpecialTuple.objects.using(
                    country.country_name
                )
                .filter(
                    alteia_id=feature["properties"]["plantation_code"],
                )[0]
                .alteia_id,
                "plantation_size": get_plantation_size(feature=feature),
                "Commune": feature["properties"]["admin_level_2"].capitalize(),
            }
            for feature in not_overlapping_plantation
        ]
        plantations = sorted(plantations, key=itemgetter("Commune"), reverse=True)

        communes = [plantation["Commune"] for plantation in plantations]
        communes = list(set(communes))
        communes = sorted(communes)

        return {
            "all_plantations_size": all_plantations_size,
            "plantations": plantations,
            "communes": communes,
            "all_communes": all_communes,
        }
    except Exception as e:
        traceback.print_exc()
        print("Nursery location: ", e)
        print("Error building get_plantations_details for ", country)
        return None


def get_number_of_nurseries(country: models.Country, plantations_details):
    try:
        trees_details = [
            {
                "number_of_sick_tree": number_of_sick_tree(
                    commune=commune,
                    code=[
                        plantation["plantation_code"]
                        for plantation in plantations_details[country.country_name][
                            "plantations"
                        ]
                        if plantation["Commune"] == commune
                    ],
                    country=country.country_name,
                ),
                "number_of_dead_tree": number_of_dead_tree(
                    country=country.country_name,
                    commune=commune,
                    code=[
                        plantation["plantation_code"]
                        for plantation in plantations_details[country.country_name][
                            "plantations"
                        ]
                        if plantation["Commune"] == commune
                    ],
                ),
                "number_of_tree_on_the_plantation": number_of_tree_on_the_plantation(
                    country=country.country_name,
                    commune=commune,
                    code=[
                        plantation["plantation_code"]
                        for plantation in plantations_details[country.country_name][
                            "plantations"
                        ]
                        if plantation["Commune"] == commune
                    ],
                ),
                "number_of_nurseries_plants": number_of_nurseries_plants(
                    country=country.country_name, commune=commune
                ),
                "commune": commune,
            }
            for commune in plantations_details[country.country_name]["communes"]
        ]

        nursery_location_details = [
            {
                "sum_of_trees": sum(
                    [
                        int(x["number_of_tree_on_the_plantation"])
                        for x in trees_details
                        if x["commune"] == commune
                    ]
                ),
                "sum_of_removable_trees": sum(
                    [
                        int(x["number_of_sick_tree"] + x["number_of_dead_tree"])
                        for x in trees_details
                        if x["commune"] == commune
                    ]
                ),
                "sum_of_nurseries_plants": sum(
                    [
                        int(x["number_of_nurseries_plants"])
                        for x in trees_details
                        if x["commune"] == commune
                    ]
                ),
                "sum_of_plantations_size": sum(
                    [
                        int(plantation["plantation_size"])
                        for plantation in plantations_details[country.country_name][
                            "plantations"
                        ]
                        if plantation["Commune"] == commune
                    ]
                ),
                "sum_of_cashew_area_size": sum(
                    [
                        int(
                            get_satellite_estimation_data(
                                code=plantation["plantation_alteia_code"],
                                country=country.country_name,
                            )["cashew_surface_area"]
                        )
                        for plantation in plantations_details[country.country_name][
                            "plantations"
                        ]
                        if plantation["Commune"] == commune
                    ]
                ),
                "commune": commune,
            }
            for commune in plantations_details[country.country_name]["communes"]
        ]
        json_object = json.dumps(
            nursery_location_details, indent=4, sort_keys=True, ensure_ascii=False
        )
        with open(
            f"staticfiles/{country.country_name}/nursery_location_details.json",
            mode="w",
            encoding="utf8",
            errors="ignore",
        ) as outfile:
            outfile.write(json_object)
        free_area = [
            {
                "free_area": details["sum_of_plantations_size"]
                - details["sum_of_cashew_area_size"],
                "commune": details["commune"],
            }
            for details in nursery_location_details
        ]

        communes_details = [
            {
                "number_of_needed_plants_based_on_trees": details[
                    "sum_of_removable_trees"
                ],
                "number_of_needed_plants_based_on_area": sum(
                    [
                        area["free_area"] * 177
                        for area in free_area
                        if area["commune"] == details["commune"]
                    ]
                ),
                "commune": details["commune"],
            }
            for details in nursery_location_details
        ]

        nursery_recommandation_params = [
            {
                "sum_of_needed_plants": (
                    (
                        details["number_of_needed_plants_based_on_trees"]
                        + details["number_of_needed_plants_based_on_area"]
                    )
                    - sum(
                        [
                            detail["sum_of_nurseries_plants"]
                            for detail in nursery_location_details
                            if detail["commune"] == details["commune"]
                        ]
                    )
                    if sum(
                        [
                            detail["sum_of_nurseries_plants"]
                            for detail in nursery_location_details
                            if detail["commune"] == details["commune"]
                        ]
                    )
                    < (
                        details["number_of_needed_plants_based_on_trees"]
                        + details["number_of_needed_plants_based_on_area"]
                    )
                    else 0
                ),
                "commune": details["commune"],
            }
            for details in communes_details
        ]

        nurseries_data = [
            {
                "number_of_nurseries": round(params["sum_of_needed_plants"] / 1000),
                "sum_of_all_needed_plants": sum(
                    [
                        details["number_of_needed_plants_based_on_trees"]
                        + details["number_of_needed_plants_based_on_area"]
                        for details in communes_details
                        if details["commune"] == params["commune"]
                    ]
                ),
                "sum_of_existing_plants": sum(
                    [
                        detail["sum_of_nurseries_plants"]
                        for detail in nursery_location_details
                        if detail["commune"] == params["commune"]
                    ]
                ),
                "commune": params["commune"],
            }
            for params in nursery_recommandation_params
        ]
        nurseries_data = [
            number for number in nurseries_data if number["number_of_nurseries"]
        ]

        return nurseries_data
    except Exception as e:
        print(e)
        return None


def get_nurseries_location(country: models.Country, plantations_details):
    """ " """
    benin_adm2_json = utils.Fetcher.GAUL2(country=country.country_name).geo

    number_of_nurseries = get_number_of_nurseries(
        country.country_name, plantations_details
    )
    similarity_percentage = []
    for feature in benin_adm2_json["features"]:
        similarity_percentage.append(
            dict(
                feature=feature,
                similarity_percentage=[
                    jellyfish.jaro_similarity(
                        unidecode(item["commune"]),
                        unidecode(feature["properties"]["NAME_2"]),
                    )
                    for item in number_of_nurseries
                ],
            )
        )

    nurseries_locations = []
    for feature in benin_adm2_json["features"]:
        for item in number_of_nurseries:
            for similarity_percent in similarity_percentage:
                if (
                    jellyfish.jaro_similarity(
                        unidecode(feature["properties"]["NAME_2"]),
                        unidecode(item["commune"]),
                    )
                    == max(similarity_percent["similarity_percentage"])
                    and jellyfish.jaro_similarity(
                        unidecode(feature["properties"]["NAME_2"]),
                        unidecode(item["commune"]),
                    )
                    >= 0.8
                    and feature == similarity_percent["feature"]
                ):
                    poly = shape(feature["geometry"])
                    nurseries_locations.append(
                        dict(
                            commune=feature["properties"]["NAME_2"],
                            nurseries_location=polygon_random_points(
                                poly, item["number_of_nurseries"]
                            ),
                        )
                    )

    nurseries_locations = {x["commune"]: x for x in nurseries_locations}.values()
    nurseries_locations = [
        location for location in nurseries_locations if location["nurseries_location"]
    ]
    nurseries_locations = sorted(nurseries_locations, key=itemgetter("commune"))

    return nurseries_locations

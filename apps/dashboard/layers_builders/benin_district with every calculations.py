# import asyncio
# import json
# import time

# import folium
# import geojson
# import jellyfish
# from area import area
# from celery import shared_task
# from django.db.models import Sum, Avg
# from django.utils.translation import gettext
# from math import log10, floor
# from unidecode import unidecode

# from apps.dashboard.scripts.layers_datas_computation plantations_details, nursery_number
# from apps.dashboard.models import BeninYield, Nursery
# from apps.dashboard.models import CommuneSatellite
# # from apps.dashboard.scripts.layers_datas_computation import current_qars

# heroku = False

# # Load the Benin Communes shapefile
# with open("staticfiles/json/ben_adm3.json", encoding="utf8", errors="ignore") as f:
#     benin_adm3_json = geojson.load(f)
# satellite_prediction_computed_data_json = open('staticfiles/satellite_prediction_computed_data.json', encoding="utf8", errors="ignore")
# data_dictionary = json.load(satellite_prediction_computed_data_json)


# class DataObject:
#     def __init__(self, **entries):
#         self.__dict__.update(entries)


# def __human_format__(num):
#     num = float('{:.3g}'.format(num))
#     magnitude = 0
#     while abs(num) >= 1000:
#         magnitude += 1
#         num /= 1000.0
#     return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


# def __highlight_function__(feature):
#     """
#     Function to define the layer highlight style
#     """
#     return {"fillColor": "#ffaf00", "color": "green", "weight": 3, "dashArray": "1, 1"}


# def __get_average_nut_count__(qars: list, commune):
#     """
#       Get the average of nut_count in the district passed as parameter in the area
#     """

#     _all = list(filter(lambda c: c.commune == commune, qars))
#     total = 0
#     count = len(_all)
#     if count == 0:
#         count = 1
#     for i, x in enumerate(_all):
#         total += x.nut_count
#     result = total / count
#     return "{:.2f}".format(result) if result != 0 else "NA"


# def __get_average_defective_rate__(qars: list, commune):
#     """
#     Get the average of defective_rate in the commune passed as parameter in the area
#     """

#     _all = list(filter(lambda c: c.commune == commune, qars))
#     total = 0
#     count = len(_all)
#     if count == 0:
#         count = 1
#     for i, x in enumerate(_all):
#         total += x.defective_rate
#     result = total / count
#     return "{:.2f}".format(result) if result != 0 else "NA"


# def __get_average_kor__(qars: list, commune):
#     """
#     Get the average of kor in the commune passed as parameter in the area
#     """

#     _all = list(filter(lambda c: c.commune == commune, qars))
#     total = 0
#     count = len(_all)
#     if count == 0:
#         count = 1
#     for i, x in enumerate(_all):
#         total += x.kor
#     result = total / count
#     return "{:.2f}".format(result) if result != 0 else "NA"


# def __build_caj_q_html_view__(data: object) -> any:
#     """
#     popup's table for Caju Quality Information
#     """

#     tns_survey = gettext("TNS Survey")
#     nut_count_average = gettext("Nut Count Average")
#     defective_rate_average = gettext("Defective Rate Average")
#     kor_average = gettext("KOR Average")

#     return f'''
#                  <h4>Caju Quality Informations</h4>
#                  <table>
#                     <tr>
#                         <th></th>
#                         <th>{tns_survey}</th>
#                     </tr>
#                     <tr>
#                         <td>{nut_count_average}</td>
#                         <td>{__get_average_nut_count__(data.qars, data.commune)}</td>
#                     </tr>
#                     <tr>
#                         <td>{defective_rate_average}</td>
#                         <td>{__get_average_defective_rate__(data.qars, data.commune)}</td>
#                     </tr>
#                     <tr>
#                         <td>{kor_average}</td>
#                         <td>{__get_average_kor__(data.qars, data.commune)}</td>
#                     </tr>
#                 </table>
#             '''


# def __build_nur_recom_num_html_view__(data: object) -> any:
#     """
#     popup's table for nurseries number recommandation
#     """
#     nurseries_recommandation_informations = gettext('Nurseries recommandation informations')
#     plants_per_nursery = gettext('Plants per nursery')
#     plants_per_nursery_number = 1000
#     total_recommended_plants = gettext('Total number of recommended plants')
#     existing_plants = gettext('Existing plants')
#     missing_nurseries = gettext('Missing nurseries')

#     return f'''
#                  <h4>{nurseries_recommandation_informations}</h4>
#                  <table>
#                     <tr>
#                         <td>{plants_per_nursery}</td>
#                         <td>{plants_per_nursery_number}</td>
#                     </tr>
#                     <tr>
#                         <td>{total_recommended_plants}</td>
#                         <td>{data.needed_plants}</td>
#                     </tr>
#                     <tr>
#                         <td>{existing_plants}</td>
#                         <td>{data.existing_plants}</td>
#                     </tr>
#                     <tr>
#                         <td>{missing_nurseries}</td>
#                         <td>{data.nurseries_number}</td>
#                     </tr>
#                 </table>
#             '''


# def __build_html_view__(data: object) -> any:
#     """
#     Return the HTML view of the district Layer popup
#     """
#     # Commune translation variable
#     departments_cashew_tree = gettext('Departments Cashew Tree Cover Statistics In')
#     active_trees = gettext("Active Trees")
#     sick_trees = gettext("Sick Trees")
#     dead_trees = gettext("Dead Trees")
#     out_of_production = gettext("Out of Production Trees")
#     cashew_trees_status = gettext("Cashew Trees Status in")
#     is_ranked = gettext("is ranked")
#     satellite_est = gettext("Satellite Estimation")
#     tns_survey = gettext("TNS Survey")
#     year = gettext("In 2020, ")

#     # All 3 shapefiles share these variables
#     total_cashew_yield = gettext("Total Cashew Yield (kg)")
#     total_area = gettext("Total Area (ha)")
#     cashew_tree_cover = gettext("Cashew Tree Cover (ha)")
#     protected_area = gettext("Protected Area (ha)")
#     cashew_tree_cover_within_protected_area = gettext("Cashew Tree Cover Within Protected Area (ha)")
#     yield_hectare = gettext("Yield/Hectare (kg/ha)")
#     yield_per_tree = gettext("Yield per Tree (kg/tree)")
#     number_of_trees = gettext("Number of Trees")
#     source_tns = gettext("Source: TNS/BeninCaju Yield Surveys 2020")
#     among_benin_communes = gettext(
#         "among Benin communes in terms of total cashew yield according to the TNS Yield Survey")

#     return f'''
#                 <html>
#                 <head>
#                     <style>
#                         table {{
#                         font-family: arial, sans-serif;
#                         border-collapse: collapse;
#                         width: 100%;
#                         }}


#                         table th {{
#                         background-color: #004b55;
#                         text-align: left;
#                         color: #FFF;
#                         padding: 4px 30px 4px 8px;
#                         }}


#                         table td {{
#                         border: 1px solid #e3e3e3;
#                         padding: 4px 8px;
#                         }}


#                         table tr:nth-child(odd) td{{
#                         background-color: #e7edf0;
#                         }}
#                         </style>
#                         <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
#                         <script type="text/javascript">
#                         // Load Charts and the corechart and barchart packages.
#                         google.charts.load('current', {{'packages':['corechart']}});
#                         google.charts.load('current', {{'packages':['bar']}});

#                         // Draw the pie chart and bar chart when Charts is loaded.
#                         google.charts.setOnLoadCallback(drawChart);

#                         function drawChart() {{

#                             var data_donut = google.visualization.arrayToDataTable([
#                             ['Tree Type', 'Number of Trees'],
#                             ['{active_trees}',      {data.active_treesC}],
#                             ['{sick_trees}',      {data.sick_treeC}],
#                             ['{dead_trees}',     {data.dead_treeC}],
#                             ['{out_of_production}',      {data.out_prod_treeC}],
#                             ]);

#                             var options_donut = {{
#                             title: '{cashew_trees_status} {data.commune}',
#                             pieHole: 0.5,
#                             colors: ['007f00', '#02a8b1', '9e1a1a', '#242526'],
#                             }};

#                             var chart_donut = new google.visualization.PieChart(document.getElementById('donutchart'));
#                             chart_donut.draw(data_donut, options_donut);

#                             }};
#                         </script>
#                     </head>
#                     <body>

#                         <h2>{data.commune}</h2>
#                         <h4>
#                         {year}{data.commune}{is_ranked}
#                         {data.my_dict_communes[str(data.predictions["rank"])]}
#                         {among_benin_communes}.
#                         </h4>

#                         <table>
#                         <tr>
#                             <th></th>
#                             <th>{satellite_est}</th>
#                             <th>{tns_survey}</th>

#                         </tr>
#                         <tr>
#                             <td>{total_cashew_yield}</td>
#                             <td>{__human_format__(data.predictions["total cashew yield"])}</td>
#                             <td>{data.r_total_yieldC / 1000000:n}M</td>

#                         </tr>
#                         <tr>
#                             <td>{total_area}</td>
#                             <td>{__human_format__(data.predictions["total area"])}</td>
#                             <td>{__human_format__(data.predictions["total area"])}</td>
#                         </tr>
#                         <tr>
#                             <td>{protected_area}</td>
#                             <td>{__human_format__(data.predictions["protected area"])}</td>
#                             <td>NA</td>
#                         </tr>
#                         <tr>
#                             <td>{cashew_tree_cover}</td>
#                             <td>{__human_format__(data.predictions["cashew tree cover"])}</td>
#                             <td>{__human_format__(data.r_surface_areaC)}</td>
#                         </tr>
#                         <tr>
#                             <td>{cashew_tree_cover_within_protected_area}</td>
#                             <td>{__human_format__(data.predictions["cashew tree cover within protected area"])}</td>
#                             <td>NA</td>
#                         </tr>

#                         <tr>
#                             <td>{yield_hectare}</td>
#                             <td>{__human_format__(data.predictions["yield per hectare"])}</td>
#                             <td>{data.r_yield_haC}</td>
#                         </tr>
#                         <tr>
#                             <td>{yield_per_tree}</td>
#                             <td>
#                             {__human_format__(data.predictions["yield per tree"]) if data.predictions["yield per tree"] != 0 else "N/A"}
#                             </td>
#                             <td>{data.r_yield_treeC}</td>
#                         </tr>
#                         <tr>
#                             <td>{number_of_trees}</td>
#                             <td>
#                             {__human_format__(data.predictions["number of trees"]) if data.predictions["number of trees"] != 0 else "N/A"}
#                             </td>
#                             <td>{data.r_num_treeC / 1000:n}K</td>
#                         </tr>
#                         </table>

#                         &nbsp;&nbsp;
#                         {__build_caj_q_html_view__(data)}
#                         &nbsp;&nbsp;
#                         &nbsp;&nbsp;
#                         {__build_nur_recom_num_html_view__(data)}
#                         &nbsp;&nbsp;
#                         <table>
#                             <td><div id="donutchart" style="width: 400; height: 350;"></div></td>
#                         </table>
#                         <table>
#                             <td><div style= "text-align: center"><h5>{source_tns}</h5></div>
#                         </table>
#                     </body>
#                     </html>
#                 '''


# def __build_data__(feature, qars):
#     """
#     Return all the data needed to build the communes Layer
#     """
#     data = {'qars': qars, 'protected_area': 0,
#             "predictions": data_dictionary[feature["properties"]["NAME_0"]][feature["properties"]["NAME_1"]][
#                 feature["properties"]["NAME_2"]]}

#     # GEOJSON layer consisting of a single feature
#     commune = feature["properties"]["NAME_2"]
#     data["commune"] = commune

#     # looping through all communes in Benin Repubic to get the ranking
#     z_list = []
#     for c in range(len(CommuneSatellite.objects.all())):
#         y = CommuneSatellite.objects.all()[c].commune
#         x = CommuneSatellite.objects.filter(commune=y).aggregate(Sum('cashew_tree_cover'))
#         x = x['cashew_tree_cover__sum']
#         z_list.append((y, x))

#     sorted_by_second = sorted(z_list, reverse=True, key=lambda tup: tup[1])
#     list2, _ = zip(*sorted_by_second)

#     # A small logic to solve the French symbols name error when viewed on local host
#     if heroku:
#         position2 = list2.index(commune)
#     else:
#         position2 = 1
#     data["position2"] = position2

#     # formatted rankings in dictionary format
#     my_dict_communes = {'1': 'highest', '2': '2nd', '3': '3rd', '4': '4th', '5': '5th', '6': '6th', '7': '7th',
#                         '8': '8th', '9': '9th', '10': '10th',
#                         '11': '11th', '12': '12th', '13': '13th', '14': '14th', '15': '15th', '16': '16th',
#                         '17': '17th', '18': '18th', '19': '19th', '20': '20th',
#                         '21': '21st', '22': '22nd', '23': '23rd', '24': '24th', '25': '25th', '26': '26th',
#                         '27': '27th', '28': '28th', '29': '29th', '30': '30th',
#                         '31': '31st', '32': '32nd', '33': '33rd', '34': '34th', '35': '35th', '36': '36th',
#                         '37': '37th', '38': '38th', '39': '39th', '40': '40th',
#                         '41': '41st', '42': '42nd', '43': '43rd', '44': '44th', '45': '45th', '46': '46th',
#                         '47': '47th', '48': '48th', '49': '49th', '50': '50th',
#                         '51': '51st', '52': '52nd', '53': '53rd', '54': '54th', '55': '55th', '56': '56th',
#                         '57': '57th', '58': '58th', '59': '59th', '60': '60th',
#                         '61': '61st', '62': '62nd', '63': '63rd', '64': '64th', '65': '65th', '66': '66th',
#                         '67': '67th', '68': '68th', '69': '69th', '70': '70th',
#                         '71': '71st', '72': '72nd', '73': '73rd', '74': '74th', '75': '75th', '76': 'lowest'}
#     data["my_dict_communes"] = my_dict_communes

#     # load statistics from the database and formating them for displaying on popups

#     tree_ha_pred_comm = CommuneSatellite.objects.filter(commune=commune).aggregate(Sum('cashew_tree_cover'))
#     try:
#         tree_ha_pred_comm = int(round(tree_ha_pred_comm['cashew_tree_cover__sum'] / 10000, 2))
#     except Exception:
#         tree_ha_pred_comm = 0
#     data["tree_ha_pred_comm"] = tree_ha_pred_comm

#     surface_areaC = BeninYield.objects.filter(commune=commune).aggregate(Sum('surface_area'))
#     try:
#         surface_areaC = int(round(surface_areaC['surface_area__sum'], 2))
#     except Exception:
#         surface_areaC = 0
#     data["surface_areaC"] = surface_areaC

#     total_yieldC = BeninYield.objects.filter(commune=commune).aggregate(Sum('total_yield_kg'))
#     try:
#         total_yieldC = int(round(total_yieldC['total_yield_kg__sum'], 2))
#     except Exception:
#         total_yieldC = 0
#     data["total_yieldC"] = total_yieldC

#     yield_haC = BeninYield.objects.filter(commune=commune).aggregate(Avg('total_yield_per_ha_kg'))
#     try:
#         yield_haC = int(round(yield_haC['total_yield_per_ha_kg__avg'], 2))
#     except Exception:
#         yield_haC = 0
#     data["yield_haC"] = yield_haC

#     # Used only in case of error in the try and except catch
#     yield_treeC = BeninYield.objects.filter(commune=commune).aggregate(Avg('total_yield_per_tree_kg'))
#     try:
#         yield_treeC = int(round(yield_treeC['total_yield_per_tree_kg__avg'], 2))
#     except Exception:
#         yield_treeC = 0
#     data["yield_treeC"] = yield_treeC

#     num_treeC = BeninYield.objects.filter(commune=commune).aggregate(Sum('total_number_trees'))
#     try:
#         num_treeC = int(num_treeC['total_number_trees__sum'])
#     except Exception:
#         num_treeC = 0
#     data["num_treeC"] = num_treeC

#     sick_treeC = BeninYield.objects.filter(commune=commune).aggregate(Sum('total_sick_trees'))
#     try:
#         sick_treeC = int(sick_treeC['total_sick_trees__sum'])
#     except Exception:
#         sick_treeC = 0
#     data["sick_treeC"] = sick_treeC

#     out_prod_treeC = BeninYield.objects.filter(commune=commune).aggregate(Sum('total_trees_out_of_prod'))
#     try:
#         out_prod_treeC = int(out_prod_treeC['total_trees_out_of_prod__sum'])
#     except Exception:
#         out_prod_treeC = 0
#     data["out_prod_treeC"] = out_prod_treeC

#     dead_treeC = BeninYield.objects.filter(commune=commune).aggregate(Sum('total_dead_trees'))
#     try:
#         dead_treeC = int(round(dead_treeC['total_dead_trees__sum'], 2))
#     except Exception:
#         dead_treeC = 0
#     data["dead_treeC"] = dead_treeC

#     region_sizeC = area(feature['geometry']) / 10000
#     try:
#         active_treesC = num_treeC - sick_treeC - out_prod_treeC - dead_treeC
#     except Exception:
#         active_treesC = 0
#     data["active_treesC"] = active_treesC

#     # formating numbers greater than 90000 to show 91k
#     try:
#         r_region_sizeC = round(region_sizeC, 1 - int(floor(log10(abs(region_sizeC))))) \
#             if region_sizeC < 90000 \
#             else round(region_sizeC, 2 - int(floor(log10(abs(region_sizeC)))))
#     except Exception:
#         r_region_sizeC = region_sizeC
#     data["r_region_sizeC"] = r_region_sizeC

#     try:
#         r_tree_ha_pred_comm = round(tree_ha_pred_comm, 1 - int(
#             floor(log10(abs(tree_ha_pred_comm))))) \
#             if tree_ha_pred_comm < 90000 \
#             else round(tree_ha_pred_comm, 2 - int(floor(log10(abs(tree_ha_pred_comm)))))
#     except Exception:
#         r_tree_ha_pred_comm = tree_ha_pred_comm
#     data["r_tree_ha_pred_comm"] = r_tree_ha_pred_comm

#     try:
#         r_surface_areaC = round(surface_areaC, 1 - int(floor(log10(abs(surface_areaC))))) \
#             if surface_areaC < 90000 \
#             else round(surface_areaC, 2 - int(floor(log10(abs(surface_areaC)))))
#     except Exception:
#         r_surface_areaC = surface_areaC
#     data["r_surface_areaC"] = r_surface_areaC

#     try:
#         r_total_yieldC = round(total_yieldC, 1 - int(floor(log10(abs(total_yieldC))))) \
#             if total_yieldC < 90000 \
#             else round(total_yieldC, 2 - int(floor(log10(abs(total_yieldC)))))
#     except Exception:
#         r_total_yieldC = total_yieldC
#     data["r_total_yieldC"] = r_total_yieldC

#     try:
#         r_yield_haC = round(yield_haC, 1 - int(floor(log10(abs(yield_haC))))) \
#             if yield_haC < 90000 \
#             else round(yield_haC, 2 - int(floor(log10(abs(yield_haC)))))
#     except Exception:
#         r_yield_haC = yield_haC
#     data["r_yield_haC"] = r_yield_haC

#     try:
#         yield_pred_comm = int(r_yield_haC * tree_ha_pred_comm)
#     except Exception:
#         yield_pred_comm = 0
#     data["yield_pred_comm"] = yield_pred_comm

#     try:
#         r_yield_pred_comm = round(yield_pred_comm, 1 - int(
#             floor(log10(abs(yield_pred_comm))))) \
#             if yield_pred_comm < 90000 \
#             else round(yield_pred_comm, 2 - int(floor(log10(abs(yield_pred_comm)))))
#     except Exception:
#         r_yield_pred_comm = yield_pred_comm
#     data["r_yield_pred_comm"] = r_yield_pred_comm

#     # try: r_yield_treeC = round(yield_treeC, 1-int(floor(log10(abs(yield_treeC))))) if yield_treeC < 90000 else
#     # round(yield_treeC, 2-int(floor(log10(abs(yield_treeC))))) except Exception: r_yield_treeC = yield_treeC

#     try:
#         r_yield_treeC = round(r_total_yieldC / active_treesC)
#     except Exception:
#         r_yield_treeC = yield_treeC
#     data["r_yield_treeC"] = r_yield_treeC

#     try:
#         r_num_treeC = round(num_treeC, 1 - int(floor(log10(abs(num_treeC))))) \
#             if num_treeC < 90000 \
#             else round(num_treeC, 2 - int(floor(log10(abs(num_treeC)))))
#     except Exception:
#         r_num_treeC = num_treeC
#     data["r_num_treeC"] = r_num_treeC

#     current_commune_nurseries_number = None
#     current_commune_all_needed_plants = None
#     current_commune_existing_plants = None
#     similarity_percentage1 = [
#         jellyfish.jaro_similarity((unidecode(commune.capitalize())), unidecode(comm.capitalize())) for comm in
#         plantations_details['all_communes']]
#     plantations_size = []
#     for item in plantations_details['all_plantations_size']:
#         if jellyfish.jaro_similarity(unidecode(commune.capitalize()),
#                                      unidecode(item['commune'].capitalize())) == max(
#             similarity_percentage1) and jellyfish.jaro_similarity(unidecode(commune.capitalize()),
#                                                                   unidecode(
#                                                                       item['commune'].capitalize())) >= 0.8:
#             plantations_size.append(int(item['plantation_size']))

#     try:
#         current_commune_all_needed_plants = round(sum(plantations_size)) * 177
#         current_commune_existing_plants = round(
#             sum([int(item.number_of_plants) for item in Nursery.objects.filter(commune=commune)])) if len(
#             Nursery.objects.filter(commune=commune)) != 0 else 0
#         current_commune_nurseries_number = 0 if round(
#             (current_commune_all_needed_plants - current_commune_existing_plants) / 1000) < 0 else round((current_commune_all_needed_plants - current_commune_existing_plants) / 1000)
#     except Exception as e:
#         print(e)

#     similarity_percentage = [jellyfish.jaro_similarity(unidecode(commune), unidecode(item['commune'])) for item in
#                              nursery_number]
#     for item in nursery_number:
#         if jellyfish.jaro_similarity(unidecode(commune), unidecode(item['commune'])) == max(
#                 similarity_percentage) and jellyfish.jaro_similarity(unidecode(commune),
#                                                                      unidecode(item['commune'])) >= 0.8:
#             current_commune_nurseries_number = 0 if item['number_of_nurseries'] < 0 else item['number_of_nurseries']
#             current_commune_all_needed_plants = item['sum_of_all_needed_plants']
#             current_commune_existing_plants = item['sum_of_existing_plants']

#     data["nurseries_number"] = current_commune_nurseries_number
#     data["needed_plants"] = current_commune_all_needed_plants
#     data["existing_plants"] = current_commune_existing_plants

#     return data


# def __task__(feature, benin_district_layer, qars):
#     temp_layer3 = folium.GeoJson(feature, zoom_on_click=False, highlight_function=__highlight_function__)

#     # data = __build_data__(feature, qars)

#     # html template for the popups
#     # html_view = __build_html_view__(DataObject(**data))
#     html_view = __build_html_view__()

#     iframe = folium.IFrame(html=html_view, width=600, height=400)

#     folium.Popup(iframe, max_width=2000).add_to(temp_layer3)

#     # consolidate individual features back into the main layer
#     folium.GeoJsonTooltip(fields=["NAME_3"],
#                           aliases=["District:"],
#                           labels=True,
#                           sticky=False,
#                           style=(
#                               "background-color: white; color: black;"
#                               " font-family: sans-serif; font-size: 12px; padding: 4px;")
#                           ).add_to(temp_layer3)

#     temp_layer3.add_to(benin_district_layer)


# @shared_task(bind=True)
# def create_benin_district(self, qars):
#     """
#     Adding the shapefiles with popups for the communes
#     Add communes data to the parent layer
#     """
#     __start_time = time.time()

#     benin_district_layer = folium.FeatureGroup(name=gettext('Benin Districts'), show=False, overlay=True)
#     temp_geojson3 = folium.GeoJson(data=benin_adm3_json,
#                                    name='Benin-Adm3 Districts',
#                                    highlight_function=__highlight_function__)

#     async def __get_data__():
#         __loop = asyncio.get_event_loop()
#         futures = []
#         for feature in temp_geojson3.data['features']:
#             __start_time__ = time.time()
#             _future = __loop.run_in_executor(None, __task__, feature, benin_district_layer, qars)
#             futures.append(_future)
#         await asyncio.gather(*futures)

#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(__get_data__())
#     loop.close()
#     # __get_data__()
#     return benin_district_layer


# current_benin_district_layer = create_benin_district(current_qars)

import folium
from django.utils.translation import gettext
from folium.plugins import MarkerCluster


def __build_popup__(current_object):
    # variables for translation
    qar_region = gettext("Region")
    qar_site = gettext("Site")
    qar_kor = gettext("KOR")
    qar_nut_count = gettext("Nut Count")
    qar_defective_rate = gettext("Defective Rate")

    return f"""
            <div style="">
            <h4 style="font-family: 'Trebuchet MS', sans-serif">
                {qar_region}: <b>{current_object.department}</b>
            </h4>
            <h5 style="font-family: 'Trebuchet MS', sans-serif">
                {qar_site}: <i>{current_object.site}</i>
            </h5>
            <h5 style="font-family: 'Trebuchet MS', sans-serif">
                {qar_kor}: <b>{current_object.kor}</b>
            </h5>
            <h5 style="font-family: 'Trebuchet MS', sans-serif">
                {qar_nut_count}: <b>{current_object.nut_count}</b>
            </h5>
            <h5 style="font-family: 'Trebuchet MS', sans-serif">
                {qar_defective_rate}: <b>{current_object.defective_rate}</b>
            </h5>
            <img src="https://images.squarespace-cdn.com/content/v1/5e1197fe8aa5803c29b6b711/1580400113932-60TBXUG8S0NEZ8R4CQ1Y/08.jpg" width="200" height="133">
            </div>
        """


class QarLayer:
    def __init__(self, marker_cluster, qars):
        self.qars = qars
        self.marker_cluster = marker_cluster

    def add_qar(self, country):
        # Loop through every nursery owner and add to the nursery marker popups
        iconurl = "https://cdn.mapmarker.io/api/v1/font-awesome/v5/pin?icon=fa-warehouse&size=50&hoffset=0&voffset=-1&background=1167b1"
        marker_datas = []
        for i in range(len(self.qars)):
            current_object = self.qars[i]
            icon = folium.features.CustomIcon(
                iconurl,
                icon_size=(45, 45),
            )
            marker = folium.Marker(
                location=[current_object.latitude, current_object.longitude],
                rise_on_hover=True,
                rise_offset=500,
                icon=icon,
                popup=__build_popup__(current_object),
            )
            marker.add_to(self.marker_cluster)
            marker_datas.append(marker)

        return self.marker_cluster, marker_datas


def create_qar(current_qars_imported, country):
    print(f"Creating QAR layer {country}")
    try:
        qars = current_qars_imported[country]
        marker_cluster = MarkerCluster(name=gettext("Warehouse Location"), show=True)
        qar_layer = QarLayer(marker_cluster, qars).add_qar(country)
    except Exception as e:
        qar_layer = None, None
        print(e)
        pass
    return qar_layer

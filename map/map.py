import folium
import pandas

data = pandas.read_csv("volcanoes.txt")

lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])


def color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.03, -99.04],
                 zoom_start=6, titles="Mapbox Bright")

fg = folium.FeatureGroup(name="my map")

for la, lo, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(
        location=[la, lo], radius=6, popup=el, fill_color=color(el), color='green', fill_opacity=0.9))


fg.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig'), style_function=lambda x: {'fillcolor': 'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Map1.html")

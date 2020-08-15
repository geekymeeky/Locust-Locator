import requests
from flask import Blueprint, render_template
from app.settings import G_API
blueprint = Blueprint('lmap', __name__)
import gmplot 
'''
def GetUserGeoLocation():
    url = 'http://ipinfo.io/json '
    payload = {}
    files = {}
    headers= {}
    
    response = requests.request("GET", url, headers=headers, data = payload, files = files)
    data = response.json()
    list1=data["loc"].split(sep=",")
    return list1
'''
'''def getmap():
    """from_geocode method return the 
    latitude and longitude of given location .""" 
    User=GetUserGeoLocation()
    latitude_list, longitude_list = [11.059821, 17.123184], [78.387451, 79.208824]
    gmap = gmplot.GoogleMapPlotter.from_geocode("India", apikey=G_API,zoom=1)
    gmap.marker(float(User[0]), float(User[1]), color='Green', edge_width = 2.5,title="You")
    for i in range(len(latitude_list)):
        gmap.marker(latitude_list[i], longitude_list[i],  
               'cornflowerblue', edge_width = 2.5)
    gmap.draw( "app/templates/map/lmap.html" )

'''
'''@blueprint.route('/map')
def lmap():
    getmap()
    return render_template('map/lmap.html')
'''
@blueprint.route('/map')
def dash():
    return render_template('map/index.html')    


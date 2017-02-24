import urllib
import json
from urllib import request

city_dict={'Iasi':'675810','Suceava':'665849','Vaslui':'663118','Covasna':'680428'}

city_name=input('Name of City')
AppKEY ="99bc216d5e4421eeb06fbbb0e974427d"

urlManagement = 'http://api.openweathermap.org/data/2.5/forecast/city?id='+city_dict[city_name]+'&APPID='+AppKEY
print(urlManagement)
try:
    response = urllib.request.urlopen(urlManagement).read()
    print(response)

except Exception as e:
    print("Error -> ", e)

from flask import request
from flask import Flask, jsonify
import urllib
import json

app = Flask(__name__)

@app.route('/math_api/nsum', methods=['GET'])
def reverse():
    n=request.args.get('number')

    sum=0
    if n != None and str.isnumeric(n)==True:
        for iterator in range(0,int(n)+1):
            sum=sum+iterator
    else:
        sum='parameter was not a number'

    jsonToSend=jsonify({'sum':sum})
    return jsonToSend

@app.route('/string_api/reverse', methods=['GET'])
def get_sum_of_n():
    n=request.args.get('string')

    if n != None:
        n=n[::-1]
    else:
        n='parametre is not valid'

    jsonToSend=jsonify({'reverse_string':n})
    return jsonToSend

@app.route('/reverse_math', methods=['GET'])
def reverse_and_sum():
    reverse=request.args.get('string')
    n=request.args.get('number')

    response_reversed=''
    response_sum=0

    if reverse!=None and n!=None:

        try:
            urlManagement = 'http://127.0.0.1:5000/string_api/reverse?string=' + reverse
            response = urllib.request.urlopen(urlManagement)
            encoding = response.info().get_content_charset('utf8')
            data = json.loads(response.read().decode(encoding))
            response_reversed=data['reverse_string']

            urlManagement = 'http://127.0.0.1:5000/math_api/nsum?number=' + n
            response = urllib.request.urlopen(urlManagement)
            encoding = response.info().get_content_charset('utf8')
            data = json.loads(response.read().decode(encoding))
            response_sum = data['sum']

        except Exception as e:
            print("Error -> ", e)

    jsonToSend=jsonify({'reverse_string':response_reversed,'sum':response_sum})
    return jsonToSend

@app.route('/weather', methods=['GET'])
def get_weather():
    city_name = request.args.get('city')

    city_dict = {'Iasi': '675810', 'Suceava': '665849', 'Vaslui': '663118', 'Covasna': '680428'}

    AppKEY = "99bc216d5e4421eeb06fbbb0e974427d"
    weather=0

    urlManagement = 'http://api.openweathermap.org/data/2.5/forecast/city?id=' + city_dict[
        city_name] + '&APPID=' + AppKEY
    print(urlManagement)
    try:
        response = urllib.request.urlopen(urlManagement)
        encoding = response.info().get_content_charset('utf8')
        data = json.loads(response.read().decode(encoding))
        weather=data

    except Exception as e:
        print("Error -> ", e)

    jsonToSend=jsonify({'weather':weather})
    return jsonToSend
if __name__ == '__main__':
    app.run(threaded=True)
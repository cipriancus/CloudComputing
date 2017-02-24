from flask import request
from flask import Flask, jsonify
import urllib
import json


string="ciprian"
urlManagement = 'http://127.0.0.1:5000/string_api/reverse?string=' + string
response = urllib.request.urlopen(urlManagement)
encoding = response.info().get_content_charset('utf8')
data = json.loads(response.read().decode(encoding))
response_reversed=data['reverse_string']
print(response_reversed)

n=str(10)
urlManagement = 'http://127.0.0.1:5000/math_api/nsum?number=' + n
response = urllib.request.urlopen(urlManagement)
encoding = response.info().get_content_charset('utf8')
data = json.loads(response.read().decode(encoding))
response_sum = data['sum']
print(response_sum)

urlManagement = 'http://127.0.0.1:5000/reverse_math?number=' + n+"&string="+string
response = urllib.request.urlopen(urlManagement)
encoding = response.info().get_content_charset('utf8')
data = json.loads(response.read().decode(encoding))
print(data)

city='Iasi'
urlManagement = 'http://127.0.0.1:5000/weather?city=' + city
response = urllib.request.urlopen(urlManagement).read()
print(response)
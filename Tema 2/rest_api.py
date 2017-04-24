#GET /orders --> returns all orders present in the system
#POST /orders --> inserts new order in system | with oder_date,order_obj-> return order_id
#PUT /orders/order_id -> updates and order
#DELETE /orders/order_id -> deletes and order


import time
import BaseHTTPServer
import time
import re
import json as simplejson
import random

class order:
    def __init__(self):
        self.order_date=time.time()
        self.order_id=0
        self.order_obj=''


HOST_NAME = '127.0.0.1'
PORT_NUMBER = 9000

orders = dict()

order0=order()
order0.order_obj='telefon'
order0.id=0
orders[order0.id]=order0

nr_of_orders=0

def for0for(s):
    s.send_response(404)
    s.send_header("Content-type", "text/html")
    s.end_headers()
    s.wfile.write("<html><head><title>404 NOT FOUND</title></head>")
    s.wfile.write("<body><p>Page not found</p>")
    s.wfile.write("</body></html>")

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        global orders
        if s.path=='/orders':
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write("<html><head><title>All orders</title></head>")

            for iterator in orders.keys():
               s.wfile.write("<body><p>"+orders[iterator].order_obj+" "+str(orders[iterator].order_id)+" "+"</p>")

            s.wfile.write("</body></html>")
        else:
            for0for(s)

    def do_DELETE(s):
        global orders
        if re.match('/orders/\d+',s.path):
            result= re.search('/orders/(\d+)',s.path)

            if int(result.group(1)) in orders.keys():
                del orders[int(result.group(1))]
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
                s.wfile.write("<html><head><title>Deleted order</title></head>")
                s.wfile.write("<body><p>Deleted</p></body>")
                s.wfile.write("</body></html>")
            else:
                for0for(s)

            s.wfile.write("</body></html>")
        else:
            for0for(s)

    def do_PUT(s):
            global orders
            if re.match('/orders/\d+', s.path):
                result = re.search('/orders/(\d+)', s.path)

                if int(result.group(1)) in orders.keys():
                    order0=orders[int(result.group(1))]

                    content_len = int(s.headers.getheader('content-length', 0))
                    post_body = s.rfile.read(content_len)
                    data = simplejson.loads(post_body)

                    if 'order_obj' in data.keys():
                        order0.order_obj=data['order_obj']
                        order0.order_date=time.time()
                        orders[order0.order_id]=order0
                    else:
                        for0for(s)

                    s.send_response(200)
                    s.send_header("Content-type", "text/html")
                    s.end_headers()
                    s.wfile.write("<html><head><title>Deleted order</title></head>")
                    s.wfile.write("<body><p>Edited</p></body>")
                    s.wfile.write("</body></html>")
                else:
                    for0for(s)

                s.wfile.write("</body></html>")
            else:
                for0for(s)


    def do_POST(s):
        global orders,nr_of_orders
        if s.path == '/orders':
            content_len = int(s.headers.getheader('content-length', 0))
            post_body = s.rfile.read(content_len)
            data = simplejson.loads(post_body)

            new_order=order()
            nr_of_orders=nr_of_orders+1
            new_order.order_id=nr_of_orders
            new_order.order_date=time.time()

            if 'order_obj' in data.keys():
                new_order.order_obj = data['order_obj']
                orders[new_order.order_id] = new_order
            else:
                for0for(s)

            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.end_headers()
            s.wfile.write("<html><head><title>Deleted order</title></head>")
            s.wfile.write("<body><p>Inserted</p></body>")
            s.wfile.write("</body></html>")

        else:
            for0for(s)


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
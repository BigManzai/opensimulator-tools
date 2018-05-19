#!/usr/bin/python

import http.client

HOST_NAME = "192.168.1.2"
PORT_NUMBER = 9000

conn = http.client.HTTPConnection(HOST_NAME, PORT_NUMBER)

# It doesn't currently matter what we request here
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print(r1.status, r1.reason)
conn.close()

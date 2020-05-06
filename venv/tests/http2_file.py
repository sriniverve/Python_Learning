'''
this is to demonstrate usage of HTTP2
'''

from hyper import HTTPConnection

conn = HTTPConnection('youtube.com')
conn.request('GET', '/get')
resp = conn.get_response()

print(resp.read())
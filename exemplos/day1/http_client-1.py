from urllib.request import urlopen
result  = urlopen("http://example.com/index.html")
print(result)
print(result.status)
print(result.getheaders())
print(result.getheader('Content-Type'))
print(result.read().decode('utf-8'))


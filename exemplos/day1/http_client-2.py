import httpx
result  = httpx.get("http://example.com/index.html")
print(result.status_code)
print(result.headers)   
print(result.content)

import  urllib.parse
url="https://www.google.com/search?q=sathyabama+lms&oq=&aqs=chrome.0.69i59i450l8.123235272j0j15&sourceid=chrome&ie=UTF-8"
tpl=urllib.parse.urlparse(url)
print(tpl)

print("scheme=",tpl.scheme)
print("net location=",tpl.netloc)
print("path=",tpl.path)
print("port=",tpl.port)
print("fragment=",tpl.fragment)
print("totalurl=",tpl.geturl())

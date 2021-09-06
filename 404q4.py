import requests
import sys
print("The version of the requests is: %s" % requests.__version__)
print("Python version: %s" % sys.version)
print("")

r = requests.get('http://www.google.com/')
print(r.url)
print(r)
print(r.text)

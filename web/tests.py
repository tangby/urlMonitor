from django.test import TestCase
import requests
import time
# Create your tests here.

begin= time.time()
r=requests.get('http://www.facebook.com')
print r.elapsed.microseconds/1000
end=time.time()
print begin
print end
print end-begin
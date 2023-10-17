
import os
import urllib.request

def save_raw_file(url, filename):
    urllib.request.urlretrieve(url, filename)
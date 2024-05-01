import time
from seleniumwire import webdriver
import os

def get_headers(req):
    with open('headers.json','a') as f:
        if req.url == 'https://vwc.cinesa.es/WSVistaWebClient/ocapi/v1/films':
            f.write('{\n')
            headers_str = ",\n".join([f'"{key}": "{value}"' for key, value in req.headers.items()])
            f.write(headers_str)
            f.write('\n}')
            f.close()

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)
driver.request_interceptor =get_headers

os.remove('headers.json')
driver.get('https://www.cinesa.es/cines/oasiz/')
time.sleep(10)
driver.quit()

import json
import base64
from selenium.webdriver.remote.remote_connection import RemoteConnection
import selenium.webdriver.common.devtools.v96 as devtools
import asyncio
from selenium.webdriver.remote.webdriver import RemoteConnection
# import selenium.webdriver.common.devtools.v96 as devtools
from selenium.webdriver.common.bidi import cdp
from selenium import webdriver
import parser
from urllib import parse
from urllib.parse import urlparse

# browser_ip = '212.26.138.5'
# browser_ip ='127.0.0.1'
#
# capabilities = {
#         "browserName": "chrome",
#         "version": "99.0",
#         "enableVNC": True,
#         "enableVideo": False,
#         "platform": "LINUX"
#            }
def get_auth_header(user, password):
    b64 = "Basic " + base64.b64encode('{}:{}'.format(user, password).encode('utf-8')).decode('utf-8')
    headers = {'headers':{"Authorization":b64}}
    return json.dumps(headers)

# driver = webdriver.Remote(command_executor = f'http://{browser_ip}:4444/wd/hub', desired_capabilities=capabilities)


# {"headers": get_auth_header(os.getenv('user'), os.getenv("password"))})
url = 'http://gcst.meteo.gov.ua/armua/sino/index.phtml'


# load_dotenv()
aut = get_auth_header('chernovcgm', "(zBLFX$#)b")
print(aut)
# dev = devtools.network.enable()
# dev.send()
# r = RemoteConnection
# username='chernovcgm'
# password= "(zBLFX$#)b"
# f'http://{username}:{password}gcst.meteo.gov.ua/armua/sino/index.phtml'
# # r.get_remote_connection_headers()
#
# print(r)
# driver.get('https://www.google.com')



# def test_get_remote_connection_headers_adds_auth_header_if_pass():
#     username = 'chernovcgm'
#     password = '(zBLFX$#)'
#     url = f'htpp://{username}@{password}gcst.meteo.gov.ua/armua/sino/index.phtml'
#     print(parse.urlparse(url, allow_fragments=False))
#     headers = RemoteConnection.get_remote_connection_headers(parse.urlparse(url))
#     # print(headers.items())
#     headers.get('Authorization')

import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)


def send(driver, cmd, params={}):
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    print(url)
    body = json.dumps({'cmd': cmd, 'params': params})
    print(body)
    response = driver.command_executor._request('POST', url, body)
    print(response)
    return response.get('value')
cmd = "Network.setExtraHTTPHeaders"
params = get_auth_header('chernovcgm', "(zBLFX$#)b")
# send(driver=driver, cmd=cmd, params=params)
print(send(driver=driver, cmd=cmd, params=params))
driver.get('https://www.google.com')
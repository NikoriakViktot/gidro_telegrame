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

browser_ip = '212.26.138.5'
capabilities = {
        "browserName": "chrome",
        "version": "99.0",
        "enableVNC": True,
        "enableVideo": False,
        "platform": "LINUX"
           }
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
dev = devtools.network.enable()
# dev.send()
# r = RemoteConnection
# username='chernovcgm'
# password= "(zBLFX$#)b"
# f'http://{username}:{password}gcst.meteo.gov.ua/armua/sino/index.phtml'
# # r.get_remote_connection_headers()
#
# print(r)
# driver.get('https://www.google.com')
async def geoLocationTest():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor=f'http://{browser_ip}:4444/wd/hub',
        options=chrome_options
    )

    async with driver.bidi_connection() as session:
        cdpSession = session.session
        await cdpSession.execute(devtools.emulation.set_geolocation_override(latitude=41.8781,longitude=-87.6298,accuracy=100))
    driver.get("https://my-location.org/")
    driver.quit()

def test_get_remote_connection_headers_adds_auth_header_if_pass():
    username = 'chernovcgm'
    password = '(zBLFX$#)'
    url = f'htpp://{username}@{password}gcst.meteo.gov.ua/armua/sino/index.phtml'
    print(parse.urlparse(url, allow_fragments=False))
    headers = RemoteConnection.get_remote_connection_headers(parse.urlparse(url))
    # print(headers.items())
    headers.get('Authorization')


test_get_remote_connection_headers_adds_auth_header_if_pass()
import datetime
import base64
import parser
import time
import os
from dotenv import load_dotenv
import json
import asyncio
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Chrome, Remote
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telegrame_save.request_index import request_index
from meteo_telegrame.request_index_meteo import request_index_meteo
import selenium.webdriver.common.devtools.v96 as devtools
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.bidi import cdp
import requests
from selenium import webdriver
import tracemalloc
from requests.auth import HTTPBasicAuth

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

# url = 'http://gcst.meteo.gov.ua/armua/sino/index.phtml'

# def test_get_remote_connection_headers_adds_auth_header_if_pass():
#     load_dotenv()
#     url = f'http://{os.getenv("user")}:{os.getenv("password")}@gcst.meteo.gov.ua/armua/sino/index.phtml'
#     headers = RemoteConnection.get_remote_connection_headers(url)
#     return headers.get('Authorization') == 'Basic Y2hlcm5vdmNnbTooekJMRlgkIyli'
aut = get_auth_header('chernovcgm', "(zBLFX$#)b")
# a = RemoteConnection.get_remote_connection_headers(parsed_url=url)
driver = webdriver.Remote(command_executor = f'http://{browser_ip}:4444/wd/hub', desired_capabilities=capabilities)
# headers = RemoteConnection.get_remote_connection_headers(parser.expr(url))
print(aut)
# print(test_get_remote_connection_headers_adds_auth_header_if_pass())
desired_cap = {
  'unhandledPromptBehavior': 'ignore'
}

# driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')
# driver.execute_script("executeScript",('chernovcgm',"(zBLFX$#)b"))
# driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')

# driver.execute_async_script('browserstack_executor: {"action": "sendBasicAuth", "arguments": {"username":"chernovcgm", "password":"(zBLFX$#)b", "timeout": "10"}}')
# with driver.bidi_connection() as session:
#     cdp_session = session.session
#     load_dotenv()
#     cdp_session.execute(devtools.network.enable().send("Network.setExtraHTTPHeaders",
#                                                        {"headers": get_auth_header(os.getenv('user'), os.getenv("password"))}))
#     driver.get(url)
d = cdp
# tracemalloc.start()
f = devtools
f.network.enable()
# d.CdpSession.execute("Network.enable", {})
# # d.set_global_connection("Network.enable", {})
load_dotenv()
# f.network.set_extra_http_headers({"headers": get_auth_header(os.getenv('user'), os.getenv("password"))})
# d.CdpSession.execute("Network.setExtraHTTPHeaders",
#                        {"headers": get_auth_header(os.getenv('user'), os.getenv("password"))})
# driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')
g = f.network.Headers.to_json(aut)
print(g)
kk = f.network.set_extra_http_headers(f.network.Headers.to_json(aut))
driver.execute('get', )
# c = f.network.set_extra_http_headers(g)
# print(c)
# driver.execute('get', c.send(None))
# cmd = "Network.setUserAgentOverride"
# ua = "My brand new user agent!"
# cmd_args = dict(userAgent=ua)
#
# driver.execute("executeCdpCommand", {"cmd": cmd, "params": cmd_args})
# assert ua == driver.execute_script("return navigator.userAgent;")
# session = requests.Session()
# www_request = session.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml', auth=HTTPBasicAuth('chernovcgm', "(zBLFX$#)b"), allow_redirects=False)
# print(www_request)
# driver.get(url)

# url = 'http://gcst.meteo.gov.ua/armua/sino/index.phtml'
# driver = webdriver.Remote(command_executor=f'http://{browser_ip}:4444/wd/hub', desired_capabilities=capabilities, )

# load_dotenv()
# username = {"username":'chernovcgm', "password":"(zBLFX$#)b"}
#
# driver.execute_cdp_cmd("Network.setExtraHTTPHeaders",
#                        {"headers": get_auth_header(os.getenv('user'), os.getenv("password"))})
# driver.execute('get', params='/session/$sessionId/title')
# driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')

# for key in cookies:
#     driver.add_cookie({'name': key, 'value': cookies[key]})
# browser_ip = '212.26.138.5'
# capabilities = {
#        "browserName": "chrome",
#         "version": "99.0",
#         "enableVNC": True,
#         "enableVideo": False,
#         "platform": "LINUX"
#            }
# driver = webdriver.Remote(command_executor=f'http://{browser_ip}:4444/wd/hub', desired_capabilities=capabilities)

# driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')
# cookies = session.cookies.get_dict()
# for key in cookies:
#     driver.add_cookie({'name': key, 'value': cookies[key]})
#
# driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')
# # browser_ip = '212.26.138.5'
# capabilities = {
#        "browserName": "chrome",
#         "version": "99.0",
#         "enableVNC": True,
#         "enableVideo": False,
#         "platform": "LINUX"
#            }
# driver = webdriver.Remote(command_executor=f'http://{browser_ip}:4444/wd/hub', desired_capabilities=capabilities)
# def get_auth_header(user, password):
#     b64 = "Basic " + base64.b64encode('{}:{}'.format(user, password).encode('utf-8')).decode('utf-8')
#     return {"Authorization": b64}
#

# chrome_options = Options()
# chrome_options.headless = True
# service = Service(executable_path=ChromeDriverManager().install())

# driver = webdriver.Chrome(service=service, options=chrome_options)
# load_dotenv()
# # driver.get('https://www.google.com')
# driver.get_screenshot_as_base64()
# driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')
# print(driver.command_executor)
# desired_cap = {
#   'unhandledPromptBehavior': 'ignore'}
# # driver.execute_script('browserstack_executor: {"action": "sendBasicAuth", "arguments": {"chernovcgm", "(zBLFX$#)b" }}')
#
# test = driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
# # test_= driver.current_window_handle
# # print(test_)
# for item in test:
#   print(item)
# # driver.command_executor

# driver.("Network.enable", {})
# load_dotenv()
# driver.execute("Network.setExtraHTTPHeaders",
#                        {"headers": get_auth_header(os.getenv('user'), os.getenv("password"))})
# driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')

# def post_gidro_telegrame():
#     # driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')
#     time.sleep(0.3)
#     for value in request_index():
#         index = value[0]
#
#         time.sleep(0.1)
#         driver.implicitly_wait(time_to_wait=0.2)
#         time.sleep(0.1)
#         driver.find_element(by=By.CLASS_NAME, value='submenu'). \
#                 find_element(by=By.XPATH,
#                              value='/html/body/table/tbody/tr/td[1]/a[10]').click()
#         time.sleep(0.3)
#
#         try:
#             WebDriverWait(driver, 0.3).until(EC.presence_of_element_located((By.CLASS_NAME, "t1")))
#             time.sleep(0.3)
#             driver.find_element(by=By.CLASS_NAME, value='t1').send_keys(index)
#             time.sleep(0.1)
#             driver.implicitly_wait(time_to_wait=0.3)
#             print(f' write {index}')
#             time.sleep(0.1)
#             driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/'
#                                 'form/table/tbody/tr[2]/td[1]/table'
#                                 '/tbody/tr[3]/td/font/input[2]').clear()
#             time.sleep(0.1)
#             driver.find_element(by=By.XPATH,
#                                 value='/html/body/table/tbody/tr/td[2]/'
#                                    'form/table/tbody/tr[2]/td[1]/'
#                                    'table/tbody/tr[3]/td/font/input[2]')\
#                                 .send_keys(datetime.date.today().strftime("%Y-%m-%d")+ ' ' + '09:00:36')
#             time.sleep(0.1)
#             driver.find_element(by=By.XPATH,
#                                 value='/html/body/table/tbody/tr/td[2]/'
#                                       'form/table/tbody/tr[1]/td/input[2]').click()
#             time.sleep(0.1)
#             file_object = open(f'../telegrame_save/data_html/{index}.html', "w", encoding=('koi8-u'))
#             html = driver.page_source
#             time.sleep(0.1)
#             file_object.write(html)
#             time.sleep(0.1)
#             file_object.close()
#             print(f'save _____{index}____.html')
#             driver.refresh()
#             print("__new index__")
#             time.sleep(0.2)
#         except:
#             driver.refresh()
#             time.sleep(0.2)
#             print(f'not save {index}')
#             driver.find_element(by=By.CLASS_NAME, value='submenu').find_element(by=By.XPATH,
#                                 value='/html/body/table/tbody/tr/td[1]/a[10]').click()
#             time.sleep(1.5)
#
#     driver.close()
#     print(f'save telegrame {datetime.date.today().strftime("%Y-%m-%d")}')
#     driver.quit()
#
#
# def post_meteo_telegrame():
#     driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')
#     time.sleep(0.3)
#     for value in request_index_meteo():
#         index = value[0]
#         time.sleep(0.1)
#         driver.implicitly_wait(time_to_wait=0.5)
#         time.sleep(0.2)
#
#         driver.find_element(by=By.CLASS_NAME, value='submenu'). \
#                 find_element(by=By.XPATH,
#                              value='/html/body/table/tbody/tr/td[1]/a[7]').click()
#         time.sleep(0.3)
#
#         try:
#             WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "t1")))
#             driver.find_element(by=By.CLASS_NAME, value='t1').send_keys(index)
#             time.sleep(0.2)
#             driver.implicitly_wait(time_to_wait=1.0)
#             print(f' write {index}')
#             time.sleep(0.2)
#             driver.find_element(by=By.XPATH,
#                                 value='/html/body/table/tbody/tr/td[2]/'
#                                       'form/table/tbody/tr[1]/td/input[2]').click()
#             time.sleep(0.2)
#             file_object = open(f'../meteo_telegrame/data_html/{index}.html', "w", encoding=('koi8-u'))
#             html = driver.page_source
#             time.sleep(0.2)
#             file_object.write(html)
#             time.sleep(0.1)
#             file_object.close()
#             print(f'save _____{index}____.html')
#             driver.refresh()
#             print("__new index__")
#             time.sleep(0.2)
#         except:
#             driver.refresh()
#             time.sleep(0.2)
#             print(f'not save {index}')
#             driver.find_element(by=By.CLASS_NAME, value='submenu').find_element(by=By.XPATH,
#                                 value='/html/body/table/tbody/tr/td[1]/a[7]').click()
#             time.sleep(1.5)
#     driver.close()
#     print(f'save telegrame {datetime.date.today().strftime("%Y-%m-%d")}')
#     driver.quit()


#
# def post_gidro_telegrame_all(index):
#     driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')
#     time.sleep(0.3)
#     time.sleep(0.1)
#     driver.implicitly_wait(time_to_wait=0.2)
#     time.sleep(0.1)
#     driver.find_element(by=By.CLASS_NAME, value='submenu'). \
#                 find_element(by=By.XPATH,
#                              value='/html/body/table/tbody/tr/td[1]/a[10]').click()
#     time.sleep(0.3)
#
#     try:
#         WebDriverWait(driver, 0.3).until(EC.presence_of_element_located((By.CLASS_NAME, "t1")))
#         time.sleep(0.3)
#         driver.find_element(by=By.CLASS_NAME, value='t1').send_keys(index)
#         time.sleep(0.1)
#         driver.implicitly_wait(time_to_wait=0.3)
#         print(f' write {index}')
#         time.sleep(0.1)
#         driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/form/table/' \
#         'tbody/tr[2]/td[1]/table/tbody/tr[3]/td/font/input[1]').clear()
#         driver.find_element(by=By.XPATH,value='/html/body/table/tbody/tr/td[2]/form/table/' \
#         'tbody/tr[2]/td[1]/table/tbody/tr[3]/td/font/input[1]') \
#             .send_keys('2')
#         driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/'
#                                 'form/table/tbody/tr[2]/td[1]/table'
#                                 '/tbody/tr[3]/td/font/input[2]').clear()
#         time.sleep(0.1)
#         driver.find_element(by=By.XPATH,
#                                 value='/html/body/table/tbody/tr/td[2]/'
#                                    'form/table/tbody/tr[2]/td[1]/'
#                                    'table/tbody/tr[3]/td/font/input[2]')\
#                                 .send_keys(datetime.date.today().strftime("%Y-%m-%d")+ ' ' + '10:00:36')
#         time.sleep(0.1)
#         driver.find_element(by=By.XPATH,
#                                 value='/html/body/table/tbody/tr/td[2]/'
#                                       'form/table/tbody/tr[1]/td/input[2]').click()
#         time.sleep(0.1)
#         file_object = open(f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html', "w", encoding=('koi8-u'))
#         html = driver.page_source
#         time.sleep(0.1)
#         file_object.write(html)
#         time.sleep(0.1)
#         file_object.close()
#         print(f'save _____{index}____.html')
#         driver.refresh()
#         print("__new index__")
#         time.sleep(0.2)
#     except:
#         driver.refresh()
#         time.sleep(0.2)
#         print(f'not save ')
#         driver.find_element(by=By.CLASS_NAME, value='submenu').find_element(by=By.XPATH,
#                                 value='/html/body/table/tbody/tr/td[1]/a[10]').click()
#         time.sleep(1.5)
#
#     driver.close()
#     print(f'save telegrame {datetime.date.today().strftime("%Y-%m-%d")}')
#     driver.quit()

# post_gidro_telegrame()
# post_meteo_telegrame()
# def index_gidropost()->str:
#     i = []
#     for value in request_index():
#         i.append(value[0])
#     index = ' '.join(i)
#     return index

# print(index_gidropost())

# post_gidro_telegrame_all(index_gidropost())

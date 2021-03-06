import time
import os
from dotenv import load_dotenv
import json
import base64
import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telegrame_save.class_db import Database

# username = 'chernovcgm'
# password = '(zBLFX$#)'


def get_auth_header(user, password):
    b64 = "Basic " + base64.b64encode('{}:{}'.format(user, password).encode('utf-8')).decode('utf-8')
    return {"Authorization": b64}


def execute_cmd(driver, cmd, params):
    resource = f"/session/{driver.session_id}/chromium/send_command_and_get_result"
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    return response.get('value')


def get_driver():
    print('Connecting to Selenoid Chrome')
    browser_ip = '212.26.138.5'
    options = webdriver.ChromeOptions()
    options.set_capability('selenoid:options', {"enableVNC": True})
    return webdriver.Remote(command_executor=f'http://{browser_ip}:4444/wd/hub', options=options)


driver = get_driver()
url = 'http://gcst.meteo.gov.ua/armua/sino/index.phtml'
data_html = f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html'

def post_gidro_telegrame_all(index):
    "Відправка post запиту телеграм по гідропостам  на сайт УкрГМЦ "
    try:
        driver.maximize_window()
        execute_cmd(driver, "Network.enable", {})
        load_dotenv()
        execute_cmd(driver, "Network.setExtraHTTPHeaders",
                    {"headers": get_auth_header(os.getenv('user'), os.getenv('password'))})
        time.sleep(0.2)
        driver.get(url)
        time.sleep(0.3)
        driver.implicitly_wait(time_to_wait=0.2)
        time.sleep(0.1)
        driver.find_element(by=By.CLASS_NAME, value='submenu'). \
            find_element(by=By.XPATH,
                         value='/html/body/table/tbody/tr/td[1]/a[10]').click()
        time.sleep(0.3)
        WebDriverWait(driver, 0.3).until(EC.presence_of_element_located((By.CLASS_NAME, "t1")))
        time.sleep(0.3)
        driver.find_element(by=By.CLASS_NAME, value='t1').send_keys(index)
        time.sleep(0.1)
        driver.implicitly_wait(time_to_wait=0.3)
        time.sleep(0.1)
        driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/form/table/' \
                                               'tbody/tr[2]/td[1]/table/tbody/tr[3]/td/font/input[1]').clear()
        driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/form/table/' \
                                               'tbody/tr[2]/td[1]/table/tbody/tr[3]/td/font/input[1]') \
            .send_keys('2')
        driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/'
                                               'form/table/tbody/tr[2]/td[1]/table'
                                               '/tbody/tr[3]/td/font/input[2]').clear()
        time.sleep(0.1)
        driver.find_element(by=By.XPATH,
                            value='/html/body/table/tbody/tr/td[2]/'
                                  'form/table/tbody/tr[2]/td[1]/'
                                  'table/tbody/tr[3]/td/font/input[2]') \
            .send_keys(datetime.date.today().strftime("%Y-%m-%d") + ' ' + '10:00:36')

        driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/'
                                               'form/table/tbody/tr[2]/td[1]/table'
                                               '/tbody/tr[3]/td/font/input[3]').clear()
        time.sleep(0.1)
        driver.find_element(by=By.XPATH,
                            value='/html/body/table/tbody/tr/td[2]/'
                                  'form/table/tbody/tr[2]/td[1]/'
                                  'table/tbody/tr[3]/td/font/input[3]') \
            .send_keys((datetime.datetime.today() + datetime.timedelta(days=-1)).strftime
                       ("%Y-%m-%d") + ' ' + '05:00:36')
        time.sleep(0.1)
        driver.find_element(by=By.XPATH,
                            value='/html/body/table/tbody/tr/td[2]/'
                                  'form/table/tbody/tr[1]/td/input[2]').click()
        time.sleep(0.1)
        file_object = open(data_html, "w", encoding=('koi8-u'))
        html = driver.page_source
        time.sleep(0.1)
        file_object.write(html)
        time.sleep(0.1)
        file_object.close()
        driver.close()
        print(f'save telegrame {datetime.date.today().strftime("%Y-%m-%d")}')
        time.sleep(1)
        driver.quit()
    except Exception as ex:
        print(ex)
        driver.quit()



def index_gidropost()->str:
    i = []
    file = '../gauges_telegrame1.db'
    for value in Database(filename=file, table='index_gauges'):
        i.append(value[0])
    index = ' '.join(i)
    return index


def main():
    post_gidro_telegrame_all(index_gidropost())



if __name__ == '__main__':
    main()
import datetime
import base64
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telegrame_save.request_index import request_index
from meteo_telegrame.request_index_meteo import request_index_meteo





chrome_options = Options()
chrome_options.headless = True
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver = webdriver.Chrome(service=service)


def get_auth_header(user, password):
    b64 = "Basic " + base64.b64encode('{}:{}'.format(user, password).encode('utf-8')).decode('utf-8')
    return {"Authorization": b64}

driver.execute_cdp_cmd("Network.enable", {})
load_dotenv()
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders",
                       {"headers": get_auth_header(os.getenv('user'), os.getenv("password"))})

def post_gidro_telegrame():
    driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')
    time.sleep(0.3)
    for value in request_index():
        index = value[0]

        time.sleep(0.2)
        driver.refresh()
        driver.implicitly_wait(time_to_wait=2.0)
        # print('1')
        # time.sleep(0.5)
        # print('2')
        # driver.find_element(by=By.CLASS_NAME, value='submenu').\
        #                         find_element(by=By.XPATH,
        #                         value='/html/body/table/tbody/tr/td[1]/a[10]').click()
        # time.sleep(1.5)
        # driver.implicitly_wait(time_to_wait=2.0)
        # print(f' read {index}')
        time.sleep(0.5)

        driver.find_element(by=By.CLASS_NAME, value='submenu'). \
                find_element(by=By.XPATH,
                             value='/html/body/table/tbody/tr/td[1]/a[10]').click()
        time.sleep(1.5)

        try:

            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, "t1")))
            driver.find_element(by=By.CLASS_NAME, value='t1').send_keys(index)


            # driver.find_element(by=By.CLASS_NAME, value='t1').send_keys(index)
            time.sleep(0.2)
            driver.implicitly_wait(time_to_wait=1.0)
            print(f' write {index}')
            time.sleep(0.2)
            driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/'
                                'form/table/tbody/tr[2]/td[1]/table'
                                '/tbody/tr[3]/td/font/input[2]').clear()
            time.sleep(0.2)
            driver.find_element(by=By.XPATH,
                                value='/html/body/table/tbody/tr/td[2]/'
                                   'form/table/tbody/tr[2]/td[1]/'
                                   'table/tbody/tr[3]/td/font/input[2]')\
                                .send_keys(datetime.date.today().strftime("%Y-%m-%d")+ ' ' + '09:00:36')
            time.sleep(0.2)
            driver.find_element(by=By.XPATH,
                                value='/html/body/table/tbody/tr/td[2]/'
                                      'form/table/tbody/tr[1]/td/input[2]').click()
            time.sleep(0.2)
            file_object = open(f'../telegrame_save/data_html/{index}.html', "w", encoding=('koi8-u'))
            html = driver.page_source
            time.sleep(0.2)
            file_object.write(html)
            time.sleep(0.1)
            file_object.close()
            print(f'save _____{index}____.html')
            # driver.refresh()
            print("__new index__")
            time.sleep(0.5)
        except:
            driver.refresh()
            time.sleep(0.2)
            print(f'not save {index}')
            driver.find_element(by=By.CLASS_NAME, value='submenu').find_element(by=By.XPATH,
                                value='/html/body/table/tbody/tr/td[1]/a[10]').click()
            time.sleep(1.5)

    driver.close()
    print(f'save telegrame {datetime.date.today().strftime("%Y-%m-%d")}')
    driver.quit()

def post_meteo_telegrame():
    driver.get('http://gcst.meteo.gov.ua/armua/sino/index.phtml')
    time.sleep(0.3)
    for value in request_index_meteo():
        index = value[0]
        time.sleep(0.2)
        driver.implicitly_wait(time_to_wait=2.0)
        time.sleep(0.5)

        driver.find_element(by=By.CLASS_NAME, value='submenu'). \
                find_element(by=By.XPATH,
                             value='/html/body/table/tbody/tr/td[1]/a[7]').click()
        time.sleep(1.5)

        try:
            driver.find_element(by=By.CLASS_NAME, value='t1').send_keys(index)
            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, "t1")))
            time.sleep(0.2)
            driver.implicitly_wait(time_to_wait=1.0)
            print(f' write {index}')
            time.sleep(0.2)
            driver.find_element(by=By.XPATH,
                                value='/html/body/table/tbody/tr/td[2]/'
                                      'form/table/tbody/tr[1]/td/input[2]').click()
            time.sleep(0.3)
            file_object = open(f'../meteo_telegrame/data_html/{index}.html', "w", encoding=('koi8-u'))
            html = driver.page_source
            time.sleep(0.2)
            file_object.write(html)
            time.sleep(0.1)
            file_object.close()
            print(f'save _____{index}____.html')
            driver.refresh()
            print("__new index__")
            time.sleep(0.5)
        except:
            driver.refresh()
            time.sleep(0.2)
            print(f'not save {index}')
            driver.find_element(by=By.CLASS_NAME, value='submenu').find_element(by=By.XPATH,
                                value='/html/body/table/tbody/tr/td[1]/a[7]').click()
            time.sleep(1.5)
    driver.close()
    print(f'save telegrame {datetime.date.today().strftime("%Y-%m-%d")}')
    driver.quit()





# post_gidro_telegrame()
# post_meteo_telegrame()
# print(post_meteo_telegrame())
post_gidro_telegrame()
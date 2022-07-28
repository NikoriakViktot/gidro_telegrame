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


class Driver():
    browser_ip = '212.26.138.5'
    options = webdriver.ChromeOptions()




    def __init__(self):
        self.options.set_capability('selenoid:options', {"enableVNC": True})
        self.driver = webdriver.Remote(command_executor=f'http://{self.browser_ip}:4444/wd/hub', options=self.options)



    def get_auth_header(self, user, password):
        b64 = "Basic " + base64.b64encode('{}:{}'.format(user, password).encode('utf-8')).decode('utf-8')
        return {"Authorization": b64}



    def execute_cmd(self, cmd, params):
        resource = f"/session/{self.driver.session_id}/chromium/send_command_and_get_result"
        url = self.driver.command_executor._url + resource
        body = json.dumps({'cmd': cmd, 'params': params})
        response = self.driver.command_executor._request('POST', url, body)
        return response.get('value')




class SeleniumGidro(Driver):
    url = 'http://gcst.meteo.gov.ua/armua/sino/index.phtml'
    date = datetime.date.today().strftime("%Y-%m-%d")
    data_html = f'../telegrame_save/data_html/{datetime.date.today().strftime("%Y-%m-%d")}.html'


    def __init__(self):

        super().__init__()
        self.driver.maximize_window()
        self.execute_cmd("Network.enable", {})
        load_dotenv()
        self.execute_cmd("Network.setExtraHTTPHeaders",
                    {"headers": self.get_auth_header(os.getenv('user'), os.getenv('password'))})



#

    def post_gidro_telegrame_all(self,index):


        "Відправка post запиту телеграм по гідропостам  на сайт УкрГМЦ "
        try:
            time.sleep(0.2)
            self.driver.get(self.url)
            time.sleep(0.3)
            self.driver.implicitly_wait(time_to_wait=0.2)
            time.sleep(0.1)
            self.driver.find_element(by=By.CLASS_NAME, value='submenu'). \
                find_element(by=By.XPATH,
                             value='/html/body/table/tbody/tr/td[1]/a[10]').click()
            time.sleep(0.3)
            WebDriverWait(self.driver, 0.3).until(EC.presence_of_element_located((By.CLASS_NAME, "t1")))
            time.sleep(0.3)
            self.driver.find_element(by=By.CLASS_NAME, value='t1').send_keys(index)
            time.sleep(0.1)
            self.driver.implicitly_wait(time_to_wait=0.3)
            time.sleep(0.1)
            self.driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/form/table/' \
                                                   'tbody/tr[2]/td[1]/table/tbody/tr[3]/td/font/input[1]').clear()
            self.driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/form/table/' \
                                                   'tbody/tr[2]/td[1]/table/tbody/tr[3]/td/font/input[1]') \
                .send_keys('2')
            self.driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/'
                                                   'form/table/tbody/tr[2]/td[1]/table'
                                                   '/tbody/tr[3]/td/font/input[2]').clear()
            time.sleep(0.1)
            self.driver.find_element(by=By.XPATH,
                                value='/html/body/table/tbody/tr/td[2]/'
                                      'form/table/tbody/tr[2]/td[1]/'
                                      'table/tbody/tr[3]/td/font/input[2]') \
                .send_keys(datetime.date.today().strftime("%Y-%m-%d") + ' ' + '10:00:36')

            self.driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/'
                                                   'form/table/tbody/tr[2]/td[1]/table'
                                                   '/tbody/tr[3]/td/font/input[3]').clear()
            time.sleep(0.1)
            self.driver.find_element(by=By.XPATH,
                                value='/html/body/table/tbody/tr/td[2]/'
                                      'form/table/tbody/tr[2]/td[1]/'
                                      'table/tbody/tr[3]/td/font/input[3]') \
                .send_keys((datetime.datetime.today() + datetime.timedelta(days=-1)).strftime
                           ("%Y-%m-%d") + ' ' + '05:00:36')
            time.sleep(0.1)
            self.driver.find_element(by=By.XPATH,
                                value='/html/body/table/tbody/tr/td[2]/'
                                      'form/table/tbody/tr[1]/td/input[2]').click()
            time.sleep(0.1)
            file_object = open(self.data_html, "w", encoding=('koi8-u'))
            html = self.driver.page_source
            time.sleep(0.1)
            file_object.write(html)
            time.sleep(0.1)
            file_object.close()
            self.driver.close()
            print(f'save telegrame {datetime.date.today().strftime("%Y-%m-%d")}')
            time.sleep(1)
            self.driver.quit()
        except Exception as ex:
            print(ex)
            self.driver.quit()



#
# if __name__ == '__main__':

    # def index_gidropost() -> str:
    #     i = []
    #     file = '../gauges_telegrame1.db'
    #     for value in Database(filename=file, table='index_gauges'):
    #         i.append(value[0])
    #     index = ' '.join(i)
    #     return index
    # SeleniumGidro().post_gidro_telegrame_all(index_gidropost())
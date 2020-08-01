import time
from builtins import enumerate
from selenium.webdriver.common.keys import Keys

icx_Oraclemport
#DB접속
from selenium import webdriver
connection = cx_Oracle.connect("c##oracle", "1", "113.131.219.170:40001/cdb1")
cursor = connection.cursor()

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": r"C:",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
driver = webdriver.Chrome(r'C:\Users\ckdwo\Desktop\hak\chromedriver_win32_83\chromedriver.exe', chrome_options=options)

time.sleep(3)

url = 'https://www.pharm114.or.kr/main.asp'
driver.get(url)

driver.find_element_by_xpath('//*[@id="continents"]/li[16]/a').click()

for iidx, dataa in enumerate(driver.find_elements_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/select[2]/option')):

    if iidx == 0:
        continue
    dataa.click()
    serch = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/input')
    serch.send_keys(Keys.CONTROL+"\n")
    driver.switch_to.window(driver.window_handles[1])
    for idx, data in enumerate(driver.find_elements_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table[3]/tbody/tr[4]/td/table/tbody/tr/td[3]/a')):

        # for idx, data in enumerate(driver.find_elements_by_xpath('//*[@id="printZone"]/table[2]/tbody/tr')):
        #     print(idx)
        first_tab = driver.window_handles[0]
        second_tab = driver.window_handles[1]
        #첫번째 페이지 크롤링
        data.send_keys(Keys.CONTROL+"\n")

        driver.switch_to.window(driver.window_handles[2])
        #두번째 이후 크롤링

        driver.close()

        driver.switch_to.window(window_name=second_tab)
        if idx == idx[:-1]:
            driver.close()
            driver.switch_to.window(window_name=first_tab)

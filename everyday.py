import time

import cx_Oracle
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

for a in range(1, 3000):
    print(a)
    data = int(a)
    # url= 'https://store.naver.com/restaurants/list?filterId=r08&page=%s'%data + '&query=%EB%B6%80%EC%82%B0%20%EB%A7%9B%EC%A7%91&sessionid=WNBtwEisB%2B%2B6Ez6%2BcydImg%3D%3D'
    # url =  'https://store.naver.com/restaurants/list?filterId=r08&menu=1&page=%s'%data + '&query=%EB%B6%80%EC%82%B0%20%EB%A7%9B%EC%A7%91&sessionid=bX487UrswXA3IqBwFsiBTg%3D%3D'
    url = 'https://map.naver.com/v5/search/%EB%B6%80%EC%82%B0%20%EC%95%BD%EA%B5%AD?c=14362488.9508990,4177405.4172987,14,0,0,0,dh'
    driver.get(url)

    for idx, data in enumerate(driver.find_elements_by_xpath('//*[@id="container"]/div[2]/div[1]/div/div[2]/ul/li')):

        intidx = int(idx) + 1
        storename = ""
        storephone = ""
        storeaddr = ""
        storeintroduce = ""
        try:
            selectname = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div[2]/ul/li[%s]/div/div/div[1]/span/a/span'%intidx)
        except:
            break

        print(selectname)

        selectname.click()

        driver.switch_to.window(driver.window_handles[1])
        try:
            storename = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/strong').text
            print(storename)
        except:
            driver.close()
            first_tab = driver.window_handles[0]
            driver.switch_to.window(window_name=first_tab)
            break
        try:
            storephone = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[1]/div').text
            print(storephone)
        except:
            driver.close()
            first_tab = driver.window_handles[0]
            driver.switch_to.window(window_name=first_tab)
            break
        try:
            storeaddr = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[2]/div/ul/li[1]/span').text
            print(storeaddr)
        except:
            driver.close()
            first_tab = driver.window_handles[0]
            driver.switch_to.window(window_name=first_tab)
            break
        try:
            storetype = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/span').text
            print(storetype)
        except:
            driver.close()
            first_tab = driver.window_handles[0]
            driver.switch_to.window(window_name=first_tab)
            break
        if(storetype=='카페,디저트'):
            storetype = 2
            print(storetype)
        else:
            storetype = 0
            print(storetype)
        try:
            sql = "INSERT INTO everyday" \
                  "(" \
                  "STORENAME, " \
                  "STOREPHONE, " \
                  "STOREADDR, " \
                  "STORETYPE)" \
                  "VALUES(" \
                  ":STORENAME, " \
                  ":STOREPHONE, " \
                  ":STOREADDR, " \
                  ":STORETYPE) "
            cursor.execute(sql, (storename, storephone, storeaddr, storetype))
        finally:
            connection.commit()

        driver.close()
        first_tab = driver.window_handles[0]
        driver.switch_to.window(window_name=first_tab)

        print(idx)

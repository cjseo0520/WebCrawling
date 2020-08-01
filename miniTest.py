import time

import cx_Oracle
#DB접속
from selenium import webdriver
connection = cx_Oracle.connect("scott", "tiger", "localhost:1521/xe")
cursor = connection.cursor()


options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": r"C:",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
driver = webdriver.Chrome(r'C:\Users\ckdwo\Desktop\hak\chromedriver_win32_83\chromedriver.exe', chrome_options=options)
# #귀검사
# driver.get('http://df.nexon.com/df/info/equipment/search?page=1&is_limit=&filter=100%2C400%2C204&max=100&min=100&level=Y&order_name=rarity&order_type=desc')
# #격투가
#driver.get('http://df.nexon.com/df/info/equipment/search?page=1&is_limit=&filter=100%2C401%2C204&max=100&min=100&level=Y&order_name=rarity&order_type=desc')
# #거너
#driver.get('http://df.nexon.com/df/info/equipment/search?page=1&is_limit=&filter=100%2C402%2C204&max=100&min=100&level=Y&order_name=rarity&order_type=desc')
# #마법사
#driver.get('http://df.nexon.com/df/info/equipment/search?page=1&is_limit=&filter=100%2C403%2C204&max=100&min=100&level=Y&order_name=rarity&order_type=desc')
# #프리스트
#driver.get('http://df.nexon.com/df/info/equipment/search?page=1&is_limit=&filter=100%2C404%2C204&max=100&min=100&level=Y&order_name=rarity&order_type=desc')
# #도적
#driver.get('http://df.nexon.com/df/info/equipment/search?page=1&is_limit=&filter=100%2C405%2C204&max=100&min=100&level=Y&order_name=rarity&order_type=desc')
# #마창사
#driver.get('http://df.nexon.com/df/info/equipment/search?page=1&is_limit=&filter=100%2C406%2C204&max=100&min=100&level=Y&order_name=rarity&order_type=desc')
# #총검사
driver.get('http://df.nexon.com/df/info/equipment/search?page=1&is_limit=&filter=100%2C407%2C204&max=100&min=100&level=Y&order_name=rarity&order_type=desc')


time.sleep(3)

driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div[4]/span[1]/a').click()

time.sleep(3)

sid = 0
itemname = ""
category = ""
img = ""
pattack = ""
mattack = ""
iattack = ""
pow = ""
intpow = ""
anti = ""
foption = ""
soption = ""
explanation = ""

for idx, data in enumerate(driver.find_elements_by_xpath('//*[@id="searchList"]/tr')):

    data.click()

    driver.switch_to.window(driver.window_handles[1])

    itemname = driver.find_element_by_xpath('//*[@id="equipmentList"]/div[1]/div[1]/div/div/dl/dt/a/span').get_attribute('innerText')
    print(itemname)
    item_slice = itemname.split('[')
    if (len(item_slice)) == 2:
        itemname_test1 = item_slice[1]
        itemname_test2 = itemname_test1.replace(']', '', -1)

        if itemname_test2 == '결투장':
            driver.close()
            first_tab = driver.window_handles[0]
            driver.switch_to.window(window_name=first_tab)
    else:
        category = driver.find_element_by_xpath('//*[@id="equipmentList"]/div[1]/div[1]/div/div/div/ul[1]/li[2]').get_attribute('innerHTML').split('<br>')
        category_name = category[2].strip()
        img = driver.find_element_by_xpath('//*[@id="equipmentList"]/div[1]/div[1]/div/div/dl/dt/a').get_attribute('innerHTML').split('"')
        img2 = img[1]
        totald = driver.find_element_by_xpath('//*[@id="equipmentList"]/div[1]/div[1]/div/div/div/ul[1]/li[1]/span').get_attribute('innerHTML').split('<br>')
        pattack = totald[0].strip()
        mattack = totald[1].strip()
        iattack = totald[2].strip()
        totalpi = driver.find_element_by_xpath('//*[@id="equipmentList"]/div[1]/div[1]/div/div/div/ul[2]/li').get_attribute('innerHTML').split('<br>')
        # for idx2, val in enumerate(totalpi):
        if (len(totalpi)) == 2:
            slice1 = totalpi[0].strip().split(" ")
            totalpi[1].strip().split(" ")
            if slice1[0] == '힘':
                pow = totalpi[0]
                anti = totalpi[1]
            elif slice1[0].strip() =='지능':
                intpow=totalpi[0]
                anti = totalpi[1]
        elif (len(totalpi)) == 3:
            slice1 = totalpi[0].strip()
            slice2 = totalpi[1].strip()
            totalpi[2].strip()

            pow = slice1
            intpow = slice2
            anti = totalpi[2]

        foption = driver.find_element_by_xpath('//*[@id="equipmentList"]/div[1]/div[1]/div/div/div/ul[3]/li').get_attribute('innerText')
        soption = driver.find_element_by_xpath('//*[@id="equipmentList"]/div[1]/div[1]/div/div/div/ul[4]/li').get_attribute('innerText')
        explanation = driver.find_element_by_xpath('//*[@id="equipmentList"]/div[1]/div[1]/div/div/div/ul[5]/li').get_attribute('innerText')
        try:
            sql = "INSERT INTO ITEM" \
                  "(" \
                  "ITEMNAME, " \
                  "CATEGORY, " \
                  "IMG, " \
                  "PATTACK, " \
                  "MATTACK," \
                  "IATTACK, " \
                  "POW, " \
                  "INTPOW," \
                  "ANTI, " \
                  "FOPTION, " \
                  "SOPTION, " \
                  "EXPLANATION)" \
                  "VALUES(" \
                  ":ITEMNAME, " \
                  ":CATEGORY, " \
                  ":IMG, " \
                  ":PATTACK, " \
                  ":MATTACK, " \
                  ":IATTACK, " \
                  ":POW, " \
                  ":INTPOW, " \
                  ":ANTI, " \
                  ":FOPTION, " \
                  ":SOPTION, " \
                  ":EXPLANATION)"
            cursor.execute(sql, (itemname, category_name, img2, pattack, mattack, iattack, pow, intpow, anti, foption, soption, explanation))
        finally:
            connection.commit()
        driver.close()
        first_tab = driver.window_handles[0]
        driver.switch_to.window(window_name=first_tab)
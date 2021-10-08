from time import sleep



def login():
    from selenium import webdriver
    from selenium.webdriver.android.webdriver import WebDriver
    import time
    from selenium.webdriver.support import expected_conditions as EC, wait
    from selenium.webdriver.support.ui import WebDriverWait
    import netflixdb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    web = webdriver.Safari()

    web.get("https://www.netflix.com/in/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse")

    time.sleep(3)

    mail = web.find_element_by_xpath('//*[@id="id_userLoginId"]')
    mail.send_keys(netflixdb.username)

    password = web.find_element_by_xpath('//*[@id="id_password"]')
    password.send_keys(netflixdb.decrypted)

    submit = web.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
    submit.click()


    time.sleep(6)

    try:
        element = WebDriverWait(web , 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[4]/div/a/div/div'))
        )
        element.click()
    except:
        web.quit()

    

    time.sleep(3)


def login():

    from selenium import webdriver
    from selenium.webdriver.android.webdriver import WebDriver
    import time
    from selenium.webdriver.support import expected_conditions as EC, wait
    from selenium.webdriver.support.ui import WebDriverWait
    import perfectelearningdb 
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys


    web = webdriver.Safari()

    web.get("https://perfectelearning.com/")

    time.sleep(3)

    # login = web.find_element_by_xpath('//*[@id="head-menu"]/div/div[3]/a[2]')
    # login.click()

    try:
        element = WebDriverWait(web , 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="head-menu"]/div/div[3]/a[2]'))
        )
        element.click()
    except:
        print("error")


    time.sleep(5)

    try:
        element = WebDriverWait(web , 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="SignInForm"]/div[1]/input'))
        )
        element.send_keys(perfectelearningdb.username)
    except:
        print("error")

    time.sleep(5)

    try:
        element = WebDriverWait(web , 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="lg_passowrd"]'))
        )
        element.send_keys(perfectelearningdb.decrypted)
    except:
        print("error")

    try:
        element = WebDriverWait(web , 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="SignInForm"]/button'))
        )
        element.click()
    except:
        print("error")


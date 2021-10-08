def login():
    from selenium import webdriver
    from selenium.webdriver.android.webdriver import WebDriver
    import time
    from selenium.webdriver.support import expected_conditions as EC, wait
    from selenium.webdriver.support.ui import WebDriverWait
    import jamboreedb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    web = webdriver.Safari()

    web.get("https://jamboree.online/auth")

    time.sleep(4)

    mail = web.find_element_by_xpath('/html/body/unc-app/unc-view/div/main/div[1]/unc-auth-login/form/input[1]')
    mail.send_keys(jamboreedb.username)

    password = web.find_element_by_xpath('/html/body/unc-app/unc-view/div/main/div[1]/unc-auth-login/form/input[2]')
    password.send_keys(jamboreedb.decrypted)

    submit = web.find_element_by_xpath('/html/body/unc-app/unc-view/div/main/div[1]/unc-auth-login/form/button')
    submit.click()

    


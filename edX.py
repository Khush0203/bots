def login():
    from selenium import webdriver
    from selenium.webdriver.android.webdriver import WebDriver
    import time
    from selenium.webdriver.support import expected_conditions as EC, wait
    from selenium.webdriver.support.ui import WebDriverWait
    import edXdb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    web = webdriver.Safari()

    web.get("https://authn.edx.org/login?next=%2Fdashboard")

    time.sleep(3)

    mail = web.find_element_by_xpath('//*[@id="emailOrUsername"]')
    mail.send_keys(edXdb.username)

    password = web.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(edXdb.decrypted)

    submit = web.find_element_by_xpath('//*[@id="main-content"]/div/form/button')
    submit.click()

    time.sleep(3)

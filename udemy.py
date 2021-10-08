def login():

    from selenium import webdriver
    from selenium.webdriver.android.webdriver import WebDriver
    import time
    from selenium.webdriver.support import expected_conditions as EC, wait
    from selenium.webdriver.support.ui import WebDriverWait
    import udemydb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    web = webdriver.Safari()

    web.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")

    time.sleep(5)

    email = web.find_element_by_xpath('//*[@id="email--1"]')
    email.send_keys(udemydb.username)

    time.sleep(3)
    password = web.find_element_by_xpath('//*[@id="id_password"]')
    password.send_keys(udemydb.decrypted)

    login = web.find_element_by_xpath('//*[@id="submit-id-submit"]')
    login.click()

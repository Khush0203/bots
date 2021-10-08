def login():
    from selenium import webdriver
    from selenium.webdriver.android.webdriver import WebDriver
    import time
    from selenium.webdriver.support import expected_conditions as EC, wait
    from selenium.webdriver.support.ui import WebDriverWait
    import linkedindb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    web = webdriver.Safari()
    web.get("https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fin%2Elinkedin%2Ecom%2Fin%2Fkhush-munshi-794b76211&fromSignIn=true&trk=public_profile_nav-header-signin")

    time.sleep(3)

    email = web.find_element_by_xpath('//*[@id="username"]')
    email.send_keys(linkedindb.username)

    time.sleep(1)
    password = web.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(linkedindb.decrypted)


    submit = web.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
    submit.click()

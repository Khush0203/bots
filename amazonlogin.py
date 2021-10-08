def login(searchitem):

    from selenium import webdriver
    from selenium.webdriver.android.webdriver import WebDriver
    import time
    from selenium.webdriver.support import expected_conditions as EC, wait
    from selenium.webdriver.support.ui import WebDriverWait
    import amazonlogindb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import pyttsx3

    engine = pyttsx3.init()


    # Question
    # searchitem = input("What do you want to search in amazon:  ")
    # print()
    # print()

    #opening server
    web = webdriver.Safari()
    web.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    #username
    email =  web.find_element_by_xpath('//*[@id="ap_email"]')
    email.send_keys(amazonlogindb.username)

    #username submit
    email_submit = web.find_element_by_xpath('//*[@id="continue"]')
    email_submit.click()


    time.sleep(3)

    #password 
    pasword = web.find_element_by_xpath('//*[@id="ap_password"]')
    pasword.send_keys(amazonlogindb.decrypted)

    #password submit
    password_submit = web.find_element_by_xpath('//*[@id="signInSubmit"]')
    password_submit.click()

    time.sleep(5)

    #search
    search = web.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    search.send_keys(searchitem)

    time.sleep(2)

    #search submit
    button = web.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
    button.click()


    engine.say('Done')
    engine.runAndWait



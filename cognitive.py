def login():
    
    from selenium import webdriver
    from selenium.webdriver.android.webdriver import WebDriver
    import time
    from selenium.webdriver.support import expected_conditions as EC, wait
    from selenium.webdriver.support.ui import WebDriverWait
    import cognitivedb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys


    web = webdriver.Safari()

    web.get("https://courses.cognitiveclass.ai/login?next=/oauth2/authorize%3Fclient_id%3DXCTzu9NHWn%26redirect_uri%3Dhttps%253A%252F%252Fcognitiveclass.ai%252Fauth%252Fopen_edx%252Fcallback%26response_type%3Dcode%26scope%3Duser_id%2Bprofile%2Bemail%26state%3Df64609e78a84ec16f1409c783d87258f02d66bf38e457ead")

    time.sleep(3) 

    mail = web.find_element_by_xpath('//*[@id="login-email"]')
    mail.send_keys(cognitivedb.username)

    password = web.find_element_by_xpath('//*[@id="login-password"]')
    password.send_keys(cognitivedb.decrypted)

    submit = web.find_element_by_xpath('//*[@id="login"]/button')
    submit.click()


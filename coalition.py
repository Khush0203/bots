def login():
    from selenium import webdriver
    from selenium.webdriver.android.webdriver import WebDriver
    import time
    from selenium.webdriver.support import expected_conditions as EC, wait
    from selenium.webdriver.support.ui import WebDriverWait
    import coalitiondb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys


    web = webdriver.Safari()

    web.get("https://shibboleth-idp.collegenet.com/idp/profile/SAML2/Redirect/SSO?SAMLRequest=fZJBU8IwFIT%2FSid3mrZYaDOUGYSDzKAwtHrw4qTpEzKmSc1LRf%2B9haLihVsm%2BbL7dpMJ8lo1bNa6vd7CewvovM9aaWSng4y0VjPDUSLTvAZkTrB8dr9ikR%2BwxhpnhFHEmyGCddLoudHY1mBzsB9SwON2lZG9cw0ySg%2BHg19%2FCcOVPKK%2BsTu6e6P5XpalUeD2PqKhR%2FWIbtZ5QbxFN47U%2FEj%2FyeAvP5BV43f%2BCnagwXXLmnZbtJvrVSo4S22hkhaEo3m%2BJt5ykZGXMr4ZxZAIMarKMhwmIk15NBpHVVwO0zhNOgyxhaVGx7XLSBRE4SAMBkFSBGMWRmwYPRNvc45%2FK3Ul9e56V2UPIbsris2gj%2FcEFk%2FROoBMJ8fG2cnYXrzBdVn%2BUzyZXqv5ojNs6IReWPW%2BDXvotJeLjVFSfHkzpcxhboE7yEhI6LS%2F8v%2BjTL8B&RelayState=https%3A%2F%2Fwww.mycoalition.org%2Fgk")

    web.refresh()
    time.sleep(4)

    mail = web.find_element_by_xpath('//*[@id="j_username"]')
    mail.send_keys(coalitiondb.username)

    password = web.find_element_by_xpath('//*[@id="j_password"]')
    password.send_keys(coalitiondb.decrypted)

    submit = web.find_element_by_xpath('/html/body/div/div[2]/div/div/main/div/div[2]/div/div[2]/form/div[3]/button')
    submit.click()

    # web.refresh()

    time.sleep(15)

login()
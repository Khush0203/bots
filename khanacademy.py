def login():
    from selenium import webdriver
    from selenium.webdriver.android.webdriver import WebDriver
    import time
    from selenium.webdriver.support import expected_conditions as EC, wait
    from selenium.webdriver.support.ui import WebDriverWait
    import khanacademydb
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    web = webdriver.Safari()

    web.get("https://www.khanacademy.org/login?continue=https%3A//www.khanacademy.org/mission/sat/exams")

    searchbox = web.find_element_by_xpath('//*[@id="identifier-field"]')
    searchbox.send_keys(khanacademydb.username)


    searchbox1 = web.find_element_by_xpath('//*[@id="uid-labeled-text-field-0-wb-id-field"]')
    searchbox1.send_keys(khanacademydb.decrypted)

    searchbutton = web.find_element_by_xpath('//*[@id="app-shell-root"]/div/div[3]/div/div[3]/section[2]/div/div/form/button')
    searchbutton.click()


    try:
        element = WebDriverWait(web , 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Practice'))
        )
        element.click()
    except:
        web.quit()

    time.sleep(10)





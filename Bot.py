from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
import time

def main():

    NAME = "My beautiful Name"  # Change this

    NICK = "My beautiful User Name"  # Change this

    PWD = "1234 is a bad password"  # Change this

    browser  = webdriver.Chrome(ChromeDriverManager().install())

    browser.get('https://www.instagram.com/')

    time.sleep(3)
    try:
        browser.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
    except:
        pass

    def register():
        try:
            try:
                browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/a/span').click()
            except:
                browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[2]/div/p/a/span').click()
        except:
            register()

    register()

    drive  = webdriver.Chrome(ChromeDriverManager().install())

    drive.get('https://email-fake.com')

    def copy():
        try:
            drive.find_element_by_xpath('//*[@id="copbtn"]').click()
        except:
            copy()

    copy()

    browser.find_element_by_name("emailOrPhone").send_keys(Keys.CONTROL, "v")
    browser.find_element_by_name("fullName").send_keys(NAME)
    browser.find_element_by_name("username").send_keys(NICK)
    browser.find_element_by_name("password").send_keys(PWD)

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[7]/div/button').click()

    time.sleep(1)

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select').click()

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[19]').click()

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select').click()

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[6]').click()

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select').click()

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[10]').click()

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button').click()

    def temp():
        global code
        try:
            code = drive.find_element_by_xpath('//*[@id="email_content"]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]').text
        except:
            time.sleep(1)
            drive.refresh()
            temp()

    temp()

    browser.find_element_by_name("email_confirmation_code").send_keys(code)

    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button').click()

if __name__ == '__main__':
    main()
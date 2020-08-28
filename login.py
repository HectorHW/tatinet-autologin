from selenium.common.exceptions import NoSuchElementException

from utils import read_credentials
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from config import GECKOPATH, CREDENTIALS_PATH

if __name__ == '__main__':
    login, passw = read_credentials(CREDENTIALS_PATH)

    options = Options()
    options.headless = True


    with webdriver.Firefox(executable_path=GECKOPATH, options=options) as driver:
        print("started headless firefox")
        driver.get("http://wifi.tatinet.ru")
        try:
            elem = driver.find_element_by_link_text("Разорвать соединение")
            print("found element `Разорвать соединение`, we are connected")
            elem.click()
            print("pressed disconnect")
            print("broke existing connection")
            driver.get("http://wifi.tatinet.ru")

        except NoSuchElementException as e:
            print("could not find `Разорвать соединение`, assume we are not logged in")

        print("connection should be broken by now")

        login_fields= driver.find_elements_by_xpath("//input[@name='username']")
        pass_fields = driver.find_elements_by_xpath("//input[@name='password']")

        login_button = driver.find_element_by_xpath("//input[@value=\"Вход\"]")

        login_field = login_fields[1]
        pass_field = pass_fields[1]
        login_field.send_keys(login)
        pass_field.send_keys(passw)
        print("typed in login info")
        login_button.click()
        print("clicked `login`")

print("browser terminated")

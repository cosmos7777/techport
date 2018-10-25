import unittest
from selenium import webdriver
# test47 Проверка входа логина и пароля личного кабинета, Отрицательный сценарий, не заполнено поле пароля
class LoginTest(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)




    def test_user_login3(self):
        # Отрицательный сценарий, не заполнено поле пароля
        driver = self.driver
        driver.get("https://test1.techport.ru/login")
        # Загружаем страницу, вводим логин и нажимаем войти
        login_field = driver.find_element_by_id("login_static")
        login_field.send_keys("cosmos7777@zdenka.net")
        button_login = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button")
        button_login.click()
        # проверяем слово "пароль" в ошибке
        user_mail = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[1]/div[2]")
        assert "пароль" in user_mail.text







    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()




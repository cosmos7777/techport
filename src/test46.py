import unittest
from selenium import webdriver
# test46 Проверка входа логина и пароля личного кабинета, Отрицательный сценарий, не заполнено поле логина
class LoginTest(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)




    def test_user_login2(self):
        # Отрицательный сценарий, не заполнено поле логина
        driver = self.driver
        driver.get("https://test1.techport.ru/login")
        # Загружаем страницу, вводим пароль и нажимаем войти
        password_field = driver.find_element_by_id("password_static")
        password_field.send_keys("abc1234")
        button_login = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button")
        button_login.click()
        # проверяем слово "e-mail" в ошибкеа
        user_mail = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[1]/div/div[2]")
        assert "e-mail" in user_mail.text







    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()




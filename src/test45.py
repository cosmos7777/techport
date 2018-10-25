import unittest
from selenium import webdriver
# test45 Проверка входа логина и пароля личного кабинета, Отрицательный сценарий, на заполнено оба поля
class LoginTest(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_user_login1(self):
        # Отрицательный сценарий, на заполнено оба поля
        driver = self.driver
        driver.get("https://test1.techport.ru/login")
        # Загружаем страницу и нажимаем войти
        button_login = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button")
        button_login.click()
        # проверяем слово "e-mail" в ошибке
        user_mail = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[1]/div/div[2]")
        assert "e-mail" in user_mail.text






    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()




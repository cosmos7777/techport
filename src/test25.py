import unittest
from selenium import webdriver
#  test25 Проверка регистрации нового пользователя, Отрицательный сценарий, не заполнено поле логин
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://test1.techport.ru/registration")

    def test(self):
        driver = self.driver

        # Отрицательный сценарий, не заполнено поле логин

        # Вводим только пароль
        password_field = driver.find_element_by_id("password_register_static")
        password_field.send_keys("abc1234")
        # нажимаем Зарегистрироваться
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button").click()
        # проверяем в поле логина ошибку "Это поле обязательно!"
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[1]/div/div[2]")
        assert "Это поле обязательно!" in cosmos.text







        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
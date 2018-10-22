import unittest
from selenium import webdriver
#  test23 Проверка регистрации нового пользователя, Положительный сценарий, заполнено оба поля
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://test1.techport.ru/registration")

    def test(self):
        driver = self.driver

        # Положительный сценарий, заполнено оба поля

        # Заполняем поле логина и пароля
        login_field = driver.find_element_by_id("login_registration_static")
        login_field.send_keys("cosmos7777@zdenka.net")
        password_field = driver.find_element_by_id("password_register_static")
        password_field.send_keys("abc1234")
        # нажимаем Зарегистрироваться
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button").click()
        # в следующем окне проверяем заголовок "Подтверждение регистрации"
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div")
        assert "Подтверждение регистрации" in cosmos.text







        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
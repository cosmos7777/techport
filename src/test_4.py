import unittest
from selenium import webdriver
# Проверка регистрация нового пользователя на сайта
class LoginTest(unittest.TestCase):
    def setUp(self):
      self.driver = webdriver.Firefox(executable_path='/geckodriver')
      #self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)

        # Положительный сценарий, заполнено оба поля
    def test_registration1(self):
        driver = self.driver
        driver.get("https://test1.techport.ru/registration")
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



     # Отрицательный сценарий, не заполнено два поля
    def test_registration2(self):
        driver = self.driver
        driver.get("https://test1.techport.ru/registration")
        # ничего не вводим, нажимаем Зарегистрироваться
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button").click()
        # проверяем в поле логина ошибку "Это поле обязательно!"
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[1]/div/div[2]")
        assert "Это поле обязательно!" in cosmos.text
        # проверяем в поле пароля ошибку "Это поле обязательно!"
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[1]/div[2]")
        assert "Это поле обязательно!" in cosmos.text

    # Отрицательный сценарий, не заполнено поле логин
    def test_registration3(self):
        driver = self.driver
        driver.get("https://test1.techport.ru/registration")
        # Вводим только пароль
        password_field = driver.find_element_by_id("password_register_static")
        password_field.send_keys("abc1234")
        # нажимаем Зарегистрироваться
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button").click()
        # проверяем в поле логина ошибку "Это поле обязательно!"
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[1]/div/div[2]")
        assert "Это поле обязательно!" in cosmos.text

        # Отрицательный сценарий, не заполнено поле пароль
    def test_registration4(self):
        driver = self.driver
        driver.get("https://test1.techport.ru/registration")
        # водим только логин
        login_field = driver.find_element_by_id("login_registration_static")
        login_field.send_keys("cosmos7777@zdenka.net")
        # нажимаем Зарегистрироваться
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button").click()
        # проверяем в поле пароля ошибку "Это поле обязательно!"
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[1]/div[2]")
        assert "Это поле обязательно!" in cosmos.text

        # Проверка отображения скрытого пароля
    def test_registration5(self):
        driver = self.driver
        driver.get("https://test1.techport.ru/registration")
        # Вводим пароль
        password_field = driver.find_element_by_id("password_register_static")
        password_field.send_keys("abc1234")
        # нажимаем в поле пароля кнопку "показать"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[1]/button").click()
        driver.find_element_by_id("password_register_static").is_displayed()



    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234

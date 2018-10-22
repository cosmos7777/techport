import unittest
from selenium import webdriver
# Проверка формы восстановления пароля
class LoginTest(unittest.TestCase):
    def setUp(self):
      self.driver = webdriver.Firefox(executable_path='/geckodriver')
      #self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)

      # Отрицательный сценарий, не заполнено два поля
    def test2(self):
        driver = self.driver
        driver.get("https://test1.techport.ru/login")
        # Нажимаем "Восстановить пароль"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[2]/a").click()
        # Оставляем пустые поле логина и пароля,
        login_field = driver.find_element_by_id("login_recovery")
        login_field.send_keys("")
        password_field = driver.find_element_by_id("password_recovery")
        password_field.send_keys("")
        # нажимаем "Восстановить пароль
        driver.find_element_by_xpath("/html/body/div[2]/noindex/div/div[9]/div/div[1]/form/div[3]/a[1]/button").click()
        # проверяем в поле логина ошибку "Это поле обязательно!"
        driver.find_element_by_xpath("/html/body/div[2]/noindex/div/div[9]/div/div[1]/form/div[1]/div/div[2]").is_displayed()
        # проверяем в поле пароля ошибку "Это поле обязательно!"
        driver.find_element_by_xpath("/html/body/div[2]/noindex/div/div[9]/div/div[1]/form/div[2]/div[1]/div[2]").is_displayed()


        # Отрицательный сценарий, не заполнено поле логина
    def test3(self):
        driver = self.driver
        driver.get("https://test1.techport.ru/login")
        # Нажимаем "Восстановить пароль"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[2]/a").click()
        # Оставляем пустым поле логина
        login_field = driver.find_element_by_id("login_recovery")
        login_field.send_keys("")
        password_field = driver.find_element_by_id("password_recovery")
        password_field.send_keys("abc1234")
        # нажимаем "Восстановить пароль
        driver.find_element_by_xpath("/html/body/div[2]/noindex/div/div[9]/div/div[1]/form/div[3]/a[1]/button").click()
        # проверяем в поле логина ошибку "Это поле обязательно!"
        driver.find_element_by_xpath("/html/body/div[2]/noindex/div/div[9]/div/div[1]/form/div[1]/div/div[2]").is_displayed()

        # Отрицательный сценарий, не заполнено поле пароля
    def test4(self):
        driver = self.driver
        driver.get("https://test1.techport.ru/login")
        # Нажимаем "Восстановить пароль"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[2]/a").click()
        # Оставляем пустым поле пароля,
        login_field = driver.find_element_by_id("login_recovery")
        login_field.send_keys("cosmos7777@zdenka.net")
        password_field = driver.find_element_by_id("password_recovery")
        password_field.send_keys("")
        # нажимаем "Восстановить пароль
        driver.find_element_by_xpath("/html/body/div[2]/noindex/div/div[9]/div/div[1]/form/div[3]/a[1]/button").click()
        # проверяем в поле пароля ошибку "Это поле обязательно!"
        driver.find_element_by_xpath("/html/body/div[2]/noindex/div/div[9]/div/div[1]/form/div[2]/div[1]/div[2]").is_displayed()

        # Положительный сценарий, заполнено оба поля
    def test5(self):
        driver = self.driver
        driver.get("https://test1.techport.ru/login")
        # Нажимаем "Восстановить пароль"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[2]/a").click()
        # Заполняем поле логина и пароля
        login_field = driver.find_element_by_id("login_recovery")
        login_field.send_keys("cosmos7777@zdenka.net")
        password_field = driver.find_element_by_id("password_recovery")
        password_field.send_keys("abc1234")
        # нажимаем "Восстановить пароль"
        driver.find_element_by_xpath("/html/body/div[2]/noindex/div/div[9]/div/div[1]/form/div[3]/a[1]/button").click()
        # в следующем окне появилось форма ввода кода из e-mail
        driver.find_element_by_class_name("tcp-input-control__input").is_displayed()



    def test1(self):
        driver = self.driver
        driver.get("https://test1.techport.ru/login")
        # Нажимаем "Восстановить пароль"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[2]/a").click()
        # Нажимаем на "Положением о персональных данных и конфиденциальности"
        driver.find_element_by_link_text("Положением о персональных данных и конфиденциальности.").click()
        # Появляется текст с содержанием "Techport.ru"
        cosmos = driver.find_element_by_id("pp_modal_wrap")
        assert "Techport.ru" in cosmos.text



    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234

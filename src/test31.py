import unittest
from selenium import webdriver
# test31 Проверка формы восстановления пароля, Положительный сценарий, заполнено оба поля
class LoginTest(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)



        # Положительный сценарий, заполнено оба поля
    def test(self):
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







    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
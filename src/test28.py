import unittest
from selenium import webdriver
# test 28 Проверка формы восстановления пароля, Отрицательный сценарий, не заполнено два поля
class LoginTest(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)

    # Отрицательный сценарий, не заполнено два поля
    def test(self):
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



    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
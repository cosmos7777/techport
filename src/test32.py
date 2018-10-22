import unittest
from selenium import webdriver
# test32 Проверка формы восстановления пароля, Проверка Положения о персональных данных и конфиденциальности, отображается и кликабельна
class LoginTest(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)



    # Проверка Положения о персональных данных и конфиденциальности, отображается и кликабельна

    def test1(self):
        driver = self.driver
        driver.get("https://test1.techport.ru/login")
        # Нажимаем "Восстановить пароль"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[2]/a").click()
        # Нажимаем на "Положением о персональных данных и конфиденциальности"
        driver.find_element_by_link_text("Положением о персональных данных и конфиденциальности.").is_displayed()
        driver.find_element_by_link_text("Положением о персональных данных и конфиденциальности.").is_enabled()




    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
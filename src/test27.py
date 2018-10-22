import unittest
from selenium import webdriver
#  test27 Проверка регистрации нового пользователя, Проверка отображения скрытого пароля
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://test1.techport.ru/registration")

    def test(self):
        driver = self.driver

        # Проверка отображения скрытого пароля

        # Вводим пароль
        password_field = driver.find_element_by_id("password_register_static")
        password_field.send_keys("abc1234")
        # нажимаем в поле пароля кнопку "показать"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[1]/button").click()
        driver.find_element_by_id("password_register_static").is_displayed()







        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
import unittest
from selenium import webdriver
# Проверка формы восстановления пароля
class testbuy(unittest.TestCase):
    def setUp(self):
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)

    def test1(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        # Нажимаем купить в 1 клик
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[6]/div/div/ul/li[1]/a/span[2]").click()
        # Заголовок "Купить в 1 клик" отображается
        driver.find_element_by_xpath("/html/body/div[2]/noindex/div/div[4]/div/div[1]/div/div/div/h1").is_displayed()


    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

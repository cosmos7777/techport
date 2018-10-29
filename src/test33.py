import unittest
from selenium import webdriver
# test33 Проверка покупки товара, покупка в 1 клик
class LoginTest(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(30)
      self.driver.set_page_load_timeout(45)




    # Покупка в 1 клик

    def test1(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        # Нажимаем купить в 1 клик



        #driver.find_element_by_link_text("Купить в 1 клик").click()
        driver.find_element_by_class_name("tcp-list-group__icon").click()




        # Заголовок "Купить в 1 клик" отображается
        driver.find_element_by_id("icon-modal-content").is_displayed()






    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
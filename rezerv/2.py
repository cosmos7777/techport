import unittest
from selenium import webdriver
# test33 Проверка покупки товара, покупка товара в окне товара
class LoginTest(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)





    def test1(self):
        driver = self.driver


        driver.get("http://test1.techport.ru/katalog/products/holodilniki")
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[3]/div[3]/div[1]/div[1]/div[3]/div[1]/a[1]/span").click()


        element = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[1]/div/div/div[3]/div/h1").text
        driver.find_element_by_id("desktop_search_input").send_keys(element)





        driver.find_element_by_id("desktop_search_submit").click()
        driver.find_element_by_id("3t5345")



    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
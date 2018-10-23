import unittest
from selenium import webdriver
# test36 Страница продукта - проверка элементов на странице, отображение мили аэрофлота,элемент "?".
class Test(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)



    # Фото товара, клик вниз, вверх

    def test1(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        # отображение мили аэрофлота
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]").is_displayed()
        # Элемент "?" кликабелен
        driver.find_element_by_css_selector(".aeroflot-miles_tip-ctrl > svg:nth-child(1)").is_enabled()
        driver.find_element_by_css_selector(".aeroflot-miles_tip-ctrl > svg:nth-child(1)").is_displayed()




    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
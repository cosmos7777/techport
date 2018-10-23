import unittest
from selenium import webdriver
# test35 Страница продукта - проверка элементов на странице, фото товара,сбоку клик вниз, вверх,  отображение, фукционирование
class Test(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)



    # Фото товара, клик вниз, вверх

    def test(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        # Клик вниз у формы фотографии
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/a").click()
        # Клик вверх у формы фотографии
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a").click()
        # Элемент главной фотографии отображается и работает
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[1]").is_displayed()



    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
import unittest
from selenium import webdriver
# test38 Страница продукта - проверка элементов кол-во штук товара, проверка кнопки "все характеристики".
class Test(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)



    # Проверка кнопки "все характеристики"

    def test(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[13]/td/a").click()
        driver.find_element_by_link_text("Все характеристики").click()

        cos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/table/tbody/tr[1]/td[1]")
        assert 'Общий полезный объем' in cos.text






    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
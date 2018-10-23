import unittest
from selenium import webdriver


# test39 Страница продукта - проверка элементов кол-во штук товара, Клик на похожие, сопутсвующие товары
class Test(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # Клик на похожие, сопутсвующие товары

    def test1(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[2]/form/div/div[1]/div/div[3]/button").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[2]/form/div/div[1]/div/div[1]/button").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]").is_enabled()




    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# cosmos7777@zdenka.net abc1234
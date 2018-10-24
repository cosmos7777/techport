import unittest
from selenium import webdriver


# test40 Страница продукта - проверка формы видео
class Test(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # проверка формы видео

    def test1(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/p[16]/iframe").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/p[16]/iframe").is_displayed()





    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# cosmos7777@zdenka.net abc1234
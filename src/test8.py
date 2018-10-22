import unittest
from selenium import webdriver
# Наличие header и footer элементов проверяется при загрузке "Главная страница"
# test8 Элемент "Ссылка на Twitter" отображается на странице и кликабелен
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Элемент "Ссылка на Twitter" отображается на странице и кликабелен
        tw = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[4]/div")
        self.assertTrue(tw.is_displayed()and tw.is_enabled())

        #cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[4]/div")
        assert 'Twitter' in tw.text

        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
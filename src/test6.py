import unittest
from selenium import webdriver
# Наличие header и footer элементов проверяется при загрузке "Главная страница"
# test6 Элемент "Ссылка на Одноклассники" отображается на странице и кликабелен
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Элемент "Ссылка на Одноклассники" отображается на странице и кликабелен
        ok = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[2]/div")
        self.assertTrue(ok.is_displayed()and ok.is_enabled())


        #cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[2]/div")
        assert 'Одноклассники' in ok.text

        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
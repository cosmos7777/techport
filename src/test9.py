import unittest
from selenium import webdriver
# Наличие header и footer элементов проверяется при загрузке "Главная страница"
# test9 Элемент "Ссылка на Instagram" отображается на странице и кликабелен
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Элемент "Ссылка на Instagram" отображается на странице и кликабелен
        ig = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[5]/div")
        self.assertTrue(ig.is_displayed()and ig.is_enabled())


        # cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[5]/div")
        assert 'Instagram' in ig.text

        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
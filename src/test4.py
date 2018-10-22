import unittest
from selenium import webdriver
# Наличие header и footer элементов проверяется при загрузке "Главная страница"
# test4 Элемент "Поле поиска" отображается на странице
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Элемент "Поле поиска" отображается на странице.
        #search = driver.find_element_by_xpath("//*[@id='desktop_search_input']")
        #self.assertTrue(search.is_displayed()and search.is_enabled())

        driver.find_element_by_xpath("//*[@id='desktop_search_input']").is_displayed()

        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
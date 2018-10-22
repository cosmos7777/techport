import unittest
from selenium import webdriver
# Наличие header и footer элементов проверяется при загрузке "Главная страница"
# test3 Элемент "Телефон города" содержит внутренний текст "8(495)228-66-69"
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Элемент "Телефон города" содержит внутренний текст "8(495)228-66-69"
        cosmos = driver.find_element_by_class_name("header_phones")
        assert '8 (495) 228-66-69' in cosmos.text

        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
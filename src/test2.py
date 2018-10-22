import unittest
from selenium import webdriver
# Наличие header и footer элементов проверяется при загрузке "Главная страница"
# test2 Проверка элементов верхнего уровня Город, Акции, Дисконт, Техбону и т.д. отборажаются
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Проверка элементов верхнего уровня Город, Акции, Дисконт, Техбону и т.д. отборажаются
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[2]/div/div").is_displayed()

        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
import unittest
from selenium import webdriver
# Проверка работы блоков на главной странице
# test12 Отзывы наших покупателей - скролл вправо,влево и заголовок "Отзывы наших покупателей" отображается на странице
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Отзывы наших покупателей - скролл вправо,влево и заголовок "Отзывы наших покупателей" отображается на странице
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[5]/div/div[1]/div[1]/div/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[5]/div/div[1]/div[1]/div/div[1]").click()
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[5]/div/div[1]/div[2]")
        assert 'Отзывы наших покупателей' in cosmos.text





        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
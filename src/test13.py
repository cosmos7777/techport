import unittest
from selenium import webdriver
# Проверка работы блоков на главной странице
# test13 Бренды -  скролл вправо,влево. И заголовок "Бренды " отображается на странице
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Бренды -  скролл вправо,влево. И заголовок "Бренды " отображается на странице
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[6]/div/div[1]/div[1]/div/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[6]/div/div[1]/div[1]/div/div[1]").click()
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[6]/div/div[1]/div[2]")
        assert 'Бренды' in cosmos.text





        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
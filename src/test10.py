import unittest
from selenium import webdriver
# Проверка работы блоков на главной странице
# test10 Большой слайдер с акциями-скролл вправо,влево, и отображение баннера на странице
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Большой слайдер с акциями-скролл вправо,влево, и отображение баннера на странице
        driver.find_element_by_xpath("//*[@id='banner-next']").click()
        driver.find_element_by_xpath("//*[@id='banner-prev']").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[1]/div/div/div[1]/div/div[1]/div/div/div[4]/a/img").is_displayed()





        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
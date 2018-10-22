import unittest
from selenium import webdriver
# Проверка работы блоков на главной странице
# test15 Кликаем в блоке новостей на кнопку "Хочу подписаться", и поле ввода e-mail появляется
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Кликаем в блоке новостей на кнопку "Хочу подписаться", и поле ввода e-mail появляется
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[8]/div/div/div[3]/button").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[8]/div/div/form/div/div/div[1]/div[1]/div/div/input").is_displayed()





        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
import unittest
from selenium import webdriver
# Наличие header и footer элементов проверяется при загрузке "Главная страница"
# test5 Элемент "Ссылка на ВКонтакте" отображается на странице и кликабелен
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Элемент "Ссылка на ВКонтакте" отображается на странице и кликабелен
        vk = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[1]/div")
        self.assertTrue(vk.is_displayed()and vk.is_enabled())

        #cosmos1 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[1]/div")
        assert 'Вконтакте' in vk.text

        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
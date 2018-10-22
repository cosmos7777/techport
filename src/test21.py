import unittest
from selenium import webdriver
#  Проверка выпадающего меню "Все категории" и производителей сайта
# test21 Проверка выпадаюдего меню, раздел "Спорт, отдых и хобби", Поставщик Nike, Torres отображаются и кликабельны
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver

        # Выполнено нажатие на кнопку "Все категории", и присутствует заголовок "ВСЕ КАТЕГОРИИ"
        driver.find_element_by_id("menu-button").click()
        cosmos = driver.find_element_by_id("menu-button")
        assert 'ВСЕ КАТЕГОРИИ' in cosmos.text

        # Проверка выпадаюдего меню, раздел "Спорт, отдых и хобби", Поставщик Nike, Torres отображаются и кликабельны
        driver.find_element_by_class_name("nike_button").is_displayed()
        driver.find_element_by_class_name("torres_button").is_displayed()
        driver.find_element_by_class_name("nike_button").is_enabled()
        driver.find_element_by_class_name("torres_button").is_enabled()





        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
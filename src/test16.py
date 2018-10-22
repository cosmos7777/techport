import unittest
from selenium import webdriver
#  Проверка выпадающего меню "Все категории" и производителей сайта
# test16 Выполнено нажатие на кнопку "Все категории", и проверено все меню выпадающего списка
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

        # Выполнено нажатие на кнопку "Все категории", и проверено все меню выпадающего списка
        driver.find_element_by_id("category-wrapper").click()
        cosmos = driver.find_element_by_id("category-wrapper")
        assert 'Бытовая техника' in cosmos.text
        assert 'Электроника' in cosmos.text
        assert 'Сантехника' in cosmos.text
        assert 'Мебель' in cosmos.text
        assert 'Инструменты' in cosmos.text
        assert 'Товары для дома' in cosmos.text
        assert 'Детские товары' in cosmos.text
        assert 'Дача и сад' in cosmos.text
        assert 'Бытовая химия и гигиена' in cosmos.text
        assert 'Отопление' in cosmos.text
        assert 'Спорт, отдых и хобби' in cosmos.text
        assert 'Дисконт' in cosmos.text
        assert 'Строительство и ремонт' in cosmos.text
        assert 'Автотовары' in cosmos.text
        assert 'Красота и здоровье' in cosmos.text
        assert 'Канцтовары' in cosmos.text







        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
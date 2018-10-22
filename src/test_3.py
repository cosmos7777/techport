import unittest
from selenium import webdriver
# Проверка выпадающего меню "Все категории" и производителей сайта https://www.techport.ru/
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/geckodriver')
        #self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_slider(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/")

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

        # Проверка выпадаюдего меню, раздел "Бытовая техника", Поставщик Bosch, LG
        driver.find_element_by_css_selector("a.bosch_button:nth-child(1)").is_displayed()
        driver.find_element_by_css_selector("#category-wrapper > div.tcp-category-content-list > div.tcp-category-content.block_item_1.tcp-category-content_active > div.tcp-category-content-body.body_with_icon_col > div > div.tcp-col.tcp-col_xs-3.tcp-col_icons > a.lg_button").is_displayed()

        # Проверка выпадаюдего меню, раздел "Сантехника", Поставщик Roca, Blanco
        driver.find_element_by_class_name("roca_button").is_displayed()
        driver.find_element_by_class_name("blanco_button").is_displayed()

        # Проверка выпадаюдего меню, раздел "Инструменты", Поставщик Makita, AEG
        driver.find_element_by_class_name("makita_button").is_displayed()
        driver.find_element_by_class_name("aeg_button").is_displayed()

        # Проверка выпадаюдего меню, раздел "Детские товары", Поставщик Chicco, Lego
        driver.find_element_by_class_name("chicco_button").is_displayed()
        driver.find_element_by_class_name("lego_button").is_displayed()

        # Проверка выпадаюдего меню, раздел "Спорт, отдых и хобби", Поставщик Nike, Torres
        driver.find_element_by_class_name("nike_button").is_displayed()
        driver.find_element_by_class_name("torres_button").is_displayed()

        # Проверка выпадаюдего меню, раздел "Строительсво и ремонт", Поставщик Ceresit, Момент
        driver.find_element_by_class_name("ceresit_button").is_displayed()
        driver.find_element_by_class_name("moment_button").is_displayed()

    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()
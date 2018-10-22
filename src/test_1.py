import unittest
from selenium import webdriver
# Наличие header и footer элементов проверяется при загрузке "Главная страница"
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/geckodriver')
        #self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_header_footer(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/")

        # Проверка логотипа Техпорт, сверху слева
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[3]/div/div/a").is_displayed()

        # Проверка элементы верхнего уровня Горож, Акции, Дисконт, Техбону и т.д. отборажаются
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[2]/div/div").is_displayed()

        # Элемент "Телефон города" содержит внутренний текст "8(495)228-66-69"
        cosmos = driver.find_element_by_class_name("header_phones")
        assert '8 (495) 228-66-69' in cosmos.text

        # Элемент "Расписание работы магазина" содержит внутренний текст "Пн"
        cosmos = driver.find_element_by_class_name("header_phones")
        assert 'Пн' in cosmos.text

        # Элемент "Бесплатная телефонная линия" содержит внутренний текст "8 (800) 555-87-78"
        cosmos = driver.find_element_by_class_name("header_phones")
        assert '8 (800) 555-87-78' in cosmos.text

        # Элемент "Поле поиска" отображается на странице
        driver.find_element_by_xpath("//*[@id='desktop_search_input']").is_displayed()

        # Элемент "Ссылка на ВКонтакте" отображается на странице
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[1]/div")
        assert 'Вконтакте' in cosmos.text

        # Элемент "Ссылка на Одноклассники" отображается на странице
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[2]/div")
        assert 'Одноклассники' in cosmos.text

        # Элемент "Ссылка на Facebook" отображается на странице
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[3]/div")
        assert 'Facebook' in cosmos.text

        # Элемент "Ссылка на Twitter" отображается на странице
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[4]/div")
        assert 'Twitter' in cosmos.text

        # Элемент "Ссылка на Instagram" отображается на странице
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[5]/div")
        assert 'Instagram' in cosmos.text



    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
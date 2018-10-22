import unittest
from selenium import webdriver
# Наличие header и footer элементов проверяется при загрузке "Главная страница"
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://test1.techport.ru/")

    def test_header_footer(self):
        driver = self.driver
        #driver.get("http://test1.techport.ru/")

        # Элемент "Ссылка на Одноклассники" отображается на странице
        cosmos2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[9]/div/div/div[2]/div")
        assert 'Одноклассники' in cosmos2.text


        # Элемент "Телефон города" содержит внутренний текст "8(495)228-66-69"

        #self.assertTrue("Пн-Пт 9–21, Сб-Вс 9–20", driver.find_element_by_class_name("header_phones").text)
        #self.assertTrue("8 (800) 555-87-78", driver.find_element_by_class_name("header_phones").text)




        def tear_down(self):
            #self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
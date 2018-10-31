import unittest
from selenium import webdriver


# test43 Проверка фильтров на странице - "Чек-боксы и строка поиска"
class Test(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # Проверка фильтров на странице - "Чек-боксы и строка поиска"

    def test(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki")
        # кликаем на фильтр "Производитель" и выбираем ARTEL
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/div[2]/div[2]/div[3]/div[2]/label").click()

        # Выбранный производитель отображается
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/div[2]/div[2]/div[1]").is_displayed()







    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# cosmos7777@zdenka.net abc1234
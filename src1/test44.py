import unittest
from selenium import webdriver


# test44 Проверка фильтров на странице - Проверка фильтра - "Холодильники"
class Test(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # Проверка фильтра - "Холодильники"

    def test(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki")
        # кликаем на фильтр "Холодильники" и выбираем "Трехкамерные"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[1]/div/div[2]/div/ul/li[3]").click()

        # Выбранный ильтр трехкамерные отображается
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[1]/div/div[2]/div/div").is_displayed()




    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# cosmos7777@zdenka.net abc1234
import unittest
from selenium import webdriver


# test42 Проверка фильтров на странице - "Только чек-боксы"
class Test(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # Проверка фильтров на странице - "Только чек-боксы"

    def test(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki")
        # кликаем на фильтр "Расположение мороз. камеры" и кликаем на вверху, отсутствует, справа
        driver.find_element_by_id("tpf-266").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/div[8]/div[2]/div[2]/div[1]/label").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/div[8]/div[2]/div[2]/div[2]/label").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/div[8]/div[2]/div[2]/div[3]/label").click()
        # Нажимаем "найдено"
        driver.find_element_by_id("tcp_counter").click()
        driver.find_element_by_id("tpf-226").is_enabled()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/div[8]/div[2]/div[1]").is_displayed()








    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# cosmos7777@zdenka.net abc1234
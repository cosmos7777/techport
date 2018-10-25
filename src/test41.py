import unittest
from selenium import webdriver


# test41 Проверка фильтров на странице - "От/до  и ползунок"
class Test(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # Проверка фильтров на странице - "От/до  и ползунок"

    def test(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki")
        # кликаем на фильтр "глубина" и выставляем значени 56 и 62

        #driver.find_element_by_id("tpf-227").click()
        driver.find_element_by_css_selector("#tpf-227 > div.tcp-filters__title").click()
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/div[7]/div[1]").click()
        form1 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/div[7]/div[2]/div/div[1]/div/input")
        form2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/div[7]/div[2]/div/div[2]/div/input")
        form1.clear()
        form1.send_keys("56")
        form2.clear()
        form2.send_keys("62")
        # Нажимаем "найдено"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div/div[1]/div/form/div[3]/div/div[7]/div[3]/div").click()
        driver.find_element_by_id("tpf-227").is_enabled()













    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

# cosmos7777@zdenka.net abc1234
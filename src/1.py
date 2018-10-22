import unittest
from selenium import webdriver
# Проверка формы восстановления пароля
class LoginTest(unittest.TestCase):
    def setUp(self):
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)

    def test1(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        # Нажимаем купить
        driver.find_element_by_id("item_button_buy").click()
        # прибавляем кол-во товара нажимая "+"
        driver.find_element_by_xpath("/html/body/div[2]/noindex/div/div[21]/div/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div/div[3]/button").click()
        # Нажимаем "оформить заказ"
        driver.find_element_by_css_selector("#order-basket > div > div.tcp-row > div.tcp-col.tcp-col_lg-4-5 > div > div.tcp-content-section > div > div:nth-child(1) > div > a").click()
        # Добавляем доп улугу "альфа-страхование"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[1]/form/div/div/div[1]/div[1]/div[2]/div/div/div[1]").click()

    # order-basket > div > div.tcp-row > div.tcp-col.tcp-col_lg-4-5 > div > div.tcp-content-section > div > div:nth-child(1) > div > a

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


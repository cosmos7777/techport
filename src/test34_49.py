import unittest
from selenium import webdriver
# test34 Проверка покупки товара, покупка товара в окне товара, полный цикл
class Test(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)



    # Покупка товара в окне товара

    def test1(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        # прибавляем кол-во товара нажимая "+"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[2]/form/div/div[1]/div/div[3]/button").click()
        # Нажимаем купить
        driver.find_element_by_id("item_button_buy").click()
        # Нажимаем "оформить заказ"
        driver.find_element_by_css_selector("#order-basket > div > div.tcp-row > div.tcp-col.tcp-col_lg-4-5 > div > div.tcp-content-section > div > div:nth-child(1) > div > a").click()
        # Нажимаем оформить
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[1]/form/div/div/div[2]/div/a").click()

        # Заполняем Имя и фамилию
        name = driver.find_element_by_id("order_name")
        name.send_keys("Андрей Иванов")
        # Заполняем e-mail
        name = driver.find_element_by_id("order_email")
        name.send_keys("cosmos7777@zdenka.net")
        # Заполняем телефон
        name = driver.find_element_by_id("order_phone")
        name.send_keys("9011111111")
        # Нажимаем "Продолжить"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div[2]/form/div/div[1]/div[3]/div/button").click()

        # Выбираемм способ получения "В пункте выдачи"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div[2]/form/div/div[1]/div[2]/div/div[2]/div[2]/label").click()
        # Нажимаем "Продолжить"
        driver.find_element_by_id("button_step_2").click()

        # Выбираем способ оплаты "При получении"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div[2]/form/div/div[1]/div[3]/div/div[2]/div[1]/div[1]/label").click()
        # Нажимаем Оформить
        driver.find_element_by_id("to_finish_checkout").click()

        # Проверяем что заказ оформлен, появляется надпись "Ваш заказ ... принят".
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div/div/div/div[1]/div").is_displayed()









    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
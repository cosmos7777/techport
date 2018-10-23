import unittest
from selenium import webdriver
# test33 Проверка покупки товара, покупка товара в окне товара
class LoginTest(unittest.TestCase):
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
        nom = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div/div/div/div[1]/div")
        nom.is_displayed()














        # Шаг 2, Заходим в CRM
        driver.get("http://vm-armtest.addi.ru:8080/workstation/#!/orders")
        # Заполняем логин
        name = driver.find_element_by_id("gwt-uid-3")
        name.send_keys("gevorkov")
        # Заполняем Пароль
        pas = driver.find_element_by_id("gwt-uid-5")
        pas.send_keys("Manchester23")
        # Нажимаем "Войти"
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div[7]/div").click()

        # Вносим номер заказа в поле "Заказ №"
        zakaz = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div[1]/div/div[12]/input")
        zakaz.send_keys("TP8923")

        # Выбираем заказ
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div").is_selected()















    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
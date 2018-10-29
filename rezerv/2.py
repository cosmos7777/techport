import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# test33 Проверка покупки товара, покупка товара в окне товара
class LoginTest(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)





    def test1(self):
        driver = self.driver

        # Шаг 2, Заходим в CRM
        driver.get("http://vm-armtest.addi.ru:8080/workstation/#!/orders")
        # Заполняем логин
        name = driver.find_element_by_id("gwt-uid-3")
        name.send_keys("gevorkov")
        # Заполняем Пароль
        pas = driver.find_element_by_id("gwt-uid-5")
        pas.send_keys("Manchester23")
        # Нажимаем "Войти"
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div[7]/div").click()

        # Вносим номер заказа в поле "Заказ №"
        zakaz = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div[1]/div/div[12]/input")
        zakaz.send_keys("8925-67780")
        # нажимаем найти
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[5]/div").click()


        # выбираем наш заказ и кликаем два раза
        el = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/table/tbody/tr/td[3]/div")
        actionchains = ActionChains(driver)
        actionchains.double_click(el).perform()

        # Сверяем название товара "Холодильник" в заказе
        hol = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[3]/div/div")
        assert 'Холодильник' in hol.text











    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
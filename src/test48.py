import unittest
from selenium import webdriver
# test48 Проверка входа логина и пароля личного кабинета, Положительный сценарий, заполнено оба поля, редактирование личных данных
class Test(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox(executable_path='/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)




    def test(self):
        # Положительный сценарий, заполнено оба поля
        driver = self.driver
        # Загружаем страницу входа, и воодим логин,пароль
        driver.get("https://test1.techport.ru/login")
        login_field = driver.find_element_by_id("login_static")
        login_field.send_keys("cosmos7777@zdenka.net")
        password_field = driver.find_element_by_id("password_static")
        password_field.send_keys("abc1234")
        # нажимаем войти
        button_login = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button")
        button_login.click()
        # проверяем свое имя "Andrey" сверху справа
        #user_mail = driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[4]/div/div/div[3]/div/div[1]")
        #assert "Andrey" in user_mail.text
        # assert user_mail.text == "Andrey"

        # Заходим в свой личный кабинет
        driver.find_element_by_class_name("tcp-user-preview__icon").click()
        #driver.find_element_by_class_name("tcp-user-preview__name").click()
        # кликаем на "мои данные"
        driver.find_element_by_css_selector("a.tcp-user-menu__item:nth-child(1) > span:nth-child(1)").click()
        # нажимаем "редактировать"
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[4]/div/div[1]/div[1]/div/div[2]/div[2]/div[3]/button").click()
        # Вводим Имя
        name = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[4]/div/div[1]/div[2]/div/form/div[1]/div[1]/div[1]/div/input")
        name.clear()
        name.send_keys("Andrey")
        # вводим e-mail
        email = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[4]/div/div[1]/div[2]/div/form/div[1]/div[1]/div[2]/div/input")
        email.clear()
        email.send_keys("cosmos7777@zdenka.net")
        # вводим телефон
        phone = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[4]/div/div[1]/div[2]/div/form/div[1]/div[2]/div[1]/div/input")
        phone.clear()
        phone.send_keys("9011111111")
        # нажимаем сохранить
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[4]/div/div[1]/div[2]/div/form/div[2]/div[2]/button").click()
        # проверяем, что введенные данные сохранились и отображаются
        forma = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[4]/div/div[1]/div[1]/div/div[2]")
        assert "Andrey" in forma.text
        assert "+7 (901) 111-11-11" in forma.text
        assert "cosmos7777@zdenka.net" in forma.text



    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()




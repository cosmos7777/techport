import unittest
from selenium import webdriver

class LoginTest1(unittest.TestCase):
    def setUp(self1):
        self1.driver = webdriver.Firefox(executable_path='/geckodriver')
        #self1.driver = webdriver.Chrome(executable_path='/chromedriver')
        self1.driver.maximize_window()
        self1.driver.implicitly_wait(10)
    def test_user_login1(self1):
        # Отрицательный сценарий, на заполнено оба поля
        driver = self1.driver
        driver.get("https://test1.techport.ru/login")
        # Загружаем страницу и нажимаем войти
        button_login = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button")
        button_login.click()
        # проверяем слово "e-mail" в ошибке
        user_mail = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[1]/div/div[2]")
        assert "e-mail" in user_mail.text
    def tear_down(self1):
     self1.driver.quit()




class LoginTest2(unittest.TestCase):
    def setUp(self2):
        #self2.driver = webdriver.Chrome(executable_path='/chromedriver')
        self2.driver = webdriver.Firefox(executable_path='/geckodriver')
        self2.driver.maximize_window()
        self2.driver.implicitly_wait(10)
    def test_user_login2(self2):
        # Отрицательный сценарий, не заполнено поле логина
        driver = self2.driver
        driver.get("https://test1.techport.ru/login")
        # Загружаем страницу, вводим пароль и нажимаем войти
        password_field = driver.find_element_by_id("password_static")
        password_field.send_keys("abc1234")
        button_login = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button")
        button_login.click()
        # проверяем слово "e-mail" в ошибкеа
        user_mail = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[1]/div/div[2]")
        assert "e-mail" in user_mail.text
    def tear_down(self2):
     self2.driver.quit()

class LoginTest3(unittest.TestCase):
    def setUp(self3):
        self3.driver = webdriver.Firefox(executable_path='/geckodriver')
        #self3.driver = webdriver.Chrome(executable_path='/chromedriver')
        self3.driver.maximize_window()
        self3.driver.implicitly_wait(10)
    def test_user_login3(self3):
        # Отрицательный сценарий, не заполнено поле пароля
        driver = self3.driver
        driver.get("https://test1.techport.ru/login")
        # Загружаем страницу, вводим логин и нажимаем войти
        login_field = driver.find_element_by_id("login_static")
        login_field.send_keys("cosmos7777@zdenka.net")
        button_login = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[3]/button")
        button_login.click()
        # проверяем слово "пароль" в ошибке
        user_mail = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div/div/div/div[1]/form/div[2]/div[1]/div[2]")
        assert "пароль" in user_mail.text
    def tear_down(self3):
     self3.driver.quit()

class LoginTest4(unittest.TestCase):
    def setUp(self4):
        self4.driver = webdriver.Firefox(executable_path='/geckodriver')
        #self4.driver = webdriver.Chrome(executable_path='/chromedriver')
        self4.driver.maximize_window()
        self4.driver.implicitly_wait(10)
    def test_user_login4(self):
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
        user_mail = driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div[4]/div/div/div[3]/div/div[1]")
        assert "Andrey" in user_mail.text
        # assert user_mail.text == "Andrey"
    def tear_down(self4):
     self4.driver.quit()




if __name__ == "__main__":
    unittest.main()




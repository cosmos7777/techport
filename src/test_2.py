import unittest
from selenium import webdriver
# Проверка работы блоков на главной странице
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/geckodriver')
        #self.driver = webdriver.Chrome(executable_path='/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_slider(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/")

        # Выполнено нажатие на кнопку "Большой слайдер с акциями-скролл вправо,влево, и отображение баннера на странице
        driver.find_element_by_xpath("//*[@id='banner-next']").click()
        driver.find_element_by_xpath("//*[@id='banner-prev']").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[1]/div/div/div[1]/div/div[1]/div/div/div[4]/a/img").is_displayed()

        # Хиты продаж - кнопка скролл вправо,влево, и заголовок "Хиты продаж" отображается на странице
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div[1]/div[1]/div/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div[1]/div[1]/div/div[1]").click()
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div/div[1]/div[2]")
        assert 'Хиты продаж' in cosmos.text

        # Отзывы наших покупателей - скролл вправо,влево и заголовок "Отзывы наших покупателей" отображается на странице
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[5]/div/div[1]/div[1]/div/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[5]/div/div[1]/div[1]/div/div[1]").click()
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[5]/div/div[1]/div[2]")
        assert 'Отзывы наших покупателей' in cosmos.text

        # Бренды -  скролл вправо,влево. И заголовок "Бренды " отображается на странице
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[6]/div/div[1]/div[1]/div/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[6]/div/div[1]/div[1]/div/div[1]").click()
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[6]/div/div[1]/div[2]")
        assert 'Бренды' in cosmos.text

        # Блок новости -  скролл вправо,влево. И заголовок "Новости " отображается на странице
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[7]/div/div[1]/div[1]/div/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[7]/div/div[1]/div[1]/div/div[1]").click()
        cosmos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[7]/div/div[1]/div[2]")
        assert 'Новости' in cosmos.text

        # Кликаем в блоке новостей на кнопку "Хочу подписаться", и поле ввода e-mail появляется
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[8]/div/div/div[3]/button").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[8]/div/div/form/div/div/div[1]/div[1]/div/div/input").is_displayed()


    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()
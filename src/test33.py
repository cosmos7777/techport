import unittest
from selenium import webdriver
# test33 Проверка покупки товара, покупка в 1 клик
class LoginTest(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(30)
      self.driver.set_page_load_timeout(45)




    # Покупка в 1 клик

    def test1(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        # Нажимаем купить в 1 клик



        #driver.find_element_by_link_text("Купить в 1 клик").click()
        #driver.find_element_by_class_name("tcp-list-group__icon").click()
        #driver.find_element_by_css_selector("div.tcp-product-body:nth-child(6) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1)").click()
        driver.find_element_by_css_selector("#page-section > div.item_wrapp > div.item_info > div > div.tcp-product.tcp-product_single.tcp-product_no_radius > div:nth-child(2) > div.tcp-col.tcp-col_md-4.tcp-col_lg-3.tcp-right-block > div:nth-child(6) > div > div > ul > li:nth-child(1)").click()





        # Заголовок "Купить в 1 клик" отображается
        driver.find_element_by_id("icon-modal-content").is_displayed()






    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
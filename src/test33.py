import unittest
from selenium import webdriver
# test33 Проверка покупки товара, покупка в 1 клик
class LoginTest(unittest.TestCase):
    def setUp(self):
      #self.driver = webdriver.Firefox(executable_path='/geckodriver')
      self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)



    # Покупка в 1 клик

    def test1(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        # Нажимаем купить в 1 клик
        driver.find_element_by_css_selector("#page-section > div.item_wrapp > div.item_info > div > div.tcp-product.tcp-product_single.tcp-product_no_radius > div:nth-child(2) > div.tcp-col.tcp-col_lg-3.tcp-visible-lg > div.tcp-product-detail.tcp-product-detail_full.tcp-product-detail_bordered > div.tcp-product-detail__item.tcp-product-detail__item_pad-xs > div.tcp-product-specification.tcp-product-specification_inline > table > tbody > tr:nth-child(13) > td > a").click()

        #driver.find_element_by_xpath("//*[@id=page-section]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[13]/td/a").click()
        # Заголовок "Купить в 1 клик" отображается
        driver.find_element_by_id("icon-modal-content").is_displayed()





    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
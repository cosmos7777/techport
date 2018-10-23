import unittest
from selenium import webdriver
# test38 Страница продукта - проверка элементов кол-во штук товара, проверка кнопки "все характеристики".
class Test(unittest.TestCase):
    def setUp(self):
      self.driver = webdriver.Firefox(executable_path='/geckodriver')
      #self.driver = webdriver.Chrome(executable_path='/chromedriver')
      self.driver.maximize_window()
      self.driver.implicitly_wait(30)



    # Проверка кнопки "все характеристики"

    def test(self):
        driver = self.driver
        driver.get("http://test1.techport.ru/katalog/products/holodilniki/dvuhkamernye/holodilnik-atlant-4008-020")
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[13]/td/a").click()
        driver.find_element_by_css_selector("#page-section > div.item_wrapp > div.item_info > div > div.tcp-product.tcp-product_single.tcp-product_no_radius > div:nth-child(2) > div.tcp-col.tcp-col_lg-3.tcp-visible-lg > div.tcp-product-detail.tcp-product-detail_full.tcp-product-detail_bordered > div.tcp-product-detail__item.tcp-product-detail__item_pad-xs > div.tcp-product-specification.tcp-product-specification_inline > table > tbody > tr:nth-child(13) > td > a").click()

        cos = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[2]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/table/tbody/tr[1]/td[1]")
        assert 'Общий полезный объем' in cos.text






    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# cosmos7777@zdenka.net abc1234
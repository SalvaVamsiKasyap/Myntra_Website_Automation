import time

from selenium.webdriver.common.by import By


class cheap_shirts_add_to_cart:

    def __init__(self,driver):

        self.driver = driver

    click_on_item = (By.XPATH,'//li[@class="product-base"]/a')
    add_to_cart = (By.XPATH,'//span[@class="myntraweb-sprite pdp-whiteBag sprites-whiteBag pdp-flex pdp-center"]')
    select_size = (By.XPATH,"//p[text()='6-12M']//parent::button")

    added_to_cart=(By.XPATH,"//a[@href='/checkout/cart']/span[text()='GO TO BAG']")

    def clickonitem(self):

        items = self.driver.find_elements(*cheap_shirts_add_to_cart.click_on_item)
        for item in items:

            item.click()
            Windows_opened = self.driver.window_handles
            self.driver.switch_to.window(Windows_opened[1])
            time.sleep(5)
            self.driver.find_element(*cheap_shirts_add_to_cart.select_size).click()
            time.sleep(5)
            self.driver.find_element(*cheap_shirts_add_to_cart.add_to_cart).click()
            self.driver.switch_to.window(Windows_opened[0])

        time.sleep(10)


    # def addtocart(self):
    #     Windows_opened = self.driver.window_handles
    #     self.driver.switch_to.window(Windows_opened[1])
    #     get_title = self.driver.title
    #     print(get_title)
    #     #time.sleep(25)
    #     self.driver.find_element(*myntrasareeselection.add_to_cart).click()
    #     time.sleep(5)
    #     return self.driver.find_element(*myntrasareeselection.added_to_cart).click()


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class myntraloggedinpage:

    def __init__(self, driver):
        self.driver = driver
        self.A = ActionChains(self.driver)

    select_women = (By.XPATH, "//div[@data-reactid='179']/a")
    select_saree = (By.XPATH, "//li[@data-reactid='193']/a")

    def women(self):
        wo_men = self.driver.find_element(*myntraloggedinpage.select_women)
        self.A.move_to_element(wo_men).perform()

    def saree(self):
        sa_ree = self.driver.find_element(*myntraloggedinpage.select_saree)
        self.A.move_to_element(sa_ree).click().perform()

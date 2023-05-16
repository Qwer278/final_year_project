from selenium.webdriver.common.by import By

from AutomationController.DriverUtilities.DriverUtils import DriverUtilitiesMethod
from Locators.ItemPageLocatos import *

class ItemPage(DriverUtilitiesMethod):

    def add_to_cart(self):
        self.click_element(element_locator=add_to_cart_btn, find_by='css')

    def add_to_wish_list(self):
        self.click_element(element_locator=add_to_wish_btn, find_by='css')

    def proceed_to_checkout(self):
        try:
            self.click_element(element_locator=proceed_to_checkout, find_by='xpath')
        except:
            self.click_element(element_locator=proceed_to_buy, find_by='xpath')

    def cod_place(self):
        self.click_element(element_locator=cod,find_by='xpath')

    def continue_btn(self):
        x=self.driver.find_elements(by=By.XPATH, value=ok_btn)
        x[0].click()
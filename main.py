from AutomationController.DriverUtilities.DriverBasePage import DriverBase
from AutomationController.DriverUtilities.DriverUtils import DriverUtilitiesMethod
from App.SearchPage import SearchPage
from App.HomePage import HomePage
from App.ItemPage import ItemPage
from Config.Credentials import *
import time


def process(item):
    driver = DriverBase().initiate_driver()
    DriverUtilitiesMethod(driver, 10).navigate_to_url("https://www.amazon.in/")
    HomePage(driver, 10).sign_in(driver)
    HomePage(driver, 10).search_item(item=item)
    SearchPage(driver, 10).open_searched_item(driver, item_for_search)
    ItemPage(driver, 10).add_to_cart()
    ItemPage(driver, 10).proceed_to_checkout()
    ItemPage(driver, 10).cod_place()
    # ItemPage(driver, 10).continue_btn()
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    process(item_for_search)

from pages import BasePage, LoginPage, InventoryPage, ItemPage, CartPage
from time import sleep

def test_est_1_login(driver) -> None:
    auth_page = LoginPage(driver)
    auth_page.auth('standard_user', 'secret_sauce')

    inventory_page = InventoryPage(driver)
    inventory_page.choose_item()
    item_page = ItemPage(driver)
    item_page.add_to_cart_btn_click()

    item_page.back_to_products_click()
    inventory_page.add_jacket_to_cart_btn_click()
    inventory_page.cart_btn_click()

    cart_page = CartPage(driver)
    assert cart_page.number_of_products() == 2
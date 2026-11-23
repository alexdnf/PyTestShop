from playwright.sync_api import Page



username = "standard_user"
password = "secret_sauce"


class LoginPage:

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page

        self.login_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def login(self):
        self.page.goto(self.URL)

        self.login_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
        return MainPage(self.page)

class MainPage:
    def __init__(self, page: Page):
        self.page = page

        self.main_header = page.locator('[data-test="title"]')
        self.cart_button = page.locator('[data-test="shopping-cart-link"]')
        self.buy_button = page.locator('.btn')
        self.cart_bridge = page.locator('[data-test="shopping-cart-badge"]')

    def add_to_cart(self):

        self.buy_button.nth(0).click()
        self.buy_button.nth(3).click()

    def go_to_cart(self):
        self.cart_button.click()
        return CartPage(self.page)


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.cart_header = page.locator('[data-test="title"]')
        self.return_button = page.locator('[data-test="continue-shopping"]')
        self.continue_button = page.locator('[data-test="checkout"]')
        self.inventory_item = page.locator('[data-test="inventory-item"]')

    def continue_shopping(self):
        self.return_button.click()
        return MainPage(self.page)

    def checkout(self):
        self.continue_button.click()
        return CheckoutPageInformation(self.page)

class CheckoutPageInformation:
    def __init__(self, page: Page):
        self.page = page

        self.checkout_header = page.locator('[data-test="title"]')
        self.checkout_form = page.locator('.checkout_info')

        self.first_name_field = page.locator('[data-test="firstName"]')
        self.last_name_field = page.locator('[data-test="lastName"]')
        self.postal_code_field = page.locator('[data-test="postalCode"]')

        self.cancel_button = page.locator('[data-test="cancel"]')
        self.checkout_continue_button = page.locator('[data-test="continue"]')

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(postal_code)
        return self

    def checkout_continue(self):
        self.checkout_continue_button.click()
        return CheckoutPageOverview(self.page)

    def cancel(self):
        self.cancel_button.click()
        return CartPage(self.page)

class CheckoutPageOverview:
    def __init__(self, page: Page):
        self.page = page

        self.checkout_header_over = page.locator('[data-test="title"]')
        self.cancel_overview_button = page.locator('[data-test="cancel"]')
        self.checkout_finish_button = page.locator('[data-test="finish"]')


    def cancel_overview(self):
        self.cancel_overview_button.click()
        return CheckoutPageInformation(self.page)

    def checkout_finish(self):
        self.checkout_finish_button.click()
        return FinishPage(self.page)

class FinishPage:
    def __init__(self, page: Page):
        self.page = page

        self.complete_header = page.locator('[data-test="complete-header"]')
        self.back_to_home_button = page.locator('[data-test="back-to-products"]')
        self.pdf_download_button = page.locator('[data-test="generate-pdf-order"]')

    def back_to_home(self):
        self.back_to_home_button.click()
        return MainPage(self.page)

    def pdf_order(self):
        with self.page.expect_download() as download_info:
            self.pdf_download_button.click()
        return download_info.value












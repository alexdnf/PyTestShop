from playwright.sync_api import Page, expect

from Pages import LoginPage, MainPage, CartPage, CheckoutPageInformation, CheckoutPageOverview, FinishPage


def test_user_login_and_buying(page: Page, user_form_data):

    main_page = LoginPage(page).login()

    expect(main_page.main_header).to_have_text("Products")
    expect(main_page.cart_button).to_be_visible()
    expect(main_page.cart_button).to_have_attribute("aria-label", "Cart, empty")
    expect(main_page.cart_bridge).to_be_hidden()

    main_page.add_to_cart()
    expect(main_page.buy_button.nth(0)).to_have_text("Remove")
    expect(main_page.buy_button.nth(3)).to_have_text("Remove")
    expect(main_page.cart_button).to_have_attribute("aria-label", "Cart, 2 items")
    expect(main_page.cart_bridge).to_be_visible()
    expect(main_page.cart_bridge).to_have_text("2")
    main_page.go_to_cart()

    cart_page = CartPage(page)
    expect(cart_page.cart_header).to_have_text("Your Cart")
    expect(cart_page.return_button).to_be_visible()
    expect(cart_page.continue_button).to_be_visible()
    expect(cart_page.inventory_item).to_have_count(2)
    cart_page.checkout()

    checkout_page_information = CheckoutPageInformation(page)
    expect(checkout_page_information.checkout_form).to_be_visible()
    expect(checkout_page_information.checkout_header).to_be_visible()
    expect(checkout_page_information.checkout_header).to_have_text("Checkout: Your Information")

    checkout_page_information.fill_checkout_form(**user_form_data)
    checkout_page_information.checkout_continue()

    checkout_page_overview = CheckoutPageOverview(page)
    expect(checkout_page_overview.checkout_header_over).to_have_text("Checkout: Overview")
    checkout_page_overview.checkout_finish()

    finish_page = FinishPage(page)
    expect(finish_page.complete_header).to_have_text("Thank you for your order!")
    download = finish_page.pdf_order()
    assert download.suggested_filename.endswith(".pdf")










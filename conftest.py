import os

import pytest
from faker import Faker
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    # По умолчанию браузер видимый (удобно для демонстрации).
    # Для CI: HEADLESS=true pytest
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture
def context(browser):
    ctx = browser.new_context()
    yield ctx
    ctx.close()


@pytest.fixture
def page(context):
    yield context.new_page()


@pytest.fixture
def fake():
    return Faker("ru_Ru")


@pytest.fixture
def user_form_data(fake):
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "postal_code": fake.postcode(),
    }
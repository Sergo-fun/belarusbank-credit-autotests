
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.credit_calculator_locators import CreditCalculatorLocators


class CreditCalculatorPage:

    URL = "https://belarusbank.by/fizicheskim_licam/kredit/consumer/kredit-na-svaye/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def _click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def _find_visible_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def open(self):
        self.driver.get(self.URL)

    def click_calculator(self):
        self._click(CreditCalculatorLocators.ESCAPE_CONSULTANT)
        self._click(CreditCalculatorLocators.COOKIE_BUTTON)
        self._click(CreditCalculatorLocators.CALCULATOR)

        self._find_visible_element(
            CreditCalculatorLocators.SETTLEMENT_TERMS
        )

    def ensure_calculator_settlement_are_displayed(self):
        self._click(CreditCalculatorLocators.SETTLEMENT_TERMS)

        assert self._find_visible_element(
            CreditCalculatorLocators.CALCULATION_MAXIMUM_AMOUNT
        )

        assert self._find_visible_element(
            CreditCalculatorLocators.CALCULATION_MAXIMUM_INCOME
        )

    def ensure_calculate_button_is_displayed(self):
        assert self._find_visible_element(
            CreditCalculatorLocators.GET_THE_CALCULATION
        )

    def ensure_select_is_displayed(self):
        assert self._find_visible_element(
            CreditCalculatorLocators.SETTLEMENT_TERMS
        )

    def _select_calculation_mode(self, option_locator):
        self._click(CreditCalculatorLocators.SETTLEMENT_TERMS)

        option = self._find_visible_element(option_locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            option
        )

        self._click(option_locator)

    def select_calculation_maximum_amount(self):
        self._select_calculation_mode(
            CreditCalculatorLocators.CALCULATION_MAXIMUM_AMOUNT
        )

    def select_calculation_maximum_income(self):
        self._select_calculation_mode(
            CreditCalculatorLocators.CALCULATION_MAXIMUM_INCOME
        )

    def _enter_value(self, locator, value):
        element = self._find_visible_element(locator)

        element.clear()
        element.send_keys(value)

    def enter_borrowers_income(self, income):
        self._enter_value(
            CreditCalculatorLocators.BORROWERS_INCOME,
            income
        )

    def enter_early_payments(self, payments):
        self._enter_value(
            CreditCalculatorLocators.EARLY_PAYMENTS,
            payments
        )

    def enter_aliments(self, aliments):
        self._enter_value(
            CreditCalculatorLocators.ALIMENTS,
            aliments
        )

    def enter_other_payments(self, payments):
        self._enter_value(
            CreditCalculatorLocators.OTHER_PAYMENTS,
            payments
        )

    def click_get_the_calculation(self):
        self._click(CreditCalculatorLocators.GET_THE_CALCULATION)

    def ensure_calculation_result_displayed(self):
        self._find_visible_element(
            CreditCalculatorLocators.CALCULATION_RESULT
        )

    def click_toggle_website(self):
        self._click(CreditCalculatorLocators.TOGGLE_WEBSITE)

    def ensure_letters_are_not_allowed(self):
        income_field = self._find_visible_element(
            CreditCalculatorLocators.BORROWERS_INCOME
        )

        income_field.clear()
        income_field.send_keys("abcdef")

        assert income_field.get_attribute("value") == ""

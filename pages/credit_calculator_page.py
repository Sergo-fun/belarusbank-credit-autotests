from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.credit_calculator_locators import CreditCalculatorLocators



class CreditCalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://belarusbank.by/fizicheskim_licam/kredit/consumer/kredit-na-svaye/")

    def click_calculator(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(CreditCalculatorLocators.ESCAPE_CONSULTANT)
        ).click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(CreditCalculatorLocators.COOKIE_BUTTON)
        ).click()

        calculator = self.driver.find_element(
            *CreditCalculatorLocators.CALCULATOR
        )

        calculator.click()
        self.driver.execute_script(
            "window.scrollBy(0, 150);"
        )
        sleep(5)

    def ensure_calculator_settlement_are_displayed(self):
        self.driver.find_element(
            *CreditCalculatorLocators.SETTLEMENT_TERMS
        ).click()

        assert self.driver.find_element(
            *CreditCalculatorLocators.CALCULATION_MAXIMUM_AMOUNT
        ).is_displayed()

        assert self.driver.find_element(
            *CreditCalculatorLocators.CALCULATION_MAXIMUM_INCOME
        ).is_displayed()

    def ensure_calculate_button_is_displayed(self):

        assert self.driver.find_element(
            *CreditCalculatorLocators.GET_THE_CALCULATION
        ).is_displayed()


    def ensure_select_is_displayed(self):
        assert self.driver.find_element(
            *CreditCalculatorLocators.SETTLEMENT_TERMS
        ).is_displayed()

    def select_calculation_maximum_amount(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                CreditCalculatorLocators.SETTLEMENT_TERMS
            )
        ).click()

        option = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                CreditCalculatorLocators.CALCULATION_MAXIMUM_AMOUNT
            )
        )


        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            option
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                CreditCalculatorLocators.CALCULATION_MAXIMUM_AMOUNT
            )
        ).click()


    def select_calculation_maximum_income(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                CreditCalculatorLocators.SETTLEMENT_TERMS
            )
        ).click()

        option = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                CreditCalculatorLocators.CALCULATION_MAXIMUM_INCOME
            )
        )


        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            option
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                CreditCalculatorLocators.CALCULATION_MAXIMUM_INCOME
            )
        ).click()

    def _enter_value(self, locator, value):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(value)

    def enter_borrowers_income(self, income):
        self._enter_value(CreditCalculatorLocators.BORROWERS_INCOME, income)

    def enter_early_payments(self, payments):
        self._enter_value(CreditCalculatorLocators.EARLY_PAYMENTS, payments)

    def enter_aliments(self, aliments):
        self._enter_value(CreditCalculatorLocators.ALIMENTS, aliments)

    def enter_other_payments(self, payments):
        self._enter_value(CreditCalculatorLocators.OTHER_PAYMENTS, payments)

    def click_get_the_calculation(self):
        self.driver.find_element(
            *CreditCalculatorLocators.GET_THE_CALCULATION
        ).click()

    def ensure_calculation_result_displayed(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                CreditCalculatorLocators.CALCULATION_RESULT
            )
        )

    def click_toggle_website(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreditCalculatorLocators.TOGGLE_WEBSITE)
        ).click()

    def ensure_letters_are_not_allowed(self):
        sleep(5)
        income_field = self.driver.find_element(
            *CreditCalculatorLocators.BORROWERS_INCOME
        )

        income_field.clear()
        income_field.send_keys("abcdef")

        assert income_field.get_attribute("value") == ""










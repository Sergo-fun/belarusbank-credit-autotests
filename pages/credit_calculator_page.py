from locators.credit_calculator_locators import CreditCalculatorLocators


class CreditCalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("URL_СТРАНИЦЫ_КРЕДИТА")

    def enter_credit_amount(self, amount):
        self.driver.find_element(
            *CreditCalculatorLocators.CREDIT_AMOUNT
        ).clear()

        self.driver.find_element(
            *CreditCalculatorLocators.CREDIT_AMOUNT
        ).send_keys(str(amount))

    def select_credit_term(self, term):
        # Реализуем после изучения типа элемента на странице
        pass

    def calculate(self):
        self.driver.find_element(
            *CreditCalculatorLocators.CALCULATE_BUTTON
        ).click()

    def get_monthly_payment(self):
        return self.driver.find_element(
            *CreditCalculatorLocators.MONTHLY_PAYMENT
        ).text
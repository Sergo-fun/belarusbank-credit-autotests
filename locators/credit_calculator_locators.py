from selenium.webdriver.common.by import By


class CreditCalculatorLocators:
    CALCULATOR = (By.XPATH, "//a[@class='page-tab swiper-slide swiper-slide-next']")
    ESCAPE_CONSULTANT = (By.XPATH, "//*[@fill='currentColor']")
    COOKIE_BUTTON = (By.XPATH, "//button[@class='cookie-button btn']")
    SETTLEMENT_TERMS = (By.XPATH, "//div[@class='custom-trigger default']")
    CALCULATION_MAXIMUM_AMOUNT = (By.XPATH, "//div[@class='custom-option' and @data-value='14']")
    CALCULATION_MAXIMUM_INCOME = (By.XPATH, "//div[@class='custom-option' and @data-value='15']")
    BORROWERS_INCOME = (By.XPATH, "//input[@class='_req']")
    EARLY_PAYMENTS = (By.XPATH, "//input[@name='R1']")
    ALIMENTS = (By.XPATH, "//input[@name='R3']")
    OTHER_PAYMENTS = (By.XPATH, "//input[contains(@oninput, 'R2')]")
    GET_THE_CALCULATION = (By.XPATH, "//a[@id='calc']")
    CALCULATION_RESULT = (By.XPATH, "//div[@id='ajaxResult']")
    TOGGLE_WEBSITE = (By.XPATH, "(//span[@class='filters__category_text'])[2]")

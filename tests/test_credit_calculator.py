from time import sleep

import allure
import pytest

from pages.credit_calculator_page import CreditCalculatorPage


@allure.feature("Кредитный калькулятор")
@allure.story("Отображение калькулятора")


@allure.title("TC-01. Проверка отображения кредитного калькулятора")
def test_credit_calculator_is_displayed(driver):
    page = CreditCalculatorPage(driver)

    with allure.step("Step 1. Открыть страницу кредита CLICKни Осень"):
        page.open()



@allure.title("TC-02. Проверка наличия элементов калькулятора")
def test_calculator_elements_are_displayed(driver):
    page = CreditCalculatorPage(driver)

    with allure.step("Шаг 1. Открыть страницу кредита"):
        page.open()

    with allure.step("Шаг 2. Перейти к калькулятору"):
        page.click_calculator()

    with allure.step("Шаг 3. Проверить варианты расчета"):
        page.ensure_calculator_settlement_are_displayed()

    with allure.step("Шаг 4. Проверить наличие выпадающего списка"):
        page.ensure_select_is_displayed()

    with allure.step("Шаг 5. Проверить наличие кнопки расчёта"):
        page.ensure_calculate_button_is_displayed()




@allure.title("TC-03. Расчёт максимальной суммы кредита")
def test_calculate_maximum_credit_amount(driver):
    page = CreditCalculatorPage(driver)

    with allure.step("Шаг 1. Открыть страницу кредита"):
        page.open()

    with allure.step("Шаг 2. Перейти к калькулятору"):
        page.click_calculator()

    with allure.step("Шаг 3. Выбрать режим расчёта максимальной суммы кредита"):
        page.select_calculation_maximum_amount()

    with allure.step("Шаг 4. Заполнить финансовые данные"):
        page.enter_borrowers_income("3000")
        page.enter_early_payments("200")
        page.enter_aliments("100")
        page.enter_other_payments("150")

    with allure.step("Шаг 5. Выполнить расчёт кредита"):
        page.click_get_the_calculation()

    with allure.step("Шаг 6. Проверить отображение результатов расчёта"):
        page.ensure_calculation_result_displayed()


@allure.title("TC-04. Расчёт необходимого дохода для получения кредита")
def test_calculate_maximum_income(driver):
    page = CreditCalculatorPage(driver)

    with allure.step("Шаг 1. Открыть страницу кредита"):
        page.open()

    with allure.step("Шаг 2. Перейти к калькулятору"):
        page.click_calculator()

    with allure.step("Шаг 3. Выбрать режим расчёта необходимого дохода"):
        page.select_calculation_maximum_income()

    with allure.step("Шаг 4. Заполнить финансовые данные"):
        page.enter_borrowers_income("5000")
        page.enter_early_payments("200")
        page.enter_aliments("100")
        page.enter_other_payments("150")

    with allure.step("Шаг 5. Выполнить расчёт кредита"):
        page.click_get_the_calculation()

    with allure.step("Шаг 6. Проверить отображение результатов расчёта"):
        page.ensure_calculation_result_displayed()


@allure.title("TC-05. Проверка запрета ввода букв в поле суммы кредита")
def test_calculate_maximum_income(driver):
    page = CreditCalculatorPage(driver)

    with allure.step("Шаг 1. Открыть страницу кредита"):
        page.open()

    with allure.step("Шаг 2. Перейти к калькулятору"):
        page.click_calculator()

    with allure.step("Шаг 3. Переключить калькулятор на сайте"):
        page.click_toggle_website()

    with allure.step("Шаг 4. Выбрать режим расчёта необходимого дохода"):
        page.select_calculation_maximum_income()

    with allure.step("Шаг 5. Проверить, что поле не принимает буквы"):
        page.ensure_letters_are_not_allowed()

    with allure.step("Шаг 6. Заполнить финансовые данные"):
        page.enter_borrowers_income("5000")
        page.enter_early_payments("200")
        page.enter_aliments("100")
        page.enter_other_payments("150")

    with allure.step("Шаг 7. Выполнить расчёт кредита"):
        page.click_get_the_calculation()

    with allure.step("Шаг 8. Проверить отображение результатов расчёта"):
        page.ensure_calculation_result_displayed()

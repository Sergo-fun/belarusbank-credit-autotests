
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

    #with allure.step("Step 2. Проверить отображение калькулятора"):
        #page.ensure_calculator_is_displayed()

    #with allure.step("Step 3. Проверить отображение блока результата"):
        #page.ensure_result_block_is_displayed()


@allure.title("TC-02. Проверка наличия элементов калькулятора")
def test_calculator_elements_are_displayed(driver):
    page = CreditCalculatorPage(driver)

    with allure.step("Step 1. Открыть страницу кредита"):
        page.open()

    with allure.step("Step 2. Проверить наличие полей калькулятора"):
        page.ensure_calculator_fields_are_displayed()

    with allure.step("Step 3. Проверить наличие вариантов грейс-периода"):
        page.ensure_grace_period_options_are_displayed()

    with allure.step("Step 4. Проверить наличие выпадающего списка"):
        page.ensure_select_is_displayed()

    with allure.step("Step 5. Проверить наличие кнопки расчёта"):
        page.ensure_calculate_button_is_displayed()


@allure.title("TC-03. Проверка выбора грейс-периода 9 месяцев")
def test_select_grace_period_9_months(driver):
    page = CreditCalculatorPage(driver)

    with allure.step("Step 1. Открыть страницу кредита"):
        page.open()

    with allure.step("Step 2. Выбрать грейс-период 9 месяцев"):
        page.select_grace_period(9)

    with allure.step("Step 3. Проверить выбранный вариант"):
        page.ensure_grace_period_selected(9)


@allure.title("TC-04. Проверка выбора грейс-периода 10 месяцев")
def test_select_grace_period_10_months(driver):
    page = CreditCalculatorPage(driver)

    with allure.step("Step 1. Открыть страницу кредита"):
        page.open()

    with allure.step("Step 2. Выбрать грейс-период 10 месяцев"):
        page.select_grace_period(10)

    with allure.step("Step 3. Проверить выбранный вариант"):
        page.ensure_grace_period_selected(10)


@allure.title("TC-05. Проверка выбора грейс-периода 11 месяцев")
def test_select_grace_period_11_months(driver):
    page = CreditCalculatorPage(driver)

    with allure.step("Step 1. Открыть страницу кредита"):
        page.open()

    with allure.step("Step 2. Выбрать грейс-период 11 месяцев"):
        page.select_grace_period(11)

    with allure.step("Step 3. Проверить выбранный вариант"):
        page.ensure_grace_period_selected(11)


@pytest.mark.parametrize(
    "grace_period",
    [9, 10, 11],
    ids=["grace-9-months", "grace-10-months", "grace-11-months"],
)
@allure.title("TC-06. Проверка расчёта кредита с грейс-периодом {grace_period} месяцев")
def test_credit_calculation_with_different_grace_periods(driver, grace_period):
    page = CreditCalculatorPage(driver)

    with allure.step("Step 1. Открыть страницу кредита"):
        page.open()

    with allure.step("Step 2. Заполнить обязательные поля калькулятора"):
        page.fill_valid_calculator_data()

    with allure.step(f"Step 3. Выбрать грейс-период {grace_period} месяцев"):
        page.select_grace_period(grace_period)

    with allure.step("Step 4. Нажать кнопку «Получить расчёт»"):
        page.calculate_credit()

    with allure.step("Step 5. Проверить отображение результатов расчёта"):
        page.ensure_calculation_result_is_displayed()

    with allure.step("Step 6. Проверить наличие рассчитанного ежемесячного платежа"):
        page.ensure_monthly_payment_is_displayed()


@allure.title("TC-07. Проверка изменения результатов при изменении параметров кредита")
def test_calculation_result_changes_after_parameters_change(driver):
    page = CreditCalculatorPage(driver)

    with allure.step("Step 1. Открыть страницу кредита"):
        page.open()

    with allure.step("Step 2. Заполнить обязательные поля и выполнить расчёт"):
        page.fill_valid_calculator_data()
        page.select_grace_period(9)
        page.calculate_credit()

    with allure.step("Step 3. Сохранить первоначальные результаты"):
        initial_result = page.get_calculation_result()

    with allure.step("Step 4. Изменить грейс-период на 10 месяцев"):
        page.select_grace_period(10)

    with allure.step("Step 5. Повторно выполнить расчёт"):
        page.calculate_credit()

    with allure.step("Step 6. Получить обновлённые результаты"):
        updated_result = page.get_calculation_result()

    with allure.step("Step 7. Проверить изменение результатов"):
        assert updated_result != initial_result, (
            "Результаты расчёта не изменились после изменения грейс-периода"
        )


@allure.title("TC-08. Проверка повторного расчёта кредита")
def test_credit_calculator_recalculates_after_input_change(driver):
    page = CreditCalculatorPage(driver)

    with allure.step("Step 1. Открыть страницу кредита"):
        page.open()

    with allure.step("Step 2. Заполнить обязательные поля калькулятора"):
        page.fill_valid_calculator_data()

    with allure.step("Step 3. Выполнить первоначальный расчёт"):
        page.calculate_credit()

    with allure.step("Step 4. Сохранить первоначальные результаты"):
        initial_result = page.get_calculation_result()

    with allure.step("Step 5. Изменить один из параметров кредита"):
        page.change_calculator_parameter()

    with allure.step("Step 6. Выполнить повторный расчёт"):
        page.calculate_credit()

    with allure.step("Step 7. Проверить обновление результатов"):
        updated_result = page.get_calculation_result()

        assert updated_result != initial_result, (
            "Результаты не обновились после изменения параметров калькулятора"
        )

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestBasket():
    #функция проверяет наличие кнопки "Корзина" на странице
    def test_is_there_basket(self, browser):
        print('Start test_is_there_basket')
        browser.get(link)

        WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")))
        basket_vis = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
        assert basket_vis, "Кнопка 'Корзина' должна присутствовать на странице"
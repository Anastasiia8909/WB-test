from pages.wb import WBPage


def test_change_country_to_armenia(web_browser):
    """ Make sure it is possible to change the country to Armenia"""
    page = WBPage(web_browser)
    page.change_country.click()
    page.armenia.click()
    assert page.get_current_url() == 'https://am.wildberries.ru/'


def test_change_country_to_belarus(web_browser):
    """ Make sure it is possible to change the country to Belarus"""
    page = WBPage(web_browser)
    page.change_country.click()
    page.belarus.click()
    assert page.get_current_url() == 'https://by.wildberries.ru/'


def test_change_country_to_israel(web_browser):
    """ Make sure it is possible to change the country to Israel"""
    page = WBPage(web_browser)
    page.change_country.click()
    page.israel.click()
    assert page.get_current_url() == 'https://wildberries.co.il/'


def test_change_country_to_kazakhstan(web_browser):
    """ Make sure it is possible to change the country to Kazakhstan"""
    page = WBPage(web_browser)
    page.change_country.click()
    page.kazakhstan.click()
    assert page.get_current_url() == 'https://kz.wildberries.ru/'


def test_change_country_to_kyrgizystan(web_browser):
    """ Make sure it is possible to change the country to Kyrgizystan"""
    page = WBPage(web_browser)
    page.change_country.click()
    page.kyrgizystan.click()
    assert page.get_current_url() == 'https://kg.wildberries.ru/'


def test_change_country_to_uzbekistan(web_browser):
    """ Make sure it is possible to change the country to Uzbekistan"""
    page = WBPage(web_browser)
    page.change_country.click()
    page.uzbekistan.click()
    assert page.get_current_url() == 'https://uz.wildberries.ru/'


def test_free_delivery(web_browser):
    """ Make sure that link redirects to free delivery page """
    page = WBPage(web_browser)
    page.free_delivery.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/besplatnaya-dostavka?desktop=1'


def test_check_work_btn(web_browser):
    """ Make sure that link redirects to employment page """
    page = WBPage(web_browser)
    page.work_in_wildberries_btn.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/trudoustroystvo'


def test_check_sale_btn(web_browser):
    """ Убедитесь, что ссылка перенаправляет на страницу продажи чего-либо """
    page = WBPage(web_browser)
    page.sale_btn.click()
    page.wait_page_loaded()
    assert page.sale_btn.is_visible()


def test_menu_burger_btn(web_browser):
    """ Make sure menu burger btn allows user to open menu """
    page = WBPage(web_browser)
    page.menu_burger.click()
    page.wait_page_loaded()
    assert page.menu_burger.is_visible()


def test_close_menu_burger(web_browser):
    """ Закрытие меню, нажав на крестик """
    page = WBPage(web_browser)
    page.menu_burger.click()
    page.wait_page_loaded()
    page.cross_icon_menu_burger.click()
    assert page.cross_icon_menu_burger.is_visible()


def test_check_address_btn(web_browser):
    """ Make sure it is possible to open page about addresses of  pick points"""
    page = WBPage(web_browser)
    page.adresess_btn.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/besplatnaya-dostavka?desktop=1#terms-delivery'


def test_check_shopping_basket_btn(web_browser):
    """ Make sure it is possible to open shopping basket page"""
    page = WBPage(web_browser)
    page.shopping_basket_btn.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.wildberries.ru/lk/basket'




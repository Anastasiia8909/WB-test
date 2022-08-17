from pages.wb import WBPage


def test_banner_black_friday(web_browser):
    """ Убедитесь, что первый баннер в карусели кликабельный """
    page = WBPage(web_browser)
    page.btn_first_banner.click()
    page.stocks.click()
    page.wait_page_loaded()
    assert page.stocks.is_visible()


def test_banner_diapers(web_browser):
    """ Убедитесь, что второй баннер в карусели кликабельный """
    page = WBPage(web_browser)
    page.btn_second_banner.click()
    page.diapers.click()
    page.wait_page_loaded()
    assert page.diapers.is_visible()


def test_banner_vivienne_sabo(web_browser):
    """ Make sure that third banner in carousel redirects to the right page """
    page = WBPage(web_browser)
    page.btn_third_banner.click()
    page.vivienne_sabo.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.wildberries.ru/promotions/skidki-do-50-na-vivienne-sabo?bid' \
                                     '=1e3a1eca-7cad-4e82-9022-6c6e0b0693ee '


def test_banner_fast_delivery(web_browser):
    """ Make sure that fourth banner in carousel redirects to the right page """
    page = WBPage(web_browser)
    page.btn_fourth_banner.click()
    page.fast_delivery.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Быстрая доставка: Санкт-Петербург'


def test_banner_clothing_stores(web_browser):
    """ Make sure that fifth banner in carousel redirects to the right page """
    page = WBPage(web_browser)
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_fifth_banner.click()
    page.clothing_stores.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Zara, Bershka, OYSHO, Pull and Bear, Stradivarius, Massimo Dutti'


def test_banner_day_of_stocks(web_browser):
    """ Make sure that sixth banner in carousel redirects to the right page """
    page = WBPage(web_browser)
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_sixth_banner.click()
    page.day_of_stocks.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.wildberries.ru/promotions/mebel?sort=popular&cardsize=c516x688&page' \
                                     '=1&bid=0c0e65b0-c52e-48f8-8f21-81fcd1a95daa&bid=85df4c35-9861-47c4-9951' \
                                     '-10ec5bb3d4ab '


def test_banner_stocks_el_equipment(web_browser):
    """ Make sure that seventh banner in carousel redirects to the right page """
    page = WBPage(web_browser)
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_seventh_banner.click()
    page.stocks_el_equipment.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Дни сниженных цен: электроника и техника'


def test_banner_school_uniform(web_browser):
    """ Make sure that eighth banner in carousel redirects to the right page """
    page = WBPage(web_browser)
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_next_slide.click()
    page.btn_eighth_banner.click()
    page.school_uniform.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Школьная форма'


def test_banner_school_supplies(web_browser):
    """ Make sure that nineth school_supplies banner redirects to the right page """
    page = WBPage(web_browser)
    page.school_supplies.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Школьные принадлежности'


def test_banner_childrens_furniture(web_browser):
    """ Make sure that tenth childrens_furniture banner redirects to the right page """
    page = WBPage(web_browser)
    page.childrens_furniture.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.wildberries.ru/promotions/gotovimsya-k-shkole-detskaya-mebel?bid' \
                                     '=c49a4cfb-61c2-4395-ab30-73e7dd50bae8 '


def test_banner_mango(web_browser):
    """ Make sure that eleventh Mango banner redirects to the right page """
    page = WBPage(web_browser)
    page.mango.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Mango'


def test_banner_large_equipment(web_browser):
    """ Make sure that 12th large equipment banner redirects to the right page """
    page = WBPage(web_browser)
    page.large_equipment.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'КБТ'


def test_banner_products(web_browser):
    """ Make sure that 13th large equipment banner redirects to the right page """
    page = WBPage(web_browser)
    page.products.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Любимые продукты'


def test_banner_erichkrause(web_browser):
    """ Make sure that школьные аксессуары  banner redirects to the right page """
    page = WBPage(web_browser)
    page.erichkrause.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Готовимся к школе с ErichKrause'


def test_banner_sokolov(web_browser):
    """ Make sure that sokolov banner redirects to the right page """
    page = WBPage(web_browser)
    # page.scroll_down(900)
    page.sokolov.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.wildberries.ru/promotions/sokolov?sort=newly&cardsize=c516x688&page' \
                                     '=1&discount=50&bid=cae481af-580b-4b0b-af90-f9296f35a807 '


def test_banner_polaris(web_browser):
    """ Make sure that Polaris banner redirects to the right page """
    page = WBPage(web_browser)
    page.scroll_down(900)
    page.polaris.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Polaris'


def test_banner_adidas(web_browser):
    """ Make sure that adidas banner redirects to the right page """
    page = WBPage(web_browser)
    page.scroll_down(900)
    page.adidas.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Готовы к учебе с Adidas'


def test_banner_yrocher(web_browser):
    """ Make sure that Y.Rocher banner redirects to the right page """
    page = WBPage(web_browser)
    page.scroll_down(1200)
    page.wait_page_loaded()
    page.yrocher.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Yves Rocher'


def test_banner_black_decker(web_browser):
    """ Make sure that black decker banner redirects to the right page """
    page = WBPage(web_browser)
    page.scroll_down(1200)
    page.wait_page_loaded()
    page.black_decker.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'Black+Decker'


def test_banner_huggies(web_browser):
    """ Make sure that huggies banner redirects to the right page """
    page = WBPage(web_browser)
    page.scroll_down(1500)
    page.wait_page_loaded()
    page.huggies.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'С заботой о всей семье'


def test_banner_cosmetic(web_browser):
    """ Make sure that cosmetic banner redirects to the right page """
    page = WBPage(web_browser)
    page.scroll_down(1500)
    page.wait_page_loaded()
    page.cosmetic.click()
    page.wait_page_loaded()
    assert page.header_one.get_text() == 'L’Oreal Paris, Garnier'

from pages.wb import WBPage


def test_check_to_make_order(web_browser):
    """Убедитесь, что ссылка перенаправляет на страницу о том, как сделать заказ"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.to_make_order.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/kak-sdelat-zakaz'


def test_payment(web_browser):
    """Убедитесь, что ссылка перенаправляет на страницу о способах оплаты"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.payment.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/sposoby-oplaty'


def test_delivery(web_browser):
    """Make sure that link redirects to page about delivery"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.delivery.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/besplatnaya-dostavka'


def test_refund_of_purchases(web_browser):
    """Убедитесь, что ссылка перенаправляет на страницу о возврате покупок"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.refund_of_purchases.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/vozvrat-tovara'


def test_refunds(web_browser):
    """Make sure that link redirects to page about refunds"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.refunds.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/vozvrat-denezhnyh-sredstv'


def test_sales_rules(web_browser):
    """Убедитесь, что ссылка перенаправляет на страницу о правилах продажи"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.sales_rules.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/pravila-prodazhi'


def test_trading_rules(web_browser):
    """Убедитесь, что ссылка перенаправляет на страницу с правилами торговой платформы"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.trading_rules.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/pravila-polzovaniya-torgovoy-ploshchadkoy'


def test_questions_and_answers(web_browser):
    """Убедитесь, что ссылка перенаправляет на страницу вопросов и ответов"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.questions_and_answers.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/voprosy-i-otvety'


def test_cooperation(web_browser):
    """Make sure that link redirects to cooperation page"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.cooperation.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://www.wildberries.ru/promo/priglashaem-k-sotrudnichestvu'


def test_pickup_point(web_browser):
    """Убедитесь, что ссылка перенаправляет на страницу об открытии пункта самовывоза"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.pickup_point.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://point-promo.wb.ru/'


def test_franchise(web_browser):
    """Make sure that link redirects to franchise page"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.franchise.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://www.wildberries.ru/services/franshizniy-punkt-vydachi'


def test_wb_guru(web_browser):
    """Make sure that link redirects to wb guru page"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.wb_guru.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://guru.wildberries.ru/?utm_source=main_footer'


def test_footer_employment(web_browser):
    """Make sure that link redirects to page about employment"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.footer_employment.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://vsemrabota.ru/appwb'


def test_digital_goods(web_browser):
    """Убедитесь, что ссылка перенаправляет на страницу о цифровых товарах"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.footer_digital_goods.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://digital.wildberries.ru/'


def test_about_us(web_browser):
    """Make sure that link redirects to about us page"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.about_us.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/o-nas'


def test_requisites(web_browser):
    """Убедитесь, что ссылка перенаправляет на страницу реквизитов"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.footer_requisites.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/rekvizity'


def test_press_center(web_browser):
    """Make sure that link redirects to press center page"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.press_center.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/presscenter'


def test_contacts(web_browser):
    """Make sure that link redirects to contacts page"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.contacts.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/kontakty'


def test_footer_bug(web_browser):
    """Make sure that link redirects to bug bounty page"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.footer_bug.click()
    assert page.get_current_url() == 'https://www.wildberries.ru/services/bug-bounty'


def test_wb_tech(web_browser):
    """Убедитесь, что ссылка перенаправляет на страницу о WB.Tech"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.footer_wb_tech.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://t.me/wbdevs'


def test_vk_link(web_browser):
    """Make sure that link redirects to vk """
    page = WBPage(web_browser)
    page.scroll_down()
    page.vk_link.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://vk.com/public9695053'


def test_classmates_link(web_browser):
    """Make sure that link redirects to classmates """
    page = WBPage(web_browser)
    page.scroll_down()
    page.classmates_link.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://ok.ru/wildberries'


def test_youtube_link(web_browser):
    """Make sure that link redirects to YouTube """
    page = WBPage(web_browser)
    page.scroll_down()
    page.youtube_link.click()
    page.wait_page_loaded()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://www.youtube.com/c/wildberries'


def test_telegram_link(web_browser):
    """Make sure that link redirects to telegram """
    page = WBPage(web_browser)
    page.scroll_down()
    page.telegram_link.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://t.me/wildberriesru_official'


def test_google_play_link(web_browser):
    """Make sure that link redirects to google play"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.google_play_link.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://play.google.com/store/apps/details?id=com.wildberries.ru'


def test_app_store_link(web_browser):
    """Make sure that link redirects to app store """
    page = WBPage(web_browser)
    page.scroll_down()
    page.app_store_link.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://apps.apple.com/ru/app/wildberries/id597880187'


def test_app_gallery_link(web_browser):
    """Make sure that link redirects to app gallery"""
    page = WBPage(web_browser)
    page.scroll_down()
    page.app_gallery_link.click()
    page.switch_to_window(window_number=1)
    assert page.get_current_url() == 'https://appgallery.huawei.com/#/app/C101183325'




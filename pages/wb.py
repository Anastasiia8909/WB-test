#!/usr/bin/python3
# -*- encoding=utf8 -*-
import os
from pages.base import WebPage
from pages.elements import Webelement, MWebElements



class WBPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://www.wildberries.ru/"
            super().__init__(web_driver, url)

    # Main search field
    search = Webelement(id='searchInput')

    # Search button
    search_run_button = Webelement(id='applySearchBtn')

    # Названия товаров в результатах поиска
    products_titles = MWebElements(class_name='goods-name')

    # Добавления товара в корзину
    add_to_shopping_cart_btn = Webelement(css_selector='div > button:nth-child(2) > span.hide-mobile')

    # Кнопка для сортировки товаров по цене
    sort_products_by_price = Webelement(partial_link_text='Цене')

    # Цены на товары в результатах поиска
    products_prices = MWebElements(class_name='lower-price')

    # Картинка на товары в результатах поиска
    product_image = MWebElements(css_selector='div.product-card__img-wrap.img-plug.j-thumbnail-wrap > img')

    # Название на товары в результатах поиска
    product_name = MWebElements(xpath='//div[@class="product-card__brand-name"]/span[@class="product-card__brand-name"]')

    # Рейтинг товаров в результатах поиска
    product_rating = MWebElements(css_selector='a > span.product-card__rating.stars-line.star5')

    # Срок доставки товаров в результатах поиска
    product_delivery = MWebElements(xpath='//*[@id="c63386219"]/div[1]/a[1]/p[1]')

    # Button of first banner in carousel
    btn_first_banner = Webelement(xpath='//li[@aria-label="Go to slide 1"]')

    # Button of second banner
    btn_second_banner = Webelement(xpath='//li[@aria-label="Go to slide 2"]')

    # Button of third banner
    btn_third_banner = Webelement(xpath='//li[@aria-label="Go to slide 3"]')

    # Button of fourth banner
    btn_fourth_banner = Webelement(xpath='//li[@aria-label="Go to slide 4"]')

    # Button of fifth banner
    btn_fifth_banner = Webelement(xpath='//li[@aria-label="Go to slide 5"]')

    # Button of sixth banner
    btn_sixth_banner = Webelement(xpath='//li[@aria-label="Go to slide 6"]')

    # Button of seventh banner
    btn_seventh_banner = Webelement(xpath='//li[@aria-label="Go to slide 7"]')

    # Button of eighth banner
    btn_eighth_banner = Webelement(xpath='//li[@aria-label="Go to slide 8"]')

    # Button of ninth banner
    btn_ninth_banner = Webelement(xpath='//li[@aria-label="Go to slide 9"]')

    # Button of tenth banner
    btn_tenth_banner = Webelement(xpath='//li[@aria-label="Go to slide 10"]')

    # Button of eleven banner
    btn_eleven_banner = Webelement(xpath='//li[@aria-label="Go to slide 11"]')

    # Next slide button
    btn_next_slide = Webelement(xpath='//button[@aria-label="Next slide"]')

    # Кнопка предыдущего слайда
    btn_previous_slide = Webelement(xpath='//button[@aria-label="Previous slide"]')

    # Элемент h1
    header_one = Webelement(css_selector='div.catalog-title-wrap > h1')

    # Элемент h1 на странице в корзине
    header_one_basket = Webelement(xpath='//span[@class="navbar-pc__notify"]')


    # Element h1 Joli Brand page
    header_one_joli_brand = Webelement(xpath='//h1[@class="brand-custom-header__name"]')

    # 1 Banner акции
    stocks = Webelement(xpath='//img[@alt="Черная пятница"]')

    # 2 Banner детские памперсы
    diapers = Webelement(xpath='//img[@alt="Трусики для активных малышей"]')

    # 3 Banner  Vivienne Sabo
    barmariska = Webelement(xpath='//img[@alt="Скидки до 50% на Vivienne Sabo"]')

    # 4 Banner fast delivery
    fast_delivery = Webelement(xpath='//img[@alt="Быстрая доставка: Санкт-Петербург"]')

    # 5 Banner  clothing_stores
    clothing_stores = Webelement(xpath='//img[@alt="Zara, Bershka, OYSHO, Pull and Bear, Stradivarius, Massimo Dutti"]')

    # 6 Banner дни сниженных цен
    day_of_stocks = Webelement(xpath='//img[@alt="Дни сниженных цен"]')

    # 7 Banner stocks electrical equipment
    stocks_el_equipment = Webelement(xpath='//img[@alt="Дни сниженных цен: электроника и техника"]')

    # 8 Banner школьная форма
    school_uniform = Webelement(xpath='//img[@alt="Школьная форма"]')

    # 9 Banner Школьные принадлежности
    school_supplies = Webelement(xpath='//img[@alt="Школьные принадлежности"]')

    # 10 Banner Детская мебель
    childrens_furniture = Webelement(xpath='//img[@alt="Детская мебель"]')

    # 11 Banner Mango
    mango = Webelement(xpath='//img[@alt="Mango"]')

    # 12 Banner Большая бытовая техника
    large_equipment = Webelement(xpath='//img[@alt="КБТ"]')

    # 13 Banner products
    products = Webelement(xpath='//img[@alt="Любимые продукты"]')

    # Banner Готовимся к школе с ErichKrause
    erichkrause = Webelement(xpath='//img[@alt="Готовимся к школе с ErichKrause"]')

    # Banner SOKOLOV
    sokolov = Webelement(xpath='//img[@alt="SOKOLOV"]')

    # Banner Polaris
    polaris = Webelement(xpath='//img[@alt="Polaris"]')

    # Banner adidas
    adidas = Webelement(xpath='//img[@alt="Adidas"]')

    # Banner Yves Rocher
    yrocher = Webelement(xpath='//img[@alt="Yves Rocher"]')

    # Banner Black+Decker
    black_decker = Webelement(xpath='//img[@alt="Black+Decker"]')

    # Banner Huggies
    huggies = Webelement(xpath='//img[@class="banner_42d72a8a-8d32-4bcc-996c-89e79647c3a4"]')

    # Banner L’Oreal Paris, Garnier
    cosmetic = Webelement(xpath='//img[@alt="L’Oreal Paris, Garnier"]')

    # Button to change country
    change_country = Webelement(css_selector='li.simple-menu__item.j-b-header-country > span > span:nth-child(1)')

    # Radio bnt Armenia
    armenia = Webelement(css_selector='label:nth-child(3) > span.radio-with-text__decor')

    # Radio bnt Belarus
    belarus = Webelement(css_selector=' label:nth-child(4) > span.radio-with-text__decor')

    # Radio bnt Israel
    israel = Webelement(css_selector=' label:nth-child(5) > span.radio-with-text__decor')

    # Radio bnt Kazakhstan
    kazakhstan = Webelement(css_selector=' label:nth-child(6) > span.radio-with-text__decor')

    # Radio bnt Kyrgizystan
    kyrgizystan = Webelement(css_selector=' label:nth-child(7) > span.radio-with-text__decor')

    # Radio bnt uzbekistan
    uzbekistan = Webelement(css_selector=' label:nth-child(8) > span.radio-with-text__decor')

    # Link to page about sell on wildberries
    sale_btn = Webelement(xpath='//a[@class="simple-menu__link simple-menu__link--sell-on-wb j-wba-header-item"]')

    # Link to page about work in wildberries
    work_in_wildberries_btn = Webelement(link_text='Работа в Wildberries')

    # Burger button
    menu_burger = Webelement(xpath='//button[@data-wba-header-name="Catalog"]')

    # Cross icon for menu burger
    cross_icon_menu_burger = Webelement(xpath='//button[@class="menu-burger__close j-close-menu-mobile"]')

    # Link to page about pickup points addresses
    adresess_btn = Webelement(link_text='Адреса')

    # Link to shopping cart page
    shopping_basket_btn = Webelement(xpath='//span[@class="navbar-pc__icon navbar-pc__icon--basket"]')

    # Link to delivery page
    delivery = Webelement(link_text='Доставка')

    # Link to page about how to make order
    to_make_order = Webelement(link_text='Как сделать заказ')

    # Link to page about payment methods
    payment = Webelement(link_text='Способы оплаты')

    # Delivery address (city)
    delivery_address = Webelement(xpath='//span[@data-wba-header-name="DLV_Adress"]')

    # Link to page about free_delivery
    free_delivery = Webelement(link_text='Бесплатная доставка')

    # Link to page about purchase returns
    refund_of_purchases = Webelement(link_text='Возврат товара')

    # Link to page about refunds
    refunds = Webelement(link_text='Возврат денежных средств')

    # Link to selling rules page
    sales_rules = Webelement(link_text='Правила продажи')

    # Link to page about rules trading platform
    trading_rules = Webelement(link_text='Правила пользования торговой площадкой')

    # Link to questions and answers page
    questions_and_answers = Webelement(link_text='Вопросы и ответы')

    # Link to carriers page
    cooperation = Webelement(link_text='Перевозчикам')

    # Link to page about opening pickup point
    pickup_point = Webelement(link_text='Партнерский пункт выдачи')

    # Link to page about franchise
    franchise = Webelement(link_text='Франшизный пункт выдачи')

    # Link to wb guru page
    wb_guru = Webelement(link_text='WB Guru')

    # Link to employment page
    footer_employment = Webelement(link_text='Трудоустройство')

    # Link to digital goods page
    footer_digital_goods = Webelement(link_text='Цифровые товары')

    # Link to about us page
    about_us = Webelement(link_text='О нас')

    # Link to about us page
    footer_requisites = Webelement(link_text='Реквизиты')

    # Link to press center page
    press_center = Webelement(link_text='Пресс-центр')

    # Link to contacts page
    contacts = Webelement(link_text='Контакты')

    # Link to bug bounty page
    footer_bug = Webelement(link_text='Bug Bounty')

    # Link to bug WB.Tech page
    footer_wb_tech = Webelement(link_text='WB.Tech')

    # VK link
    vk_link = Webelement(link_text='Вконтакте')

    # Classmates link
    classmates_link = Webelement(link_text='Одноклассники')

    # Youtube link
    youtube_link = Webelement(xpath='//a[@class="icon-yt"]')

    # Telegram link
    telegram_link = Webelement(link_text='Телеграм')

    # Google play link
    google_play_link = Webelement(class_name='google-play')

    # App store link
    app_store_link = Webelement(class_name='app-store')

    # App gallery link
    app_gallery_link = Webelement(class_name='app-gallery')

    # Button that allows users to add goods to shopping card
    go_to_shopping_cart = Webelement(link_text='В корзине')

    # First item in search results
    first_item_in_search_results = Webelement(css_selector='div:nth-of-type(2) > img')

    # Basket element (test_smoke_w)
    on_to_shopping_cart = Webelement(link_text='Перейти в корзину')



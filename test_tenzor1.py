from pages.main_page import MainPage

def test_category_search_check(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    #page.link_picture_click()
    #page.link_check_picture_click()
    page.category_search_check()
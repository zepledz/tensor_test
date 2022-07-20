from selenium import webdriver
from.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def should_be_login_link(self):
        assert self.is_element_present(By.ID, "text")

    def search_engine_input(self):
        self.browser.find_element(By.ID, "text").send_keys('Тензор')

    def examination_of_suggest(self):
        self.browser.find_element(By.ID, "text").send_keys('Тензор')
        assert self.is_element_present(By.CSS_SELECTOR, "ul.mini-suggest__popup-content")

    def results_table(self):
        self.browser.find_element(By.ID, "text").send_keys('Тензор\n')
        assert self.is_element_present(By.ID, "search-result")

    def check_link(self):
        self.browser.find_element(By.ID, "text").send_keys('Тензор\n')
        l = self.browser.find_element(By.XPATH, "//a[@href='https://tensor.ru/']/child::b").text
        k = self.browser.find_element(By.XPATH, "//li[@data-cid='0']").get_attribute('data-cid')
        assert l == "tensor.ru" and k == "0"

    #def check_link_picture(self):
        #assert self.is_element_present(By.XPATH,"//a[@href='https://yandex.ru/images/?utm_source=main_stripe_big']")

        #Проверяем, что ссылка "Картинки" существует

    #def link_picture_click(self):
        #link = self.browser.find_element(By.XPATH, "//a[@href='https://yandex.ru/images/?utm_source=main_stripe_big']").get_attribute('href')
        #self.browser.get(link)
        #Кликаем на ссылку "Картинки"

    #def link_check_picture_click(self):
        #assert self.browser.current_url == 'https://yandex.ru/images/?utm_source=main_stripe_big' or self.browser.current_url == 'https://yandex.ru/images/'
        #Проверяем, что перешли куда нужно

    #def link_click(self):
        #href_first_picture = self.browser.find_element(By.XPATH, "//div[@class='PopularRequestList-Item PopularRequestList-Item_pos_0']/child::a").get_attribute('href')
        #self.browser.get(href_first_picture)
        #Открываем первую категорию картинок

    def category_search_check(self):
        assert self.is_element_present(By.XPATH, "//a[@href='https://yandex.ru/images/?utm_source=main_stripe_big']")
        # Проверяем, что ссылка "Картинки" существует

        link_picture_click = self.browser.find_element(By.XPATH, "//a[@href='https://yandex.ru/images/?utm_source=main_stripe_big']").get_attribute('href')
        self.browser.get(link_picture_click)
        #Кликаем на ссылку "Картинки"

        assert self.browser.current_url == 'https://yandex.ru/images/?utm_source=main_stripe_big' or self.browser.current_url == 'https://yandex.ru/images/'
        # Проверяем, что перешли куда в раздел "Картинки"



        data_grid_text_first_picture = self.browser.find_element(By.XPATH,
                                                                 "//div[@class='PopularRequestList-Item PopularRequestList-Item_pos_0']").get_attribute(
            'data-grid-text')
        #Сохраняем в переменную название первой категории

        href_first_picture = self.browser.find_element(By.XPATH,
                                                        "//div[@class='PopularRequestList-Item PopularRequestList-Item_pos_0']/child::a").get_attribute(
            'href')
        self.browser.get(href_first_picture)
        # Вытаскиваем ссылку на данную категорию и открываем ее

        src_link_name = self.browser.find_element(By.XPATH, "//div[contains(@class, 'serp-item_pos_0')]//img").get_attribute('src') #находим src на странице с картинками

        resault_searche_name = self.browser.find_element(By.XPATH, "//input[@class='input__control mini-suggest__input']").get_attribute('value')
        assert data_grid_text_first_picture == resault_searche_name
        #Проверяем что результат в поисковой строке совпадает с названием категории

        href_link_to_first_picture = self.browser.find_element(By.XPATH, "//div[contains(@class, 'serp-item_pos_0')]//a").get_attribute('href')
        self.browser.get(href_link_to_first_picture)
        #Открываем первую картинку
        link_to_first_picture = self.browser.find_element(By.XPATH,
                                                          "//div[@class='MMGallery-Item MMGallery-Item_selected' ]/descendant::div[3]").get_attribute(
            'style')
        assert src_link_name[6:] in link_to_first_picture
        # Проверяем что открылась первая картинка

        self.browser.find_element(By.XPATH, "//div[contains(@class,'CircleButton CircleButton_type_next')]").click()
        # Нажимаем кнопку вперед

        thumb_image = self.browser.find_element(By.XPATH,
                                                "//div[@class='MMGallery-Item MMGallery-Item_selected' ]/descendant::div[3]")
        assert link_to_first_picture != thumb_image
        # Проверяем что картинка сменилась

        self.browser.find_element(By.XPATH, "//div[contains(@class,'CircleButton CircleButton_type_prev')]").click()
        # Нажимаем назад

        assert link_to_first_picture == self.browser.find_element(By.XPATH,
                                                                  "//div[@class='MMGallery-Item MMGallery-Item_selected' ]/descendant::div[3]").get_attribute(
            'style')
        # Проверяем, что картинка осталась до свайпа
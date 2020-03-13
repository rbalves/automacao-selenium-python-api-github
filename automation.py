from selenium import webdriver


class Automation:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.xpath_button_open_modal_project = '//button[@id="btn_open_modal"]'
        self.xpath_input_title_project = '//input[@id="input-titulo"]'
        self.xpath_input_description_project = '//input[@id="input-descricao"]'
        self.xpath_input_created_project = '//input[@id="input-criacao"]'
        self.xpath_input_language_project = '//input[@id="input-linguagem"]'
        self.xpath_button_add_project = '//button[@id="btn_add_projeto"]'

    def get_element(self, xpath):
        return self.browser.find_element_by_xpath(xpath)

    def set_value_element(self, xpath, text):
        element = self.get_element(xpath)
        element.send_keys(text)

    def open_browser(self):
        self.browser.get('https://rbalves.github.io/app-automacao-selenium-api-github/')
        self.browser.maximize_window()

    def click_button(self, xpath):
        button = self.get_element(xpath)
        button.click()

    def set_form_project(self, project):
        self.set_value_element(self.xpath_input_title_project, project['title'])
        self.set_value_element(self.xpath_input_description_project, project['description'])
        self.set_value_element(self.xpath_input_created_project, project['created_at'])
        self.set_value_element(self.xpath_input_language_project, project['language'])

    def add_projects(self, projects):
        self.open_browser()
        for project in projects:
            self.click_button(self.xpath_button_open_modal_project)
            self.set_form_project(project)
            self.click_button(self.xpath_button_add_project)

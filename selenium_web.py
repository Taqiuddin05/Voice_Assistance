from selenium import webdriver
class infow():
    def __init__(self):
        self.driver = webdriver.Chrome() #driver is instance

    def get_info(self,query):
        self.query = query
        self.driver.get(url = "https://wikipedia.org") #opens the link
        search = self.driver.find_element('xpath', '//*[@id="searchInput"]')
        #it triggers search bar in wikipedia page and stores in search variable
        search.click() #clicks the search tab
        search.send_keys(query)
        enter= self.driver.find_element('xpath', '//*[@id="search-form"]/fieldset/button')
        enter.click()













from selenium import webdriver
class music():
    def __init__(self):
        self.driver = webdriver.Chrome() #driver is instance

    def play(self,query):
        self.query = query
        self.driver.get(url = "https://www.youtube.com/results?search_query=" +query)
        # "+query" is cuz the link is always like that
        video = self.driver.find_element('xpath', '//*[@id="video-title"]/yt-formatted-string')
        # above link is the link of title of 1st video in query search
        video.click()






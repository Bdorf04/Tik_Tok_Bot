#This Part will scrape reddit stories, gather the stories and titles into arrays, and return them
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup 

import requests
import time


#working on opening and screenshoting things and them Ima throw them on top of the video
def get_stories(url, end): #grab stories from reddit url and format them into a list of titles and a list of stories
    stories = []
    driver = webdriver.Chrome()
    
    driver.get(url)
    time.sleep(5)
    driver.execute_script(f"window.scrollBy(0, {5000})") #Scrolls down to load more stories
    time.sleep(5)
    wait=WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".absolute.inset-0")))
    links=[i.get_attribute('href') for i in driver.find_elements(By.CSS_SELECTOR, ".absolute.inset-0") if i.get_attribute('href')!=None] #pull url's from page
    try:
        links=links[2:end+2]
    except:
        print("List Full")
        links=links[2:]

    driver.quit()
    
    for index, link in enumerate(links):
        story=""
        request=requests.get(link)
        soup=BeautifulSoup(request.text, "html.parser")

        title=soup.find(slot="title")
        story+=title.text

        scraped_story=soup.find_all("p", {"class": None}) #parse thru, find all instances of text without any classes (thats how the stories r formatted)
        for i in scraped_story:
            story+=i.text  #turn the array of paragraphs into a full story
        print(story)
        stories.append(story)

    return stories
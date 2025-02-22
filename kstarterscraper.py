from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import os

def Kickstarter_scraping():
    category_id_dict = {
            'cameraequipment': 333,
            'fabricationtools': 335,
            'flight': 336,
            'gadgets': 337,
            'hardware':52,
            'robots': 338,
            'sound': 339, 
            'spaceexploration': 340,
            'wearables': 341
        }
    
    for category_id in category_id_dict.values():
        scraping_website_by_category(category_id)

def scraping_website_by_category(category_id, save_path='Scraped_Projects/successful_projects', pages=200):

    category_id_dict = {
            'cameraequipment': 333,
            'fabricationtools': 335,
            'flight': 336,
            'gadgets': 337,
            'hardware':52, 
            'robots': 338,
            'sound': 339, 
            'spaceexploration': 340,
            'wearables': 341
        }

    # category_name = list(category_id_dict.keys())[list(category_id_dict.values()).index(category_id)]

    # print(f'\n\n{category_name}\n\n')



# Check if the file exists
    file_path = f'{save_path}/successful_id_{category_id}_sorted_by_newest.html'
    if os.path.exists(file_path):
        print(f"File {file_path} exists.")
        return
    
    start_from = 0

    no_of_projects = 0 + start_from*12
    for i in range(pages-start_from):

        options = Options()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
        driver.set_page_load_timeout(180)  # Increase page load timeout

        driver.get(f"https://www.kickstarter.com/discover/advanced?state=successful&category_id={category_id}&sort=newest&seed=2898064&page={i+1+start_from}")

        try:
            element_list = []
            for element in driver.find_elements("css selector", ".js-react-proj-card"):
                element_list.append(element.get_attribute('innerHTML'))
            if len(element_list) == 18:
                element_list = element_list[6:]

            with open(f'{save_path}/successful_id_{category_id}_sorted_by_newest.html', 'a') as f:
                for element in element_list:
                    f.write("%s\n" % element)
            
            no_of_projects += len(element_list)
            print(f"page no. {i+1+start_from}")
            print(f"projects {no_of_projects}")
            if len(element_list) < 12:
                break
        finally:
            driver.quit()

if "__main__" == __name__:
    Kickstarter_scraping()



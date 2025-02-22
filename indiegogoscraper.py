# prompt: using selenium make a soup of thsi website

from bs4 import BeautifulSoup
from selenium import webdriver
import time

def scrape_indiegogo():
    try:
        url = "https://www.indiegogo.com/explore/audio?project_timing=all&product_stage=all&ended_campaigns_included=true&sort=trending"
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox()
        driver.get(url)

        
        start_time = time.time()
        while 1:
            try:
                button = driver.find_element('css selector','.buttonOutline')
                if button:
                    button.click()
                    print("next page")
                    start_time = time.time()
            except:
                print(f'no next page !! try {time.time() - start_time:.1f} seconds')
                if time.time() - start_time > 10:
                    break
            

        soup = BeautifulSoup(driver.page_source, "html.parser")

        
        
        #Print the soup object to inspect
        # print(soup)
        
        # Example: Extract project titles (you'll need to inspect the website's HTML to find the correct selectors)
        # This part will likely need adjustments based on the website's structure.
        project_titles = []
        project_elements = soup.select(".projectDiscoverableCard") # Replace with the actual selector
        for element in project_elements:
          project_titles.append(element.text.strip())
        

        # Print or process the extracted data
        print(len(project_elements))
        driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")

scrape_indiegogo()


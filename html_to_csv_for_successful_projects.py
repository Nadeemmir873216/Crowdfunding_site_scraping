from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup
import csv



def get_data_from_successful_html(path, category_id, save_path='Data/Successful_Projects'):
    """
    This function reads the html file and write the data to a csv file.
    this also go to the website of each project and get the data like last updated and websites.
    NOTE :- only for successful projects
     
    """
    file_name = f"successful_id_{category_id}_sorted_by_newest.html"
    start_from = 1
    with open(path+'/'+file_name, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        projects = soup.find_all('div', class_='project-card-root')
        print(f"\nTotal no. of Projects : {len(projects)}\n")
        projects = projects[start_from-1:]
    
    file_name_wthout_exten = file_name.replace('.html', '')

    with open(f'{save_path}/{file_name_wthout_exten}({start_from}:).csv', 'w', newline='') as csvfile:
        fieldnames = ['serial_no', 'title', 'status', 'fund_perc', 'category', 'place', 'last_updated', 'company', 'websites', 'project_link', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

        writer.writeheader()
        for project in projects:
            serial_no = projects.index(project)+start_from

            title = project.find('a', class_='project-card__title').text.replace(';', ' ')
            company = project.find('p').text.replace('|', ' ')
            link = project.find('a', class_='project-card__title')['href'].split('?')[0]
            end_n_funded = project.find_all('p', class_='type-14')[1].text.replace(';', ' ') if len(project.find_all('p', class_='type-14')) > 1 else 'none'
            status = end_n_funded.split()[0]
            funded_perc = end_n_funded.split()[2] if len(end_n_funded.split()) > 2 else 'none'
            description = project.find('p', class_='type-16').text.replace(';', ' ')
            category = project.find_all('a', class_='kds-chip')[0].text.replace(';', ' ')
            place = project.find_all('a', class_='kds-chip')[1].text.replace(';', ' ')

            last_updated = None
            websites = None
            

            options = Options()
            options.add_argument('-headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--disable-extensions')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

            ### here is the code for getting last updated and websites
            ## if want to fill those options too then uncomment the below code

            # for attempt in range(1, 4):
            #     try:
            #         driver = webdriver.Firefox(options=options)
            #         driver.get(link)
            #         last_updated = driver.find_element("css selector", ".js-adjust-time").text.replace(';', ' ')
            #         break
            #     except Exception as e:
            #         print(f"!! Not able to get data from here !! Attempt {attempt} failed ! {e}")

            # driver.quit()

            # try:
            #     website_link = link+'/creator_bio'
            # except:
            #     website_link = None

            # if website_link!=None:
            #     driver = webdriver.Firefox(options=options)
            #     driver.get(website_link)
            #     websites = [a.get_attribute('href') for a in driver.find_elements("css selector", ".links a")]
            #     driver.quit()

            print(f"Project no. : {serial_no}")
            
            writer.writerow({'serial_no': serial_no,'title':title, 'status':status, 'fund_perc':funded_perc, 'category':category, 'place':place, 'last_updated':last_updated, 'company':company, 'websites':websites, 'project_link':link, 'description':description})
            csvfile.flush()


if __name__ == '__main__':
    get_data_from_successful_html('Scraped_Projects/successful_projects','successful_gadgets_sorted_by_newest.html')




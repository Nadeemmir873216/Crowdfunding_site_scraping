from kstarterscraper import scraping_website_by_category as scrape_html
from html_to_csv_for_successful_projects import get_data_from_successful_html as html_csv
import os

html_save_path = 'FlaskManagerCheck'
csv_save_path = 'FlaskManagerCheck'
category_id = 52
pages=5


if not os.path.exists(html_save_path):
    os.mkdir(html_save_path)
if not os.path.exists(csv_save_path):
    os.mkdir(csv_save_path)

scrape_html(category_id, html_save_path, pages=pages)

html_csv(html_save_path, category_id, csv_save_path)
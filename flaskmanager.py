from kstarterscraper import scraping_website_by_category as scrape_html
from html_to_csv_for_successful_projects import get_data_from_successful_html as html_csv
import os

html_save_path = 'FlaskManagerCheck'
csv_save_path = 'FlaskManagerCheck'
category_id = 52
pages=2


if not os.path.exists(html_save_path):
    os.mkdir(html_save_path)
if not os.path.exists(csv_save_path):
    os.mkdir(csv_save_path)

# scrape_html(category_id, html_save_path, pages=pages)

# html_csv(html_save_path, category_id, csv_save_path)



### Complete Flask Code starts here


from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        print(request.form['category_id'])
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
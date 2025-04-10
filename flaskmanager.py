from kstarterscraper import scraping_website_by_category as scrape_html
from html_to_csv_for_successful_projects import get_data_from_successful_html as html_csv
import os

html_save_path = 'ScrapedData'
csv_save_path = 'ScrapedData'
category_id = 52
pages=2


if not os.path.exists(html_save_path):
    os.mkdir(html_save_path)
if not os.path.exists(csv_save_path):
    os.mkdir(csv_save_path)

### Complete Flask Code starts here


from flask import Flask, render_template , send_from_directory , jsonify
from flask import request

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def scrap():
#     if request.method == 'POST':
#         global category_id,pages
#         pages = int(request.form['pages'])
#         category_id = int(request.form['category-id'])
#         scrape_html(category_id, html_save_path, pages=pages)
#         html_csv(html_save_path, category_id, csv_save_path)
#         print('Scraping Done')
#         result = f'Scraping Done. Category ID: {category_id}, Pages: {pages}'
#         return render_template('index.html', result=result)
#     return render_template('index.html')

SCRAPED_DATA_FOLDER = 'ScrapedData'

@app.route('/ScrapedData/')
def list_files():
    try:
        # files = os.listdir(SCRAPED_DATA_FOLDER)
        files = [f for f in os.listdir(SCRAPED_DATA_FOLDER) if f.endswith('.csv')]

        return jsonify(files)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/ScrapedData/<path:filename>')
def download_file(filename):
    return send_from_directory(SCRAPED_DATA_FOLDER, filename, as_attachment=True)

@app.route('/', methods=['GET', 'POST'])
def scrap():
    if request.method == 'POST':
        global category_id, pages
        pages = int(request.form['pages'])
        category_id = int(request.form['category-id'])
        scrape_html(category_id, html_save_path, pages=pages)
        html_csv(html_save_path, category_id, csv_save_path)
        print('Scraping Done')
        result = f'Scraping Done. Category ID: {category_id}, Pages: {pages}'
        return result
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
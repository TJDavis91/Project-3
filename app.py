from flask import Flask, render_template, jsonify, request
import json
import sqlite3

app = Flask(__name__)
app.static_url_path = '/static'
app.static_folder = 'static'


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')



@app.route('/compare_assets', methods=['GET', 'POST'])
def compare_assets():
    if request.method == 'POST':
        selected_asset = request.form['asset']
        # Process the selected asset (e.g., perform comparisons)
        return f"Selected asset: {selected_asset}"
    return render_template('compare_assets.html')



def get_data_for_asset(asset):
    # Connect to the database
    conn = sqlite3.connect('Currency_db.db')
    cursor = conn.cursor()


    # Execute a query based on the selected asset (Bitcoin, Gold, or Silver)
    cursor.execute("SELECT Month_Year, Closing_Price FROM {} WHERE 1".format(asset))
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    return data




@app.route('/get_data')
def get_data():
    # Load and serve the JSON data
    with open('gold_reserves.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

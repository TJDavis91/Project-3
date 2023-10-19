from flask import Flask, render_template, request, jsonify
import sqlite3
import plotly.graph_objs as go

app = Flask(__name__)

# Define a function to fetch data from the database
def fetch_data_from_db(table_name):
    conn = sqlite3.connect('Currency_db.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT Month_Year, Closing_Price, Volume FROM {table_name}")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_currency = request.form['currency']
        data = fetch_data_from_db(selected_currency)

        # Create a line graph for the selected currency
        figure = go.Figure()
        figure.add_trace(go.Scatter(x=[row[0] for row in data], y=[row[1] for row in data], mode='lines', name='Closing Price'))
        figure.update_layout(title=f'{selected_currency.capitalize()} Closing Price', xaxis_title='Date', yaxis_title='Price')

        return render_template('index.html', currency=selected_currency, graph=figure.to_html())

    return render_template('index.html', currency=None, graph=None)

if __name__ == '__main__':
    app.run(debug=True)

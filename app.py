from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []
    if request.method == 'POST':
        # Fetch JSON data from the S3 link
        api_url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
        try:
            data = requests.get(api_url).json()
        except Exception as e:
            print(f"Error fetching data: {e}")
        
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

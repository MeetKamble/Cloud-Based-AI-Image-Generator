from flask import Flask, request, render_template, url_for
import requests
import os
import uuid

app = Flask(__name__)

# Your API key and endpoint
API_KEY = 'sk-wrYs1WxlVsrvhnEgjz1GRohvnDy0cdnyFAOlXiHgMbneZLyr'
API_URL = 'https://api.stability.ai/v2beta/stable-image/generate/sd3'

# Secret key for sessions
app.secret_key = 'iSpentAlmost30HoursOnThis'

# Ensure the directory for images exists
os.makedirs('static/images', exist_ok=True)

image_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    prompt = None
    if request.method == 'POST':
        # Get the prompt from the form data
        prompt = request.form.get('prompt', 'hello')

        # Generate a unique filename
        unique_filename = f"{uuid.uuid4().hex}.jpeg"
        image_path = f'images/{unique_filename}'

        # Make the API request
        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Accept": "image/*"
            },
            files={
                'prompt': (None, prompt),
                'output_format': (None, 'jpeg')
            }
        )

        if response.status_code == 200:
            with open(f'static/{image_path}', 'wb') as file:
                file.write(response.content)
            # Prepend the new image URL and prompt to the list as a tuple
            image_data.insert(0, (image_path, prompt))
        else:
            return f"API request failed: {response.status_code} - {response.text}"

    return render_template('index.html', image_data=image_data)

@app.route('/download/<path:image_path>')
def download(image_path):
    return render_template('download.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)

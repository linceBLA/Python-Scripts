from flask import Flask, render_template, request, jsonify, redirect
import requests
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_qr', methods=['POST'])
def process_qr():
    data = request.get_json()
    qr_code = data.get('qr_code')

    # Check if the QR code contains a URL
    if qr_code.startswith("http://") or qr_code.startswith("https://"):
        # Call your URL safety check function
        is_safe = check_url_safety(qr_code)

        if is_safe:
            # Return the original URL (not Base64 encoded) to the frontend
            return jsonify({'status': 'success', 'is_safe': True, 'url': qr_code})
        else:
            return jsonify({'status': 'error', 'message': 'URL is malicious'})

    return jsonify({'status': 'error', 'message': 'Not a valid URL'})

def encode_url_for_virustotal(url):
    # Base64 encode the URL and make it URL-safe
    return base64.urlsafe_b64encode(url.encode()).decode().strip("=")

def check_url_safety(url):
    api_key = 'my API Key' # insert your Virus Total API Key
    url_id = encode_url_for_virustotal(url)  # Base64 encode the URL
    endpoint = f'https://www.virustotal.com/api/v3/urls/{url_id}'

    headers = {'x-apikey': api_key}

    try:
        # Make a GET request to the VirusTotal API
        response = requests.get(endpoint, headers=headers)
        print(f"API Response Status Code: {response.status_code}")  # Debugging line
        print(f"API Response JSON: {response.json()}")  # Debugging line

        if response.status_code == 200:
            result = response.json()

            # Check if the URL data is in the response
            if 'data' in result:
                last_analysis_stats = result['data']['attributes'].get('last_analysis_stats', {})
                malicious_count = last_analysis_stats.get('malicious', 0)

                # Return based on the malicious count
                if malicious_count == 0:
                    print("The URL is safe!")
                    # Open the URL in a new tab/window
                    # webbrowser.open(url)
                    return True
                else:
                    print(f"The URL is flagged as malicious ({malicious_count} malicious reports).")
                    return False
            else:
                print("Error: No data returned from VirusTotal.")
                return False
        else:
            print(f"Error: Unable to reach VirusTotal. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error checking URL: {e}")
        return False

@app.route('/redirect/<path:url>')
def redirect_to_url(url):
    return redirect(f'http://{url}')  # Redirect the user to the URL in the browser

def main():
    qr_data = process_qr()

    if not qr_data:
        print("No QR code detected. Exiting...")
        return

    # Check if the QR code contains a URL
    if not qr_data.startswith("http://") and not qr_data.startswith("https://"):
        print("No link. Exiting...")
        return

    url = qr_data
    print(f"Scanned URL: {url}")

    # Check the URL safety
    check_url_safety(url)

if __name__ == '__main__':
    app.run()

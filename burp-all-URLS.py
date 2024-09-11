# script to register a list of URL in Burp
# This script run through a list of URL
# It sends a passive request via the proxy Burp
# As result Burp Suite has all the URLs entered for analysis
# This script needs:
# - list of URL in excel table: All_URLS.xlsx
# header: 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)-HACKERNAME'

import pandas as pd
import requests
from tqdm import tqdm
import urllib3

# Disable SSL certificate verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Read the Excel file and extract URLs from the specified column
df = pd.read_excel('All_URLS.xlsx')
urls = df['URLS'].tolist()

# Configure your Burp Suite proxy settings
burp_proxy = {
    'http': 'http://localhost:8080',
    'https': 'http://localhost:8080'
}

# Additional headers for the requests
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)-HACKERNAME'
}

results = []  # Store the URL and response status code

# Loop through each URL and send a passive request using Burp Suite proxy
for url in tqdm(urls, desc="Processing URLs", unit="URL"):
    try:
        response = requests.get(url, proxies=burp_proxy, headers=headers, verify=False)
        status_code = response.status_code
        results.append({'URL': url, 'Status Code': status_code})
        print(f"URL: {url} - Response Status Code: {status_code}")
    except requests.exceptions.RequestException as e:
        results.append({'URL': url, 'Status Code': 'Exception'})
        print(f"URL: {url} - Exception: {e}")
    
    # Save results to a partial Excel file after processing each URL
    partial_results_df = pd.DataFrame(results)
    partial_results_df.to_excel('partial_result.xlsx', index=False)

# Convert the final results to a DataFrame
results_df = pd.DataFrame(results)

# Save the final results to a new Excel file
results_df.to_excel('final_results.xlsx', index=False)

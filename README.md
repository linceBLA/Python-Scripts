# Python-Scripts

# QR Code Security Scanner using Virus Total

In today’s digital world, QR codes are commonly used but can sometimes lead to malicious websites. To address this security concern, I developed a web-based solution that combines a Python script with an HTML front-end, hosted on PythonAnywhere. This tool allows users to scan QR codes directly through the web page. Upon scanning, the embedded URL is checked for safety using the VirusTotal API, which I access through my personal account. If the URL is deemed safe, it is opened in the browser. However, if the URL is flagged as potentially malicious, the page prevents access and alerts the user, ensuring that the scanned link is verified before being accessed.

You can easily set up your own QR Code Security Scanner by using the Python script and HTML file I’ve provided. To get started, you'll need to:

#### 1. Create a free account on the <a href="https://www.virustotal.com/gui/sign-in">VirusTotal API<a/> and obtain your personal API key.

#### 2. Sign up for a free account on PythonAnywhere and upload my two scripts: QRCODE-Scan_flask_app.py and QRCODE-Scan_index.html.

#### 3. In the QRCODE-Scan_flask_app.py script, make sure to replace the placeholder 'my API key' with your actual VirusTotal API key.

#### 4. Allow your browser to access the camera when prompted for QR code scanning. I recommend setting it to manually request permission each time for added control over security.

The HTML file is quite basic, designed with functionality in mind rather than aesthetics. Feel free to customize and enhance the HTML to suit your needs. My primary goal is to provide a working tool, not to sell or promote it—so make it your own!




# Accelerating the Mapping Phase of Pentesting with Python Scripts

During my work as a pentester, I often have to attack large applications containing thousands of URLs. My goal is always to ensure I cover the maximum possible attack surface without missing any key elements, but time is a critical factor. As most of my contracts come with tight deadlines, I can't afford to spend excessive time on the mapping phase. Accuracy and efficiency are paramount.

To address this, I developed a set of Python scripts to help streamline the mapping process, allowing me to quickly assess and target the right elements. Below are three key scripts that have significantly boosted my workflow and ensured I don’t overlook important vulnerabilities.

### 1. `check-urls-HTTPresponseStatus.py`

This script helps me check if URLs are functional. Given a list of URLs, it checks the response status code and organizes the results in an Excel table. From this table, I can quickly filter out the URLs with a `200 OK` response, allowing me to focus on valid targets for further testing.

### 2. `burp-all-URLS.py`

Burp Suite is one of my go-to tools for identifying vulnerabilities and analyzing URLs. This script simplifies the process of feeding a large list of URLs into Burp. It enables Burp to not only analyze the URLs but also to use its built-in crawler to discover additional URLs within the same domain. This ensures I cover a larger portion of the attack surface without manually opening each URL.

### 3. `Login-extract-cookies-V5.py`

The third script focuses on extracting user cookies from authenticated pages. This is particularly useful for understanding how cookies are created and for crafting new cookies for testing purposes. Additionally, the script allows other tools or scripts to use valid cookies from an active session, streamlining the testing of authenticated areas of the application.

---

These scripts have become invaluable to me, allowing me to be more efficient during the mapping phase without sacrificing thoroughness. By automating repetitive tasks, I can dedicate more time to analyzing potential vulnerabilities and improving the overall security posture of the applications I test.

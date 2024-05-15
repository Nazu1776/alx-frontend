import requests

def validate_html(html_code):
    url = "https://validator.w3.org/nu/?out=json"
    headers = {"Content-Type": "text/html; charset=utf-8"}
    data = html_code.encode("utf-8")
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.ok:
        result = response.json()
        if result["messages"]:
            print("Validation results:")
            for message in result["messages"]:
                print(f"- {message['type']}: {message['message']} (at line {message['lastLine']})")
        else:
            print("No validation errors found.")
    else:
        print("Failed to connect to the W3C Markup Validation Service.")

if __name__ == "__main__":
    # Example HTML code to validate
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Sample Page</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a sample HTML page.</p>
    </body>
    </html>
    """
    
    # Validate the HTML code
    validate_html(html_code)


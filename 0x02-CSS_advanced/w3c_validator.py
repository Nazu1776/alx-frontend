import requests

def validate_html(html_code):
    url = "https://validator.w3.org/nu/"
    headers = {
        'Content-Type': 'text/html; charset=utf-8'
    }
    params = {
        'out': 'json'
    }
    
    response = requests.post(url, headers=headers, params=params, data=html_code.encode('utf-8'))
    results = response.json()

    if 'messages' in results:
        messages = results['messages']
        if not messages:
            print("The HTML is valid!")
        else:
            for message in messages:
                print(f"Type: {message.get('type')}")
                print(f"Message: {message.get('message')}")
                print(f"Extract: {message.get('extract')}")
                print(f"First Line: {message.get('firstLine')}")
                print(f"Last Line: {message.get('lastLine')}")
                print("-" * 40)
    else:
        print("No messages in the response. Something might have gone wrong.")

if __name__ == "__main__":
    html_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>W3C Compliant Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }
        header, nav, main, footer {
            padding: 20px;
            margin: 10px;
        }
        nav ul {
            list-style: none;
            padding: 0;
        }
        nav ul li {
            display: inline;
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to a W3C Compliant Page</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="home">
            <h2>Home</h2>
            <p>This is the home section of the page.</p>
        </section>
        <section id="about">
            <h2>About</h2>
            <p>This section contains information about us.</p>
        </section>
        <section id="contact">
            <h2>Contact</h2>
            <p>Get in touch through our contact section.</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 W3C Compliant Page. All rights reserved.</p>
    </footer>
</body>
</html>"""
    
    validate_html(html_code)


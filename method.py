import requests

# Set the URL for the login page
login_url = "https://www.facebook.com/login"

# Set the URL for the homepage that we want to access after logging in
homepage_url = "https://www.facebook.com/"

# Set the login credentials
payload = {
    "email": "100089169097746",
    "pass": "javed786786xd"
}

# Create a session to retain cookies and perform the login
session = requests.Session()

# Perform the POST request to log in
response = session.post(login_url, data=payload)

# Check if the login was successful
if response.url == homepage_url:
    print("Login successful!")
else:
    print("Login failed :(")

# Access the homepage
response = session.get(homepage_url)

# Print the response text
print(response.text)




import requests
from bs4 import BeautifulSoup

def scrape(url, data):
  # Send a GET request to the target website
  response = requests.get(url)

  # Parse the HTML content of the website
  soup = BeautifulSoup(response.content, "html.parser")

  # Locate the specific data to be extracted
  extracted_data = soup.find(data)

  # Return the extracted data
  return extracted_data

# Get the target website and specific data from the user
url = input("Enter the target website: ")
data = input("Enter the specific data to extract: ")

# Scrape and print the data
scraped_data = scrape(url, data)
print("Extracted data:", scraped_data)


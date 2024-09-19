from bs4 import BeautifulSoup
import requests
import json
import sys

# Set UTF-8 encoding for standard output to handle special characters
sys.stdout.reconfigure(encoding='utf-8')

def fetch_property_data(city_name='Mumbai'):
    url = f'https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=&proptype=Residential-House,Villa&cityName={city_name}'
    response = requests.get(url)
    response.encoding = 'UTF-8'
    
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting land locations
    land_location = [n.get_text().split('in')[-1].strip() for n in soup.find_all(attrs={'class': 'mb-srp__card--title'})]

    # Extracting land areas (sqft)
    land_area = [n.get_text().split(' ')[0].strip() for n in soup.find_all(attrs={'class': 'mb-srp__card__summary--value'}) if 'sqft' in n.get_text()]

    # Extracting land prices and converting them to numeric values
    land_cost = [convert_to_numeric(n.get_text()) for n in soup.find_all(attrs={'class': 'mb-srp__card__price--amount'})]

    # Extracting land descriptions
    land_info = [n.get_text().strip() for n in soup.find_all(attrs={'class': 'mb-srp__card--desc--text'})]

    # Combine the data and return as a list of dictionaries
    data = [{'Location': loc, 'Area (sqft)': area, 'Price': price, 'Description': info} 
            for loc, area, price, info in zip(land_location, land_area, land_cost, land_info)]
    
    return data

# Convert the price text into numeric value
def convert_to_numeric(value):
    value = value.replace('₹', '').strip()
    if 'Cr' in value:
        return float(value.replace('Cr', '').strip()) * 10**7
    elif 'Lac' in value:
        return float(value.replace('Lac', '').strip()) * 10**5
    return 0

# Saving the data into a JSON file
def save_to_json(data, filename='land_data.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")

if __name__ == '__main__':
    city_name = 'Mumbai'  # You can change the city name here
    property_data = fetch_property_data(city_name)
    if property_data:
        save_to_json(property_data)

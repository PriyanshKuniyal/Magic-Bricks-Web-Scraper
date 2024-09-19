Property Scraper
This Python project scrapes property data (location, area, price, and description) from the MagicBricks website for a specified city. The data is stored in a JSON file for later use.

Project Description
The scraper fetches data from MagicBricks for residential properties (houses and villas) in a given city. It retrieves the following information:

Location: The area where the property is located.
Area: The size of the property in square feet.
Price: The price of the property in Indian Rupees, converted to numeric values for ease of analysis.
Description: A brief description of the property.
The scraped data is saved into a JSON file.

How It Works
Makes an HTTP request to the MagicBricks website for a specific city.
Extracts property details like location, area (in sqft), price, and description using BeautifulSoup.
Converts the price into numeric format (handling both crore and lakh values).
Saves the data as a structured JSON file.
Usage
Update the city name in the script (city_name variable) to the city you wish to scrape data for.
Run the script, and the data will be saved in a land_data.json file in the same directory.

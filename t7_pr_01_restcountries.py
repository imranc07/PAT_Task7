''' Q1:
Using the URL https://restcountries.com/v3.1/all write a python program which will do the following:
1.	Use the OOPS concept for the following task.
2.	Use the class constructor for tacking input the above mentioned URL for the task.
3.	Create a Method that will fetch all the JSON data from the URL mentioned above.
4.	Create a Method that will display the name of countries, currencies and currency symbols.
5.	Create a Method that will display those countries which have DOLLAR as its currency.
6.	Create a Method that will display those countries which have EURO as its currency.
'''

import requests

# Using Classes and Methods to perform api testing
class MyJSON:
    def __init__(self, url):
        self.url = url

    # Function to fetch the api status code
    def api_status_code(self):
        # response variable to store the api data
        response = requests.get(self.url)
        return response.status_code
   
    # Function to fetch the entire api data
    def fetch_api_data(self):
        if self.api_status_code() == 200:
            return requests.get(self.url).json()
        else:
            return "ERROR - 404"
       
    # Function to fetch data based on state name
    def fetch_data_by_name(self):
        if self.api_status_code() == 200:
            for data in self.fetch_api_data():
                name = data['name'].get('common', 'N/A')
                currencies = data.get('currencies', {})
                print(f"\nThe name of country is '{name}'",".")
                print(f"The country '{name}' currency and currency symbol are ",currencies,".")

    # Function to display the list of countries with DOLLOR as their currency.
    def country_with_dollor_currency(self):
        if self.api_status_code() == 200:
            # List of countries to store data based on currency symbol
            countries=[country['name']['common']for country in self.fetch_api_data() if 'USD' in country.get('currencies',{})]
            print("\nThe list of countries with DOLLOR as their currency:\n",countries)

    # Function to display the list of countries with EURO as their currency
    def country_with_euro_currency(self):
        if self.api_status_code() == 200:
            # List of countries to store data based on currency symbol
            countries=[country['name']['common']for country in self.fetch_api_data() if 'EUR' in country.get('currencies',{})]
            print("\nThe list of countries with EURO as their currency:\n",countries)

# Restcountries object with HTTP url
restcountries_url = MyJSON("https://restcountries.com/v3.1/all")

# Print API Status Code
print("API Status Code :",restcountries_url.api_status_code())

# Print all the JSON data from the URL
print(restcountries_url.fetch_api_data())

# Print Country names and their currencies
restcountries_url.fetch_data_by_name()

# Print The list of countries with DOLLOR as their currency
restcountries_url.country_with_dollor_currency()

# Print the list of countries with EURO as their currency
restcountries_url.country_with_euro_currency()
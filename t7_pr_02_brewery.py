'''Q2:
Visit the URL https://www.openbrewerydb.org/. Write a Python script which will do the following
1.	List the name of Breweries present in the states of Alaska, Maine and New York.
2.	What is the count of breweries in each of the states mentioned above?
3.	Count the number of types of breweries present in individual cities of the state mentioned above.
4.	Count and list how many breweries have websites in the states of Alaska, Maine and New York.
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
       
    # Function to fetch brewery list based on state name
    def fetch_data_by_state_name(self, state_name):
        if self.api_status_code() == 200:
            brewery_list_in_state = []
            for data in self.fetch_api_data():
                if data['state'] == state_name:
                    brewery_list_in_state.append(data['name'])
            return brewery_list_in_state
                                        
    # Function to count total number of breweries in each state
    def count_total_breweries(self, state_name):
        if self.api_status_code() == 200:
            counter = 0
            for data in self.fetch_api_data():
                if data['state'] == state_name:
                    counter += 1
            return counter
        else:
            return "ERROR 404"

    # Funcion to count total number of brewery type
    def count_total_brewery_type(self):
        if self.api_status_code() == 200:
            brewery_types = {}
            for brewery in self.fetch_api_data():
                brewery_type = brewery.get("brewery_type", "Unknown")
                brewery_types[brewery_type] = brewery_types.get(brewery_type, 0) + 1
            return brewery_types

    # Function to count Breweries with website 
    def count_breweries_with_website(self):
        websites_count = 0
        for brewery in self.fetch_api_data():
            if brewery.get("website_url"):
                websites_count += 1
                print(f"Brewery with website in {brewery['state']} ({brewery['name']}): {brewery['website_url']}")
        return websites_count

    # Function to list Breweries with website 
    def list_breweries_with_website(self):
        website_list = []
        for brewery in self.fetch_api_data():
            if brewery.get("website_url"):
                website_list.append(brewery['website_url'])
        return website_list

# Brewery List Object for Alaska state
breweries_in_alaska = MyJSON("https://api.openbrewerydb.org/v1/breweries?by_state=alaska")

# Brewery List Object for Maine state
breweries_in_maine = MyJSON("https://api.openbrewerydb.org/v1/breweries?by_state=maine")

# Brewery List Object for New York state
breweries_in_new_york = MyJSON("https://api.openbrewerydb.org/v1/breweries?by_state=New%20York")

# Print API status code
print("\nAPI status code: ",breweries_in_alaska.api_status_code())
# Print brewry name in Alaska state
print("\nThe lis of breweries in 'Alaska' state: " ,breweries_in_alaska.fetch_data_by_state_name("Alaska"))
# Print total number of breweries in alaska state
print("\nTotal number of breweries in Alaska State are :", breweries_in_alaska.count_total_breweries("Alaska"))    
# Print The number of types of breweries present in 'Alaska' State
print("\nThe number of types of breweries present in 'Alaska State' : ", breweries_in_alaska.count_total_brewery_type())
# Print Total number of breweries in Alaska State with website
print("\nTotal number of breweries in Alaska State with website : ",breweries_in_alaska.count_breweries_with_website())
# Print List of brewery website in Alaska Sate
print("\nThe list of brewery website in Alaska Sate :",breweries_in_alaska.list_breweries_with_website())

# Print API status code
print("\nAPI status code: ",breweries_in_maine.api_status_code())
# Print brewry name in Maine state
print("\nThe lis of breweries in 'Maine' state: " ,breweries_in_maine.fetch_data_by_state_name("Maine"))
# Print total number of breweries in alaska state
print("\nTotal number of breweries in Maine State are :", breweries_in_maine.count_total_breweries("Maine"))    
# Print The number of types of breweries present in 'Maine' State
print("\nThe number of types of breweries present in 'Maine' state : ", breweries_in_maine.count_total_brewery_type())
# Print Total number of breweries in Maine State with website
print("\nTotal number of breweries in Maine State with website : ",breweries_in_maine.count_breweries_with_website())
# Print List of brewery website in Maine Sate
print("\nThe list of brewery website in Maine Sate :",breweries_in_maine.list_breweries_with_website())

# Print API status code
print("\nAPI status code: ",breweries_in_new_york.api_status_code())
# Print brewry name in New York state
print("\nThe lis of breweries in 'New York' state: " ,breweries_in_new_york.fetch_data_by_state_name("New York"))
# Print total number of breweries in alaska state
print("\nTotal number of breweries in Alaska State are :", breweries_in_new_york.count_total_breweries("New York"))    
# Print The number of types of breweries present in 'New York' state
print("\nThe number of types of breweries present in 'New York' sate : ", breweries_in_new_york.count_total_brewery_type())
# Print Total number of breweries in New York with website
print("\nTotal number of breweries in New York State with website : ",breweries_in_new_york.count_breweries_with_website())
# Print List of brewery website in New York Sate
print("\nThe list of brewery website in New York Sate :",breweries_in_new_york.list_breweries_with_website())
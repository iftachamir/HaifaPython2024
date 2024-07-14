# First input - how many country - city groups
num_of_entries = int(input())

# Build a dictionary of entries
d = dict()
for i in range(num_of_entries):    # Repeat loop num_of_entries times

  # Second input sequence
  current_input = input().split()  # Get country - cities pairings and split to list
  country = current_input[0]
  cities = current_input[1:]
  d[country] = cities              # Enter into dictionary

# Third input - number of queries
num_of_queries = int(input())

# Fourth input sequence - series of queried cities
outout_list = []                   # Empty list to store countries to be listed
for i in range(num_of_queries):
  current_query_city = input()     # City asked about

  # Scan dictionary for city
  for country in d.keys():
    cities_in_country = d[country]
    if current_query_city in cities_in_country:
      outout_list.append(country)

# Output
for country in outout_list:
  print(country)
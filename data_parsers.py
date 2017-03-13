import json
# Raw win percentage data from http://mcubed.net/ncaab/seeds.shtml

# Read in raw data
historical_data = open('raw_records.txt', 'r+')
historical_data = historical_data.read()

# Split based on seed
historical_data = historical_data.split('\n\n')

# Set up dictionary with win percentages
historical_data_dict = {}

# Add empty nested dictionaries
for index, row in enumerate(historical_data):
	historical_data_dict[index + 1] = {}

# Further parse data
historical_data = [h.split('\n') for h in historical_data]

# Data cleaning
historical_data[0].insert(0, '')

for index, row in enumerate(historical_data):
	for idx, rw in enumerate(row):
		# Don't include the first two lines of the list
		if idx == 0 or idx == 1:
			pass
		# Add win history to hash
		else:
			historical_data_dict[index + 1][idx - 1] = rw.split(' ')[-1]

print(json.dumps(historical_data_dict))
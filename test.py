import json
import sys

# print("test.py running...")

# json_string = '{"first_name": "Tom", "last_name":"Hazledine"}'

# print json_string

newstring = 'Tom'

for line in sys.stdin:
	print line
	# parsedLine = json.loads(line)
	# print parsedLine


# Test JSON parsing:
# json_string = '{"first_name": "Tom", "last_name":"Hazledine"}'
# parsed_json = json.loads(json_string)
# # print(parsed_json['first_name'])

# # Test JSON output:
# data = {
#     'first_name': newstring,
#     'second_name': 'Hazledine',
#     'titles': ['Tinkerer', 'Developer'],
# }

# data['middle_name'] = 'Frederick';

# print(json.dumps(data))

# print('test.py finished.')
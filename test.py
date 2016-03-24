import json

newstring = 'Tom'

data = {
    'first_name': newstring,
    'last_name': 'Hazledine',
    'titles': ['Tinkerer', 'Developer'],
}

data['middle_name'] = 'Frederick';

print(json.dumps(data))
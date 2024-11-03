import json

# followers
with open('./data/followers_1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

followers = []
for item in data:
    for sub_item in item["string_list_data"]:
        followers.append(sub_item["value"])

# following
with open('./data/following.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

following = []
for item in data["relationships_following"]:
    for sub_item in item["string_list_data"]:
        following.append(sub_item["value"])

# main
goodpeople = []

for user in following:
    if user in followers:
        goodpeople.append(user)

for user in following:
    if user not in goodpeople:
        print(f'https://www.instagram.com/{user}')

import requests
import json
#
# post_code_req = requests.get("https://api.postcodes.io/postcodes/pr85db")
#
# print(post_code_req.status_code)
# print(post_code_req.headers)
# print(post_code_req.content)
# print(type(post_code_req.content))
# print(post_code_req.json())  # unwraps, so no 'b' wrapper. 'b' stands for 'bytes'. From request library
# print(type(post_code_req.json()))

# post request to postcodes.io

json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

# print(post_multi_req.json())

print(json.dumps(post_multi_req.json(), indent=2))

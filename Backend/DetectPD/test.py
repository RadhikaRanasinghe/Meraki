import requests

BASE = "http://127.0.0.1:5000/"

my_img = {'image': open('test.png', 'rb')}
payload = {'age': 70, 'gender': 1, 'handedness': 1}
r = requests.post(BASE + 'create_user', files=my_img, data=payload)

# print(my_img['image'])

# convert server response into JSON format.
print(r.json())

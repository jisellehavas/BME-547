import requests

# r = requests.get("https://api.github.com/repos/jisellehavas/BME-547/branches")
# print(r)
# print(type(r))
# print(r.text)
# if r.status_code == 200:
#     answer = r.json()
#     print(type(answer))
#     for branch in answer:
#         print(branch["name"])
# else:
#     print("Bad request: {}".format(r.text))

# output_info = {"name": "Jiselle Havas",
#                "net_id": "jh709",
#                "e-mail": "jiselle.havas@duke.edu"}

# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
#                   json=output_info)
# print(r)
# print(r.text)
# r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
# print(r.text)

info = {"user": "ml522", "message": "Hi friend!"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=info)
q = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/ml522")
print(q.text)
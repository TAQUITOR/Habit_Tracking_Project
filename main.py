import requests
from datetime import datetime

# PIXELA DOCUMENTATION https://docs.pixe.la/

USERNAME = "theusername"
TOKEN = "thepassword"
GRAPH_ID = "idgraph123"

pixela_endpoint = "https://pixe.la/v1/users"
# ------------- Create your user account ---------------------- #
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url= pixela_endpoint,json=user_parameters)
# print(response.text)

# ------------- Create a graph definition ---------------------- #
pixela_endpoint_graphs = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "gra1944",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=pixela_endpoint_graphs, json=graph_config, headers=headers)
# print(response.text)
# ------------- Post value to the graph ---------------------- #

today = datetime.now()
pixela_endpoint_postvalue = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
value_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today"),
}

response = requests.post(url=pixela_endpoint_postvalue, json=value_config, headers=headers)
print(response.text)

# ------------- Update a pixel ---------------------- #

pixel_end_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_config = {
    "quantity": "125"
}
# response = requests.put(url=pixel_end_update, json=update_config, headers=headers)
# print(response.text)

# ------------- Delete a pixel ---------------------- #
pixel_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=pixel_delete, headers=headers)
# print(response.text)




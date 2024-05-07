import http.client
import json

conn = http.client.HTTPSConnection("reqres.in")
conn.request("GET", "/api/users")
res = conn.getresponse()
users_data = json.loads(res.read().decode("utf-8"))
print("Users data:")
print(users_data)

new_user = {
    "name": "Ignacio",
    "job": "Profesor"
}
headers = {'Content-type': 'application/json'}
conn.request("POST", "/api/users", json.dumps(new_user), headers)
res = conn.getresponse()
created_user = json.loads(res.read().decode("utf-8"))
print("\nCreated user:")
print(created_user)

update_data = {
    "residence": "zion"
}
user_id = 2
conn.request("PUT", f"/api/users/{user_id}", json.dumps(update_data), headers)
res = conn.getresponse()
updated_user = json.loads(res.read().decode("utf-8"))
print("\nUpdated user:")
print(updated_user)

user_id = 6
conn.request("DELETE", f"/api/users/{user_id}")
res = conn.getresponse()
print("\nResponse code for user deletion:")
print(res.status)
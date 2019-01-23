import requests
import json

def invokeapi(method, uri, headers, body, payload):

    if method.upper() == "GET":
        response = requests.get(uri, headers=headers, params=payload)

    elif method.upper() == "POST":
        response = requests.post(uri, headers=headers, data=json.dumps(body))

    elif method.upper() == "PUT":
        response = requests.put(uri, headers=headers, data=body)

    elif method.upper() == "PATCH":
        response = requests.patch(uri, headers=headers, data=(body))

    elif method.upper() == "DELETE":
        response = requests.delete(uri, headers=headers)

    else:
        print("please enter a valid method")

    return response
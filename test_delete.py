import json
import string
from playwright.sync_api import sync_playwright
import random


def test_response(playwright: sync_playwright):
    email = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    
    with open('./JsonFile/CreateUser.json', 'r') as read_file:
        data = json.load(read_file)
        data['email'] = "fati.gh"+email+"1@15ce.com"

    context = playwright.request.new_context(base_url="https://gorest.co.in")
    response_post = context.post(url="/public/v2/users", headers={
        "Authorization": "Bearer 86152c35d129b4285010db11d60a7377e34d201c4092054db0124d16a9ed2fd2"
    }, data=data)

    assert response_post.status == 201
    res = response_post.json()
    user_id = res.get("id")
    assert res.get("email") == "fati.gh"+email+"1@15ce.com"

    response_delete = context.delete(url="/public/v2/users/"+str(user_id), headers={
        "Authorization": "Bearer 86152c35d129b4285010db11d60a7377e34d201c4092054db0124d16a9ed2fd2"
    })

    assert response_delete.status == 204

    response_get = context.get(url="/public/v2/users/"+str(user_id), headers={
        "Authorization": "Bearer 86152c35d129b4285010db11d60a7377e34d201c4092054db0124d16a9ed2fd2"
    })

    assert response_get.status == 404
    assert response_get.json()["message"] == "Resource not found"

import json
import string
from playwright.sync_api import sync_playwright
import random


def test_response(playwright: sync_playwright):

    with open('./JsonFile/CreateUser.json', 'r') as read_file:
        data = json.load(read_file)

    context = playwright.request.new_context(base_url="https://gorest.co.in")
    response = context.patch(url="/public/v2/users/6914330", headers={
        "Authorization": "Bearer 86152c35d129b4285010db11d60a7377e34d201c4092054db0124d16a9ed2fd2"
    }, data=data)

    print(response.body())

    assert response.status == 200

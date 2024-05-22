import json
import string
from playwright.sync_api import sync_playwright
import random


def test_response(playwright: sync_playwright):
    files = [
        ('fileName', ('test.docx',open('./JsonFile/test.docx','rb'),
        'application/octet-stream'))
    ]
    context = playwright.request.new_context(base_url="http://developer.shopclues.com")
    response = context.post(url="/api/v1/upload", headers={
        "Authorization": "Bearer 86152c35d129b4285010db11d60a7377e34d201c4092054db0124d16a9ed2fd2"
    })

    assert response.status == 200
    assert response.json()["message"] == "UnAuthorised Access"

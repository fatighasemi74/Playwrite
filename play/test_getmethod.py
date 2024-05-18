from playwright.sync_api import sync_playwright


def test_get(playwright: sync_playwright):
    context = playwright.request.new_context()
    response = context.get(url="https://gorest.co.in/public/v2/users/2934570", headers={
        "Authorization": "Bearer 86152c35d129b4285010db11d60a7377e34d201c4092054db0124d16a9ed2fd2"
    })
    res = response.json()

    assert response.status == 200
    assert response.status_text == 'OK'
    assert response.json()["name"] == "Aamod Joshi"
    assert res.get("name") == "Aamod Joshi"
    assert response.headers["content-type"] == "application/json; charset=utf-8"
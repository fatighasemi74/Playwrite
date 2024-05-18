from playwright.sync_api import sync_playwright


def test_response(playwright: sync_playwright):
    query_params = {
        "page": "1"
    }
    context = playwright.request.new_context(base_url="https://gorest.co.in")
    response = context.get(url="/public/v2/users", params=query_params, headers={
        "Authorization": "Bearer 86152c35d129b4285010db11d60a7377e34d201c4092054db0124d16a9ed2fd2"
    })
    res = response.json()

    assert response.status == 200
    assert response.status_text == 'OK'
    # assert res[0].get("name") == "Suresh Nambeesan"

    size = len(res)
    print(size)
    print(res)

    for i in range(0, size+1):
        if res[i].get("name") == "Goswami Verma" :
            assert res[i].get("name") == "Goswami Verma"
            break

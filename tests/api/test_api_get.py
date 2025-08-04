
def test_api_get_example(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization":"Bearer YOUR_API_KEY",
            "x-api-key":"reqres-free-v1"
        }
    )
    response = request.get("https://reqres.in/api/users?page=2")
    assert response.status == 200
    # assert response.json()["id"] == 1
    jeson_data = response.json()
    print(jeson_data)
    request.dispose()  # Clean up the request context after the test


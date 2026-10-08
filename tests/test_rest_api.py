import requests

# Testing random activity
def test_get_random_activity(base_url):
    url = f"{base_url}/random"
    response = requests.get(url)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()
    assert isinstance(data["activity"], str)
    assert not isinstance(data["availability"], str)
    assert isinstance(data["type"], str)
    assert isinstance(data["participants"], int)
    assert isinstance(data["price"], float)
    assert isinstance(data["accessibility"], str)
    assert isinstance(data["kidFriendly"], bool)
    assert isinstance(data["link"], str)
    assert isinstance(data["key"], str)


# Testing filter by type
def test_filter_by_type(base_url):
    typeFilter = ['education', 'recreational', 'social', 'charity', 'cooking', 'relaxation', 'busywork']

    for filter in typeFilter:
        url = f"{base_url}/filter?type={filter}"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"


# Testing filter by participiant
def test_filter_by_participiant(base_url):
    participantsFilter = [1, 2, 3, 4, 5, 6, 8]

    for participant in participantsFilter:
        url = f"{base_url}/filter?participiant={participant}"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"


# Testing activity by key if found
def test_activity_by_key_found(base_url):
    url = f"{base_url}/activity/3943506"
    response = requests.get(url)
    assert response.status_code == 200


# Testing activity by key if not found
def test_activity_by_key_not_found(base_url):
    url = f"{base_url}/activity/1"
    response = requests.get(url)
    assert response.status_code == 404
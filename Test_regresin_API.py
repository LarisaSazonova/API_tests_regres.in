import requests
import pytest
from email_validate import validate


@pytest.fixture
def expected_result():
    return {
        "page": 2,
        "per_page": 6,
        "total": 12,
        "total_pages": 2,
        "data": [
            {
                "id": 7,
                "email": "michael.lawson@reqres.in",
                "first_name": "Michael",
                "last_name": "Lawson",
                "avatar": "https://reqres.in/img/faces/7-image.jpg"
            },
            {
                "id": 8,
                "email": "lindsay.ferguson@reqres.in",
                "first_name": "Lindsay",
                "last_name": "Ferguson",
                "avatar": "https://reqres.in/img/faces/8-image.jpg"
            },
            {
                "id": 9,
                "email": "tobias.funke@reqres.in",
                "first_name": "Tobias",
                "last_name": "Funke",
                "avatar": "https://reqres.in/img/faces/9-image.jpg"
            },
            {
                "id": 10,
                "email": "byron.fields@reqres.in",
                "first_name": "Byron",
                "last_name": "Fields",
                "avatar": "https://reqres.in/img/faces/10-image.jpg"
            },
            {
                "id": 11,
                "email": "george.edwards@reqres.in",
                "first_name": "George",
                "last_name": "Edwards",
                "avatar": "https://reqres.in/img/faces/11-image.jpg"
            },
            {
                "id": 12,
                "email": "rachel.howell@reqres.in",
                "first_name": "Rachel",
                "last_name": "Howell",
                "avatar": "https://reqres.in/img/faces/12-image.jpg"
            }
        ],
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }


request_body = {
    "name": "morpheus",
    "job": "leader"
}


def test_get_list_of_users_to_have_status_code_200():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200, "Status code is not 200"


def test_get_list_of_users_to_have_correct_response_body(expected_result):
    response = requests.get("https://reqres.in/api/users?page=2")
    response_body = response.json()
    assert response_body == expected_result, "Response body is not as expected according spec"


def test_list_of_users_to_have_valide_emails():
    response = requests.get("https://reqres.in/api/users?page=2")
    response_body = response.json()

    for user in response_body["data"]:
        print(user["email"])
        assert validate(user["email"], check_smtp=False)


def test_created_user_is_in_response_body():
    response = requests.post("https://reqres.in/api/users", data=request_body)
    response_body = response.json()
    assert response_body.get("name") == "morpheus" and response_body.get("job") == "leader"

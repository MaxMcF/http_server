import requests as req


def test_server_get_home_route_status_200():
    response = req.get('http://127.0.0.1:5000/')
    assert response.status_code == 200


def test_server_get_home_route_response_content():
    response = req.get('http://127.0.0.1:5000/cow')
    assert '<html><body><h1>Cow!</h1></body></html>' == str(response.text)


# def test_server_get_home_route_response_cowpy():
#     response = req.get('http://127.0.0.1:5000/cowpy')
#     assert '<html><body><h1>Cow!</h1></body></html>' == str(response.text)


def test_server_get_home_route_response_beavis():
    response = req.get('http://127.0.0.1:5000/cow?msg=hello')
    assert '<html><body><h1>Beavis!</h1></body></html>' == str(response.text)

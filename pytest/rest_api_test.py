import requests  # need to install in settings
import json
import pytest


class RestObject:
    def __init__(self, d):
        self.__dict__ = d

    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result


def test_rest_api_get_coupon():
    resp = requests.get("http://localhost:8080/coupon/1")
    d = json.loads(resp.content)
    t = RestObject(d)
    assert t.title == 'Caffe'
    assert t.id == 1


def test_rest_api_post_coupon():
    resp = requests.post("http://localhost:8080/coupon",
                         data='{"id": 4, "title": "shwarma"}',
                         headers={"Content-type": "application/json"});
    print(f'Status code = {resp.status_code}');


def test_rest_api_update_coupon():
    resp = requests.put("http://localhost:8080/coupon/4",
                        data='{"id": 4, "title": "shwarmama"}',
                        headers={"Content-type": "application/json"});
    print(f'Status code = {resp.status_code}');


def test_rest_api_del_coupon():
    resp = requests.delete("http://localhost:8080/coupon/4")
    print(f'Status code = {resp.status_code}');


def test_rest_api_get_coupon4():
    resp = requests.get("http://localhost:8080/coupon/4")
    assert resp.content.decode('utf8').replace("'", '"') == ''

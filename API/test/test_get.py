import pytest
import requests
import API.setting.config as config
from assertpy import assert_that

global req
baseUrl = config.BASE_URL
get_user = config.get_user

def test_get1():
    req = requests.get(baseUrl + get_user, headers=config.headers)
    verify_status_code = req.status_code
    verify_json = req.json()

    assert_that(verify_status_code).is_equal_to(200)
    assert_that(verify_json).contains_key("page", "per_page", "total", "total_pages", "data")
    assert_that(verify_json["data"][0]).contains_key("id","email", "first_name", "last_name","avatar")
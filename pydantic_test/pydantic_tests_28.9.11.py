from pydantic import BaseModel
import pytest
import requests
import datetime as dt


class AccessTokenRequest(BaseModel):
    token: str

class Booking(BaseModel):
    firstname: str | None
    lastname: str | None
    checkin: dt.date | None
    checkout: dt.date | None

def test_token_not_null():
    request = {
        "token": "token111"
    }
    AccessTokenRequest(**request)

def test_valid_response():
    response = {
        "firstname": "Ivan", "lastname": "Ivanov", "checkin": dt.date(2019,6,1), "checkout": dt.date(2020,6,1)
    }
    Booking(**response)

def test_token_is_empty():
    request = {}
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)

def test_token_format():
    request = {
        "token": 111
    }
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)

def test_none_firstname_response():
    response = {
        "firstname": None, "lastname": "Ivanov", "checkin": dt.date(2019,6,1), "checkout": dt.date(2020,6,1)
    }
    Booking(**response)

def test_format_date_response():
    response = {
        "firstname": None, "lastname": "Ivanov", "checkin": "2019-06-01", "checkout": dt.date(2020,6,1)
    }
    with pytest.raises(ValueError):
        Booking(**response)

def test_format_lastname_response():
    response = {
        "firstname": "Ivan", "lastname": 111, "checkin": dt.date(2019,6,1), "checkout": dt.date(2020,6,1)
    }
    with pytest.raises(ValueError):
        Booking(**response)

def test_empty_responce():
    response = {}
    with pytest.raises(ValueError):
        Booking(**response)

def test_valid_response_two_bookings():
    response =[{
        "firstname": "Ivan", "lastname": "Ivanov", "checkin": dt.date(2019,6,1), "checkout": dt.date(2020,6,1)
    },
    {"firstname": "Sergey", "lastname": "Smirnov", "checkin": dt.date(2019,6,1), "checkout": dt.date(2020,6,1)}]
    book = [Booking(**booking) for booking in response]
    assert len(book) == 2

def test_invalid_response():
    response = {
        "attr1": "val1", "attr2": "val2"
    }
    with pytest.raises(ValueError):
        Booking(**response)









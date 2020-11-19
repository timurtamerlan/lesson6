import pytest

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.data == b"hello github"


def test_v2(app, client):
    res = client.get('/v2')
    assert res.status_code == 200
    assert res.data == b"Second action"

def test_brichev(app, client):
    res = client.get('/brichev')
    assert res.status_code == 200
    assert res.data == b"Hello from CI with GitHub Actions by Brichev"
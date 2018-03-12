import pytest
from selenium import webdriver
from models.facebook import Facebook
import os, json


@pytest.fixture()
def config():
    filename = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(filename)as f:
        return json.load(f)


@pytest.fixture()
def init(config):
    wd = webdriver.Chrome()
    app = Facebook(base_url=config["base_url"], wd=wd)
    yield app
    #app.close()

@pytest.fixture()
def login(init, config):
    init.login_acc(username=config["username"], password=config["password"])
    yield

import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.credence.in")
    return driver


def pytest_metadata(metadata):
    metadata["class"] = "Credence"
    metadata["batch"] = "CT14"


@pytest.fixture(params=[
("Credencetest@test.com","Credence@123"),
    ("Credencetest@test.com1","Credence@123"),
    ("Credencetest@test.com","Credence@1231"),
    ("Credencetest@test.com1","Credence@1231")
])
def getdataforlogin(request):
    return request.param
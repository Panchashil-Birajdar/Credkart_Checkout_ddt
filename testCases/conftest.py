

import pytest
from selenium   import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    elif browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://automation.credence.in/shop")
    return driver


def pytest_metadata(metadata):
    metadata['Class'] = 'Credence'
    metadata['Batch'] = '#CT14'
    metadata['URL'] = 'https://automation.credence.in/shop'
    metadata.pop('Platform',None)

@pytest.fixture(params=[
    ("Credenceppb3@test.com","Credence@123"),
    ("Credenceppb3@test.com","Credence@1234"),
    ("Credenceppb3@test1.com","Credence@123"),
    ("Credenceppb3@test1.com","Credence@1234")
])
def GetDataForLogin(request):
    return request.param


# pytest -v --html=HTMLReports/myreport.html --alluredir="D:\Credence\Assignments\My Assignments\Final Revision\CredKart_Pytest_Project\AllureReports" -n=2









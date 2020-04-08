import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None, help="Choose language: ru, en, fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    language = request.config.getoption("language")

    if language == "fr":
        print("\nopen website on french locale for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    elif language == "es":
        print("\nopen website on english locale for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    elif language == "ru":
        print("\nopen website on russion locale for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    #if browser_name == "chrome":
    #    print("\nstart chrome browser for test..")
    #    browser = webdriver.Chrome()

    #elif browser_name == "firefox":
    #    print("\nstart firefox browser for test..")
    #    browser = webdriver.Firefox()
        
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

import pytest
import json

import selenium.webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def browser(config):

    # webdriver per-browser init
    if config['browser'] == 'Firefox': # TODO: firefox not working yet, executable not found
        opts = selenium.webdriver.FirefoxOptions()
        b = selenium.webdriver.Firefox(options=opts)
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('--log-level=1') # don't care about FLoC related logging
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception("Browser {} is not supported", config["browser"])

    # clunky wait
    b.implicitly_wait(10)

    # return webdriver
    yield b

    # cleanup
    b.quit()


@pytest.fixture
def config(scope='session'):

    with open('config.json') as config_file:
        config = json.load(config_file)

    # sanity check browser specified in config.json
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config
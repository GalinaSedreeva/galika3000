def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru")

    parser.addoption("--status_code", default=200)


@pytest.fixture
def get_status(request):
    return request.config.getoption("--status_code")

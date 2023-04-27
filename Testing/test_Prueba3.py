import pytest

@pytest.fixture()
def fixture_code():
    print("This is a fixture executed before test case")
    print("-------------------------------------------")
    yield
    print("Execution after test cases")
    print("-------------------------------------------")


@pytest.mark.Smoke
def test_login(fixture_code):
    print("smoke")
    print("smoke test")


@pytest.mark.Sanity
def test_invalid_credentials(fixture_code):
    print("Sanity")
    print("Sanity test")

# Print statement output display on console -s
# Verbose mode display test cases name with status -v

# Omitir test cases con condicion y añadir una razon
# import pytest
# @pytest.mark.skip over the test case that we want to skip
# a=100, a= 101
# @pytest.mark.skipif(a>100, reason="Skipping as this functionality is not working, developer will fix it in new build")

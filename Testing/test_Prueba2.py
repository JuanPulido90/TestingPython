import pytest

@pytest.fixture()
def fixtureCode():
    print("this is a fixture executed before test case")
    print("-------------------------------------------")

@pytest.mark.Smoke
def test_register():
    print("Smoke")
    print("Smoke test")

import pytest


@pytest.mark.Smoke
def test_login():
    print("smoke")
    print("smoke test")

@pytest.mark.Sanity
def test_invalidcredentials():
    print("Sanity")
    print("Sanity")

# Print statement output display on console -s
# Verbose mode display test cases name with status -v

#Omitir test cases con condicion y añadir una razon
#import pytest
# @pytest.mark.skip over the test case that we want to skip
# a=100, a= 101
# @pytest.mark.skipif(a>100, reason="Skipping as this functionality is not working, developer will fix it in new build")



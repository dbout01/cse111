# Author - Dylan Butterfield, CSE111, 3:15PM Class

# import
import pytest
from names import extract_family_name, extract_given_name, make_full_name



# makes full name
def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"



# extracts family name
def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"



# extracts given name
def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"

    

# Run the tests
pytest.main(["-v", "--tb=line", "-rN", __file__])

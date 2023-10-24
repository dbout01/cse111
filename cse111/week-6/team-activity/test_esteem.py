import pytest
from esteem import positive_question, negative_question


def test_positive_question(question):
    assert positive_question(question) == question


def test_negative_question(question):
    assert negative_question(question) == question


pytest.main(["-v", "--tb=line", "-rN", __file__])
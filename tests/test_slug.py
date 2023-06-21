import pytest

from shortener_api.utils.random_slug import generate_slug


def test_random_slug():
    assert len(generate_slug(5)) == 5
    assert len(generate_slug(15)) == 15
    assert len(generate_slug(25)) == 25

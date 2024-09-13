import pytest
from seasons import calculate_words

def test_input():
    with pytest.raises(SystemExit):
        calculate_words("January 1, 1999")
        assert calculate_words("1999-01-01") == "thirteen million, one hundred sixty-five thousand, nine hundred twenty"

    with pytest.raises(SystemExit):
        calculate_words("1999.01.01")

    with pytest.raises(SystemExit):
        calculate_words("1999-10-99")

    with pytest.raises(SystemExit):
        calculate_words("cat")

import pytest
from main import art_ascii

@pytest.fixture
def mock_func():

    return {
        "0": ["        ", "  ___   ", " / _ \  ", "| | | | ", "| |_| | ", " \___/  ", "        ", "        "],
        "M": [" __  __  ", "|  \/  | ", "| \  / | ", "| |\/| | ", "| |  | | ", "|_|  |_| ", "         ", "         "],
        " ": ["        "] * 8,  
    }

def test_art_ascii(mock_func):

    result = art_ascii("0", mock_func)
    expected = "\n".join([
        "        ",
        "  ___   ",
        " / _ \  ",
        "| | | | ",
        "| |_| | ",
        " \___/  ",
        "        ",
        "        "
    ])
    assert result == expected
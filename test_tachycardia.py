import pytest
import string


@pytest.mark.parametrize("word, expected", [
                            ("tachycardic", True),
                            ("TaChYcArDiC", True),
                            ("    TaChYcArDiC     ", True),
                            (string.punctuation + "TaChYcArDiC" +
                                string.punctuation, True),
                            (string.punctuation + " TaChYcArDiC " +
                                string.punctuation, True),
                            (" " + string.punctuation + "TaChYcArDiC" +
                                string.punctuation + " ", True),
                            ("! ..@tachycardiC  #%&@.()", True),
                            ("word", False)
])
def test_is_tachycardic(word, expected):
    from tachycardia import is_tachycardic
    result = is_tachycardic(word)
    assert result == expected

import pytest

from translate import translate_to_pig_latin


@pytest.mark.parametrize(
    "message, expected",
    [
        ("hello", "ello-hay"),
        ("apple", "apple-way"),
        ("string", "ing-stray"),
        ("", ""),
        ("a", "a-way"),
        ("I am testing", "I-way am-way esting-tay"),
        ("Python is fun", "Ython-pay is-way un-fay"),
        ("Hello, world!", "Ello-hay, orld-way!"),
        ("This is a test.", "Is-thay is-way a-way est-tay."),
        ("Pig Latin is fun!", "Ig-pay Atin-lay is-way un-fay!"),
    ],
)
def test_translator_to_pig_latin(message: str, expected: str) -> None:
    translated_message: str = translate_to_pig_latin(message)
    assert translated_message == expected, (
        f"Expected '{expected}' but got '{translated_message}'"
    )

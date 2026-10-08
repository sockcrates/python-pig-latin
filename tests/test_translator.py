from translate import translate_to_pig_latin


def test_translator_to_pig_latin() -> None:
    message = "Hello, world!"
    translated_message = translate_to_pig_latin(message)
    assert translated_message == "Ello-hay, orld-way!", (
        f"Expected 'Ello-hay, orld-way!' but got '{translated_message}'"
    )

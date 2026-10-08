from translator import Translator


def test_translator_to_pig_latin() -> None:
    translator = Translator()
    message = "Hello, world!"
    translated_message = translator.to_pig_latin(message)
    assert translated_message == "Ello-hay, orld-way!", (
        f"Expected 'Ello-hay, orld-way!' but got '{translated_message}'"
    )

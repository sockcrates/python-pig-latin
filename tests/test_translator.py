from translator import Translator


def test_tokenize() -> None:
    translator = Translator()
    message = "Hello, world!"
    tokenized_message: list[str] = translator._tokenize(message)  # noqa: SLF001
    assert tokenized_message == ["Hello", ", ", "world", "!"]


def test_translator_to_pig_latin() -> None:
    translator = Translator()
    message = "Hello, world!"
    translated_message = translator.to_pig_latin(message)
    assert translated_message == "Ello-hay, orld-way!", (
        f"Expected 'Ello-hay, orld-way!' but got '{translated_message}'"
    )

from typing import Literal

LOWERCASE_VOWELS: Literal["aeiou"] = "aeiou"


def _translate_word_to_pig_latin(word: str) -> str:
    if not len(word):
        return word
    if word[0].lower() in LOWERCASE_VOWELS:
        return word + "-hay"
    for i, letter in enumerate(word):
        if letter.lower() in LOWERCASE_VOWELS:
            is_capital: bool = word.istitle()
            result: str = f"{word[i:]}-{word[:i].lower()}ay"

            if is_capital:
                result = result.capitalize()

            return result
    return word


def translate_to_pig_latin(message: str) -> str:
    """Translate the given message into Pig Latin.

    Args:
        message (str): The message to be translated.

    Returns:
        str: The translated message in Pig Latin.
    """
    translated_message: list[str] = []
    word: list[str] = []

    def flush_word() -> None:
        if not len(word):
            return
        translated_message.append(_translate_word_to_pig_latin("".join(word)))
        word.clear()

    for char in message:
        if char.isalnum():
            word.append(char)
        else:
            flush_word()
            translated_message.append(char)

    return "".join(translated_message)

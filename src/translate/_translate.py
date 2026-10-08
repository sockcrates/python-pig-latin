from typing import Literal

LOWERCASE_VOWELS: Literal["aeiouy"] = "aeiouy"


def _translate_word_to_pig_latin(word: str) -> str:
    if not word:
        return word

    word_length: int = len(word)
    split_index: int = 0

    while split_index < len(word):
        if word[split_index : split_index + 2].lower() == "qu":
            split_index += 2
        elif word[split_index].lower() in LOWERCASE_VOWELS:
            break
        else:
            split_index += 1

    if split_index == 0:
        return word + "-way"

    if split_index == word_length:
        return word

    result: str = f"{word[split_index:]}-{word[:split_index].lower()}ay"

    if word.istitle():
        return result.capitalize()

    return result


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

    flush_word()

    return "".join(translated_message)

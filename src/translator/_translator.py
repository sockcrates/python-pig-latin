from typing import Literal


class Translator:
    """Translator for converting messages into Pig Latin."""

    def _tokenize(self, message: str) -> list[str]:
        tokens: list[str] = []
        current_token: list[str] = []
        mode: Literal["init", "punctuation", "word"] = "init"

        for char in message:
            if char.isalnum():
                match mode:
                    case "init":
                        mode = "word"
                    case "punctuation":
                        mode = "word"
                        tokens.append("".join(current_token))
                        current_token.clear()

                current_token.append(char)
            else:
                match mode:
                    case "init":
                        mode = "punctuation"
                    case "word":
                        mode = "punctuation"
                        tokens.append("".join(current_token))
                        current_token.clear()

                current_token.append(char)

        tokens.append("".join(current_token))

        return tokens

    def to_pig_latin(self, message: str) -> str:
        """Translate the given message into Pig Latin.

        Args:
            message (str): The message to be translated.

        Returns:
            str: The translated message in Pig Latin.
        """
        tokens: list[str] = self._tokenize(message)
        pig_latin: list[str] = []

        for token in tokens:
            if token.isalnum():
                if token[0] in "aeiou":
                    pig_latin.append(token + "-way")
                else:
                    for i, letter in enumerate(token):
                        if letter.lower() in "aeiou":
                            is_capital: bool = token.istitle()
                            result: str = f"{token[i:]}-{token[:i].lower()}ay"

                            if is_capital:
                                result = result.capitalize()

                            pig_latin.append(result)
                            break
            else:
                pig_latin.append(token)

        return "".join(pig_latin)

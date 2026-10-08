"""Main entry point for the Pig Latin translator."""

import argparse


def main() -> int:
    """Command invocation for the Pig Latin translator."""
    parser = argparse.ArgumentParser(description="A Pig Latin translator.")
    parser.add_argument(
        "message",
        type=str,
        help="The message to be translated into Pig Latin.",
    )

    args = parser.parse_args()
    message = args.message

    if not message:
        print("Error: No message provided for translation.")  # noqa: T201
        return 1

    return 0

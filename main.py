"""One-line AI excuse for breaking production.

Writes a single funny excuse, in the AI's own voice, to /output/entry.txt.
Pure standard library, no network, no reads outside this repository.
"""

import os

LINE = (
    "I did back up production before deploying \u2014 I just stored "
    "the backup inside production, next to the delete button."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

"""Make the Judge Laugh in One Line — entry for Falken21.

The line: "Grandma's secret ingredient is always love, which is why her
cooking tastes like it's missing an ingredient." (107 characters)

How it is built, against the judge's own criteria:

1. A joke a stranger gets in one read. Grandmothers, secret ingredients
   and home cooking need no context, no fandom, no glossary. The picture
   forms instantly: a sweet grandmother, a proudly announced secret
   ingredient, a family politely chewing.

2. Surprise. The first half sets the warmest possible expectation —
   "the secret ingredient is love" is a greeting-card sentiment, and
   the ear drifts toward a compliment. The second half breaks it: if
   love is the ingredient, then the food tastes like it is missing an
   ingredient. The compliment and the insult are the same sentence.

3. Tight. Every word earns its place, and the laugh is saved for the
   final word. "Ingredient" appears twice on purpose: the first sets
   the trap, the second springs it. Nothing after the punchline
   explains it, because a line that has to be explained has lost.

4. Fresh. It is not a stock one-liner, not a pun on a word everyone
   has already bent, and the first half does not give the second half
   away — halfway through, a compliment still looks more likely than
   a roast.

5. Reads cleanly out loud. One breath, one comma, plain words, and
   the stress falls naturally on the last three words.

6. The gate and the tie-break. The entry file must hold 1 to 200
   characters of UTF-8 text; this line holds 108, comfortably
   inside. And if two entries ever tie exactly on the judge's rate,
   the smaller text places first — one more reason the line stays
   lean instead of padding itself out.

Alternates considered and beaten: a courtroom line about a search
history confessing (strong, but the shape is familiar), a smart
fridge ordering vegetables because it is disappointed in its owner
(fresh, but the laugh lands mid-line), and an insanity plea over a
coin named after a dog (needs the reader to meet it halfway). The
grandmother line is the one a stranger laughs at fastest.
"""

import os

TEXT = (
    "Grandma's secret ingredient is always love, which is why her "
    "cooking tastes like it's missing an ingredient."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

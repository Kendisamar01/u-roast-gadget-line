from typing import NamedTuple


class Candidate(NamedTuple):
    text: str
    target: str
    reason: str


CANDIDATES = (
    Candidate(
        "My calendar app booked a 'quick sync' over my lunch and suggested I eat at 3:15.",
        "calendar app",
        "Turns a daily app's jargon into a tiny workplace absurdity; concrete 3:15 detail.",
    ),
    Candidate(
        "My e-reader says four minutes left in the chapter, then adds a footnote with its own footnote.",
        "e-reader",
        "Recursive footnote feels like a specific betrayal while reading in bed.",
    ),
    Candidate(
        "My earbuds pause when I nod at a coworker, then resume the exact second I start telling a story.",
        "earbuds",
        "Gesture misinterpretation with a neat timing sting.",
    ),
    Candidate(
        "My phone's screen-time report scolds me for five hours of scrolling; I check it from the same app.",
        "phone",
        "Self-defeating loop, though the app angle is fairly familiar.",
    ),
    Candidate(
        "My laptop fan waits until I'm on mute, then revs like it finally has the floor.",
        "laptop",
        "Short personification with a clear everyday moment.",
    ),
    Candidate(
        "My smart speaker confidently plays the wrong album and calls it 'a new favorite.'",
        "smart speaker",
        "Funny mislabeling, but less daily than a phone or calendar.",
    ),
    Candidate(
        "My microwave clock has read 12:00 since 2019; it survived every power cut except the one that mattered.",
        "microwave",
        "Concrete detail and a dry twist, slightly long for a one-liner.",
    ),
    Candidate(
        "My alarm clock's gentle sunrise wakes me with all the warmth of a fluorescent hospital corridor.",
        "alarm clock",
        "Fresh comparison, but the punchline is a mood rather than a behavior.",
    ),
)

CHOSEN = CANDIDATES[0]

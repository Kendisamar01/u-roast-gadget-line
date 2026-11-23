from dataclasses import dataclass


@dataclass(frozen=True)
class Candidate:
    text: str
    target: str
    scores: tuple[int, int, int, int, int]
    note: str

    @property
    def total(self):
        return sum(self.scores)


CANDIDATES = (
    Candidate(
        "My map app reroutes me around traffic it caused by telling 40,000 drivers to take my street.",
        "map app",
        (5, 5, 5, 5, 5),
        "The app solves a jam it just created; 40,000 drivers makes the gripe specific.",
    ),
    Candidate(
        "My weather app demands precise location just to confirm it's raining on my head.",
        "weather app",
        (5, 4, 4, 5, 4),
        "Permission-dialog recognition, but the location joke is a familiar angle.",
    ),
    Candidate(
        "My password manager generates a 40-character password, then expects me to type it into the TV with a remote.",
        "password manager",
        (5, 4, 4, 4, 5),
        "Concrete device mismatch, though slightly long for a one-liner.",
    ),
    Candidate(
        "My router calls it a 'quick update,' then makes the Wi-Fi a philosophical concept for 20 minutes.",
        "router",
        (5, 4, 5, 4, 4),
        "Fresh wording for an update outage, but the target is less personal.",
    ),
    Candidate(
        "My smartwatch buzzes 'Nice job standing up!' as I walk over to plug it in.",
        "smartwatch",
        (5, 4, 4, 5, 4),
        "Tight and relatable; the fitness-nag angle has been done more often.",
    ),
    Candidate(
        "My smart doorbell marks the delivery driver as 'family' and my family as 'suspicious activity.'",
        "smart doorbell",
        (5, 4, 4, 4, 4),
        "Good misclassification sting; daily use is slightly less universal.",
    ),
    Candidate(
        "My microwave's 'one-touch' button needs two touches: one to wake it, one to ask if I meant it.",
        "microwave",
        (5, 4, 3, 4, 4),
        "Irony lands, but the double-tap complaint is a common one.",
    ),
    Candidate(
        "My laptop's fan spins up when I open a spreadsheet, as if it just remembered it has a family to feed.",
        "laptop",
        (5, 3, 3, 4, 4),
        "Neat image, but a loud laptop fan is the obvious complaint.",
    ),
    Candidate(
        "My printer's low-ink warning arrives in full color, nine pages early.",
        "printer",
        (4, 4, 3, 5, 4),
        "Very tight, but printer jokes are well worn and printing is less than daily.",
    ),
    Candidate(
        "My smart TV asks if I'm still there during the ad, then recommends a recap of the show I'm watching.",
        "smart TV",
        (5, 4, 4, 4, 4),
        "Specific behavior with a nice loop, but not as fresh as the map angle.",
    ),
)

SELECTED_INDEX = 0

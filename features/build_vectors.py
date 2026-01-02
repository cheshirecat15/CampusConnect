import numpy as np

# -------------------------------
# Feature universe (FIXED)
# -------------------------------

ALL_DOMAINS = [
    "AI/ML",
    "Data Science",
    "Cybersecurity",
    "Web Dev",
    "App Dev",
    "Systems",
    "Robotics",
    "Startups",
    "Product"
]

ALL_CLUBS = [
    "AIS",
    "Enactus",
    "Ciphers",
    "IOT and Robotics",
    "Codechef",
    "Fullstacks",
    "FOSS",
    "CSI"
]

ALL_GOALS = [
    "Research",
    "Projects",
    "Hackathons",
    "Startup",
    "Learning"
]

ALL_YEARS = [1, 2, 3]

# -------------------------------
# Vectorization logic
# -------------------------------

def vectorize_student(student):
    """
    Converts a student profile dictionary into a numeric vector.
    Output vector order:
    [domains | clubs | goals | year]
    """

    # Domains (binary)
    domain_vec = [
        1 if domain in student["domains"] else 0
        for domain in ALL_DOMAINS
    ]

    # Clubs / chapters (binary)
    club_vec = [
        1 if club in student["clubs"] else 0
        for club in ALL_CLUBS
    ]

    # Goals (binary)
    goal_vec = [
        1 if goal in student["goals"] else 0
        for goal in ALL_GOALS
    ]

    # Year (one-hot)
    year_vec = [
        1 if student["year"] == y else 0
        for y in ALL_YEARS
    ]

    # Concatenate all parts
    vector = np.array(
        domain_vec + club_vec + goal_vec + year_vec,
        dtype=float
    )

    return vector

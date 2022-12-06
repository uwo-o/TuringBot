import os

# Channels configuration
QUESTIONS_CHANNEL = "turing-bot"

# Path constants
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_PATH = os.path.join(ROOT_PATH, "data/questions/")

# If the reply type is sent privately or in the same channel
message_privacy = {
    "question": False,
    "help": False
}
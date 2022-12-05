import os

QUESTIONS_CHANNEL = "turing-bot"

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_PATH = os.path.join(ROOT_PATH, "data/questions/")

message_privacy = {
    "question": False
}
import os


class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN","7254205392:AAFiR1r7y44XdXnshKH9BGK6BUusrdiubLA")

    SESSION_NAME = os.environ.get("SESSION_NAME", "ytuploader66tbot")

    API_ID = int(os.environ.get("API_ID","21503867"))

    API_HASH = os.environ.get("API_HASH","e0e50d95e1319072731fb0a4a585e9d5")

    CLIENT_ID = os.environ.get("CLIENT_ID","888858455819-fqi07e5mnt2kiapvm6i7k02vp299c3el.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET","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")

    BOT_OWNER = int(os.environ.get("BOT_OWNER","6221136155"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "6221136155")

    AUTH_USERS = [BOT_OWNER, 6221136155] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE","unlisted") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"

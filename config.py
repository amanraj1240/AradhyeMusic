"""
AradhyeMusic — central runtime configuration
All values are read from environment variables (see .env.example).
"""

import os
import re

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


def _env_int(key: str, default=None, *, required: bool = False) -> int | None:
    raw = os.getenv(key)
    if raw is None or raw == "":
        if required:
            raise SystemExit(f"[CONFIG] Missing required integer env var: {key}")
        return default
    try:
        return int(raw)
    except ValueError as exc:
        raise SystemExit(f"[CONFIG] Env var {key!r} must be an integer, got {raw!r}") from exc


def _env_bool(key: str, default: bool = False) -> bool:
    raw = os.getenv(key)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on", "y", "t"}


# --- Telegram core (required) -------------------------------------------------
API_ID = _env_int("API_ID", required=True)
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# --- Owner / branding ---------------------------------------------------------
OWNER_ID = _env_int("OWNER_ID", required=True)
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "amanraj1240")
BOT_USERNAME = os.getenv("BOT_USERNAME", "AradhyeMusicBot")

# --- Database / logging -------------------------------------------------------
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
LOG_GROUP_ID = _env_int("LOG_GROUP_ID", required=True)

# --- Heroku (optional) --------------------------------------------------------
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# --- Upstream / updates -------------------------------------------------------
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/amanraj1240/AradhyeMusic")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN")

# --- Support links ------------------------------------------------------------
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/ShrutiBots")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/ShrutiBotsSupport")
INSTAGRAM = os.getenv("INSTAGRAM", "https://instagram.com/")
YOUTUBE = os.getenv("YOUTUBE", "https://youtube.com/")
GITHUB = os.getenv("GITHUB", "https://github.com/amanraj1240")
DONATE = os.getenv("DONATE", "https://t.me/ShrutiBots")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

# --- Limits -------------------------------------------------------------------
DURATION_LIMIT_MIN = _env_int("DURATION_LIMIT", 300)
PLAYLIST_FETCH_LIMIT = _env_int("PLAYLIST_FETCH_LIMIT", 25)

TG_AUDIO_FILESIZE_LIMIT = _env_int("TG_AUDIO_FILESIZE_LIMIT", 104857600)
TG_VIDEO_FILESIZE_LIMIT = _env_int("TG_VIDEO_FILESIZE_LIMIT", 2145386496)

# --- Spotify ------------------------------------------------------------------
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# --- Assistant string sessions (up to 5) -------------------------------------
STRING1 = os.getenv("STRING_SESSION")
STRING2 = os.getenv("STRING_SESSION2")
STRING3 = os.getenv("STRING_SESSION3")
STRING4 = os.getenv("STRING_SESSION4")
STRING5 = os.getenv("STRING_SESSION5")

# --- Behaviour flags ----------------------------------------------------------
AUTO_LEAVING_ASSISTANT = _env_bool("AUTO_LEAVING_ASSISTANT", False)

# --- Image assets -------------------------------------------------------------
START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/7q8bfg.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://files.catbox.moe/eehxb4.jpg")
PLAYLIST_IMG_URL = os.getenv("PLAYLIST_IMG_URL", "https://files.catbox.moe/eehxb4.jpg")
STATS_IMG_URL = os.getenv("STATS_IMG_URL", "https://files.catbox.moe/eehxb4.jpg")
TELEGRAM_AUDIO_URL = os.getenv("TELEGRAM_AUDIO_URL", "https://files.catbox.moe/eehxb4.jpg")
TELEGRAM_VIDEO_URL = os.getenv("TELEGRAM_VIDEO_URL", "https://files.catbox.moe/eehxb4.jpg")
STREAM_IMG_URL = os.getenv("STREAM_IMG_URL", "https://files.catbox.moe/eehxb4.jpg")
SOUNCLOUD_IMG_URL = os.getenv("SOUNCLOUD_IMG_URL", "https://files.catbox.moe/eehxb4.jpg")
YOUTUBE_IMG_URL = os.getenv("YOUTUBE_IMG_URL", "https://files.catbox.moe/eehxb4.jpg")
SPOTIFY_ARTIST_IMG_URL = os.getenv("SPOTIFY_ARTIST_IMG_URL", "https://files.catbox.moe/eehxb4.jpg")
SPOTIFY_ALBUM_IMG_URL = os.getenv("SPOTIFY_ALBUM_IMG_URL", "https://files.catbox.moe/eehxb4.jpg")
SPOTIFY_PLAYLIST_IMG_URL = os.getenv("SPOTIFY_PLAYLIST_IMG_URL", "https://files.catbox.moe/eehxb4.jpg")

# --- Runtime state containers (do not move) ----------------------------------
BANNED_USERS = filters.user()
adminlist: dict = {}
lyrical: dict = {}
votemode: dict = {}
autoclean: list = []
confirmer: dict = {}

TEMP_DB_FOLDER = "tempdb"


def time_to_seconds(time) -> int:
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Owner/error reporting fallback (kept identifier so upstream code paths still work)
ERROR_FORMAT = OWNER_ID

# --- Sanity checks ------------------------------------------------------------
if SUPPORT_CHANNEL and not re.match(r"^(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://")

if SUPPORT_GROUP and not re.match(r"^(?:http|https)://", SUPPORT_GROUP):
    raise SystemExit("[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://")

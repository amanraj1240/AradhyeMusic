<h1 align="center">🎵 AradhyeMusic 🎵</h1>

<p align="center">
  <b>An advanced, fast & feature-rich Telegram Voice Chat Music Bot</b><br>
  Plays high-quality music in Telegram group voice chats from
  <i>YouTube • Spotify • SoundCloud • Apple Music • Resso • Telegram</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pyrogram-Pyrofork-orange?logo=telegram&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTgCalls-2.x-success" />
  <img src="https://img.shields.io/badge/License-AGPL--3.0-red" />
  <img src="https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white" />
</p>

---

## ✨ Features

- 🎧 **Music & Video** streaming in Telegram group/channel voice chats
- 🔎 Multi-source: **YouTube, Spotify, SoundCloud, Apple Music, Resso, Telegram audio/video files**
- 📝 Search, queue, skip, pause, resume, loop, shuffle, seek
- 👥 Multi-assistant support (up to 5 string sessions for load balancing)
- 🛠 Powerful admin tools, sudo system, broadcast, gban, maintenance mode
- 🌐 Multi-language UI strings
- 📊 Built-in stats, ping, speedtest, system info
- 🎨 Inline thumbnails / Carbon code-image generation
- 🐳 First-class **Docker** + **docker-compose** support
- ✅ **CI pipeline** (GitHub Actions): lint + Docker build on every push

---

## 🚀 Quick Start (Docker — recommended)

```bash
# 1. Clone
git clone https://github.com/amanraj1240/AradhyeMusic.git
cd AradhyeMusic

# 2. Create your env file
cp .env.example .env
nano .env       # fill API_ID, API_HASH, BOT_TOKEN, STRING_SESSION, MONGO_DB_URI ...

# 3. Run (includes a MongoDB container)
docker compose up -d --build

# 4. Watch logs
docker compose logs -f aradhyemusic
```

> The compose file ships its own MongoDB. If you prefer Atlas, set `MONGO_DB_URI`
> in `.env` and remove the `mongo` service from `docker-compose.yml`.

---

## 🛠 Manual Install (bare metal / VPS)

Prerequisites: **Python 3.12**, **FFmpeg**, **Node.js 20**, **Git**, **MongoDB URI**.

```bash
# Debian / Ubuntu
sudo apt update && sudo apt install -y python3.12 python3.12-venv python3-pip ffmpeg git curl

git clone https://github.com/amanraj1240/AradhyeMusic.git
cd AradhyeMusic

python3.12 -m venv .venv
source .venv/bin/activate
pip install -U pip wheel
pip install -r requirements.txt

cp .env.example .env
nano .env

bash start
```

---

## 🔑 Required Environment Variables

| Variable          | Description                                                  |
|-------------------|--------------------------------------------------------------|
| `API_ID`          | App ID from <https://my.telegram.org>                        |
| `API_HASH`        | App hash from <https://my.telegram.org>                      |
| `BOT_TOKEN`       | Bot token from [@BotFather](https://t.me/BotFather)          |
| `STRING_SESSION`  | Pyrogram v2 string session for the assistant userbot         |
| `MONGO_DB_URI`    | MongoDB connection URI                                       |
| `OWNER_ID`        | Telegram user-id of the owner                                |
| `LOG_GROUP_ID`    | Group id where the bot will send logs (bot must be admin)    |

Optional: `STRING_SESSION2…5`, `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`,
`HEROKU_API_KEY`, `HEROKU_APP_NAME`, `SUPPORT_GROUP`, `SUPPORT_CHANNEL`,
`UPSTREAM_REPO`, `UPSTREAM_BRANCH`, `GIT_TOKEN`, `START_IMG_URL` …

A complete template lives in [`.env.example`](./.env.example).

---

## ☁️ One-click Deploy

| Platform | Button |
|---------|--------|
| **Heroku**  | `app.json` is pre-configured — fork & click *Deploy* on Heroku |
| **Render**  | `render.yaml` blueprint included |
| **Koyeb / Railway / Fly.io** | Use the included `Dockerfile` |

---

## 🧪 Continuous Integration

Every push runs the workflow at [`.github/workflows/ci.yml`](.github/workflows/ci.yml):

- Python compile-check across all source files
- `pyflakes` static analysis
- `ruff` style/bug lint
- Docker image build (cached via GHA cache)

---

## 📂 Project Layout

```
AradhyeMusic/
├── ShrutiMusic/           # main package (kept stable for upstream merges)
│   ├── core/              # bot, userbot, mongo, calls, git, dir
│   ├── platforms/         # YouTube, Spotify, SoundCloud, Apple, Resso, Telegram
│   ├── plugins/           # admins, sudo, tools, play, misc
│   └── utils/             # streams, thumbnails, decorators, db helpers, formatters
├── strings/               # i18n language files
├── config.py              # all env-driven configuration
├── requirements.txt       # Python 3.12 compatible deps
├── Dockerfile             # multi-stage build (Python 3.12-slim)
├── docker-compose.yml     # bot + MongoDB
├── .github/workflows/     # CI pipelines
├── app.json               # Heroku one-click manifest
├── render.yaml            # Render blueprint
└── start                  # bot launcher
```

---

## 🤝 Credits

This project is an upgraded fork of
[Devbok/ShrutiMusic1](https://github.com/Devbok/ShrutiMusic1) and the upstream
[NoxxOP/ShrutiMusic](https://github.com/NoxxOP/ShrutiMusic) lineage. All
original authors retain their credits — see [`LICENSE`](./LICENSE).

Maintained with ❤️ by **[@amanraj1240](https://github.com/amanraj1240)**.

---

## 📜 License

Licensed under **AGPL-3.0**. See [LICENSE](./LICENSE) for the full text.

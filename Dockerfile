# syntax=docker/dockerfile:1.7
# AradhyeMusic — Multi-stage Docker build (Python 3.12 + Node 20 + FFmpeg)

############################
# Stage 1 — Builder
############################
FROM python:3.12-slim-bookworm AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Build deps for compiling wheels (TgCrypto, numpy, opencv, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        g++ \
        git \
        curl \
        libffi-dev \
        libssl-dev \
        libjpeg-dev \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY requirements.txt .

# Install dependencies into an isolated prefix that we copy into the runtime image
RUN pip install --upgrade pip setuptools wheel \
 && pip install --prefix=/install --no-warn-script-location -r requirements.txt


############################
# Stage 2 — Runtime
############################
FROM python:3.12-slim-bookworm AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    DEBIAN_FRONTEND=noninteractive \
    TZ=Asia/Kolkata

# Runtime system deps (FFmpeg from official repos, Node 20 for any JS-based deps)
RUN apt-get update && apt-get install -y --no-install-recommends \
        ffmpeg \
        git \
        curl \
        ca-certificates \
        gnupg \
        tzdata \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy installed Python packages from builder stage
COPY --from=builder /install /usr/local

# App user (don't run as root)
RUN useradd -m -u 1000 aradhye \
 && mkdir -p /app \
 && chown -R aradhye:aradhye /app
WORKDIR /app
COPY --chown=aradhye:aradhye . /app/
# Re-assert ownership of WORKDIR so the runtime user can write log files,
# downloads/, cookies, etc. inside /app at runtime.
RUN chown -R aradhye:aradhye /app
USER aradhye

CMD ["bash", "start"]

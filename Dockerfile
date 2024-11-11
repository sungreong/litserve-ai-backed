# Python 3.12 베이스 이미지 사용
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 설치 및 캐시 정리
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    git \
    dos2unix \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 캐시 디렉토리 구조 생성
RUN mkdir -p /app/cache/huggingface \
    /app/cache/torch \
    /app/cache/transformers \
    /app/cache/models \
    /app/logs

# 환경 변수 설정
ENV PYTHONPATH=/app
ENV TORCH_HOME=/app/cache/torch
ENV TRANSFORMERS_CACHE=/app/cache/transformers
ENV HUGGINGFACE_HUB_CACHE=/app/cache/huggingface
ENV HF_HOME=/app/cache/huggingface
ENV MODEL_CACHE_DIR=/app/cache/models
ENV XDG_CACHE_HOME=/app/cache
ENV TOKENIZERS_PARALLELISM=true

# 캐시 디렉토리 권한 설정
RUN chmod -R 777 /app/cache && \
    chown -R 1000:1000 /app/cache

# 볼륨 마운트 포인트 설정
VOLUME ["/app/cache", "/app/logs"]

# 환경 변수 설정
ENV HOST=0.0.0.0
ENV PORT=8000

# 기본 쉘을 bash로 설정
SHELL ["/bin/bash", "-c"]

# bash를 기본 진입점으로 설정
ENTRYPOINT ["/bin/bash"]
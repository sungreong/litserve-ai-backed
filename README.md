# LitServer AI Backend

HuggingFace 모델들을 서빙하기 위한 Lightning AI 기반 서버입니다.

## 기능
- Text Generation (GPT-2, T5 등)
- Text Reranking
- Text Classification

## 요구사항
- Docker
- Docker Compose
- NVIDIA GPU (선택사항)
- NVIDIA Container Toolkit (GPU 사용 시 필요)

## 설치 및 실행

## 도커 빌드

```bash
docker build -t litserve-model .
```

## 도커 실행

### 1. 서버 실행 (PowerShell)
```bash
docker run -itd --rm -p 9999:8000 -v C:\Users\leesu\Documents\ProjectCode\llm-serving\litserver-ai-backend\app:/app litserve-model
```

## 볼륨 마운트 설명
- `./app:/app`: 로컬의 app 디렉토리를 컨테이너의 /app 디렉토리에 마운트
- 코드 수정 시 실시간 반영을 위해 사용 (개발 모드)

## 환경 변수 설정 (선택사항)
```bash
docker run -it --rm \
  -p 9999:8000 \
  -v ./app:/app \
  -e DEFAULT_MODELS="gpt2,bert-base-uncased" \
  -e CUDA_VISIBLE_DEVICES=0 \
  litserve-model bash
```
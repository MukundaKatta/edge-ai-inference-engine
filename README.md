# Edge Ai Inference Engine

Optimized inference for AI models on edge devices

## Features

- Api
Benchmarker
Cli
Engine
Optimizers - Distillation
Optimizers - Pruning
Profiler
Quantizer
Runtime

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Key Dependencies:** pydantic,fastapi,uvicorn,anthropic,openai,numpy
- **Containerization:** Docker + Docker Compose

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)

### Installation

```bash
git clone https://github.com/MukundaKatta/edge-ai-inference-engine.git
cd edge-ai-inference-engine
pip install -r requirements.txt
```

### Running

```bash
uvicorn app.main:app --reload
```

### Docker

```bash
docker-compose up
```

## Project Structure

```
edge-ai-inference-engine/
├── src/           # Source code
├── tests/         # Test suite
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## License

MIT

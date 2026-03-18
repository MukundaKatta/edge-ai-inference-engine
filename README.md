# edge-ai-inference-engine

**Optimized inference engine for running AI models on edge devices**

![Build](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-proprietary-red)

## Install
```bash
pip install -e ".[dev]"
```

## Quick Start
```python
from src.core import EdgeAiInferenceEngine
 instance = EdgeAiInferenceEngine()
r = instance.process(input="test")
```

## CLI
```bash
python -m src status
python -m src run --input "data"
```

## API
| Method | Description |
|--------|-------------|
| `process()` | Process |
| `analyze()` | Analyze |
| `transform()` | Transform |
| `validate()` | Validate |
| `export()` | Export |
| `get_stats()` | Get stats |
| `get_stats()` | Get stats |
| `reset()` | Reset |

## Test
```bash
pytest tests/ -v
```


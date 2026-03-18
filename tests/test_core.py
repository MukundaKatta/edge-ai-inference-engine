"""Tests for EdgeAiInferenceEngine."""
from src.core import EdgeAiInferenceEngine
def test_init(): assert EdgeAiInferenceEngine().get_stats()["ops"] == 0
def test_op(): c = EdgeAiInferenceEngine(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = EdgeAiInferenceEngine(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = EdgeAiInferenceEngine(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = EdgeAiInferenceEngine(); r = c.process(); assert r["service"] == "edge-ai-inference-engine"

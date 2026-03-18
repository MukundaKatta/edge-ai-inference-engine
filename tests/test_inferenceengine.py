"""Tests for InferenceEngine."""
import pytest
from src.inferenceengine import InferenceEngine

def test_init():
    obj = InferenceEngine()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = InferenceEngine()
    result = obj.load_model(input="test")
    assert result["processed"] is True
    assert result["operation"] == "load_model"

def test_multiple_ops():
    obj = InferenceEngine()
    for m in ['load_model', 'quantize_model', 'optimize_graph']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = InferenceEngine()
    r1 = obj.load_model(key="same")
    r2 = obj.load_model(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = InferenceEngine()
    obj.load_model()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = InferenceEngine()
    obj.load_model(x=1)
    obj.quantize_model(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats

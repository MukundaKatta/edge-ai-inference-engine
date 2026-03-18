"""CLI for edge-ai-inference-engine."""
import sys, json, argparse
from .core import EdgeAiInferenceEngine

def main():
    parser = argparse.ArgumentParser(description="Optimized inference engine for running AI models on edge devices")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = EdgeAiInferenceEngine()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"edge-ai-inference-engine v0.1.0 — Optimized inference engine for running AI models on edge devices")

if __name__ == "__main__":
    main()

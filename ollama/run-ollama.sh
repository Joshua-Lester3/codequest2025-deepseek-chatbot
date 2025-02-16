#!/usr/bin/env bash
ollama serve &
ollama list
ollama pull llama3

ollama serve &
ollama list
ollama pull deepseek-r1:1.5b
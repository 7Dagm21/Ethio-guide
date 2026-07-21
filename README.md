# Ethio Gov AI

## Problem
Difficulty accessing Ethiopian government service information.

## Solution
AI assistant that helps citizens navigate passport services.

## MVP Features
- Document-based AI chatbot
- Passport requirement assistant
- Checklist generation
- Document upload
- Voice interaction

## Architecture

User
 ↓
React Frontend
 ↓
FastAPI Backend
 ↓
RAG Pipeline
 ↓
ChromaDB + Gemini

## Tech Stack
Frontend:
- React
- Vite

Backend:
- FastAPI
- Python

AI:
- LangChain
- ChromaDB
- Sentence Transformers
- Gemini API
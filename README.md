# Research Planner — Multi-Agent System

An agentic AI research assistant built with the OpenAI Agents SDK.
Given a research topic, it autonomously plans searches, retrieves
web results, writes a detailed report, and sends a notification.

## Architecture

| Agent           | Role                                      |
|-----------------|-------------------------------------------|
| Planner Agent   | Breaks query into targeted web searches   |
| Search Agent    | Executes web searches in parallel         |
| Writer Agent    | Synthesizes findings into a report        |
| Sender Agent    | Delivers the final report                 |

## Tech Stack

- Python 3.12+
- OpenAI Agents SDK
- Pydantic (structured output validation)
- Gradio (UI)
- asyncio (concurrent agent execution)

## How to Run

1. Clone the repo
2. Create `.env` with your OpenAI API key:
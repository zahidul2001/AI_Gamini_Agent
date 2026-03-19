# 🧠 AI Projects Hub

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C.svg)
![Gemini AI](https://img.shields.io/badge/Google-Gemini%20AI-FF6D00.svg)
![License](https://img.shields.io/badge/license-MIT-green)

**A collection of AI-powered applications: classic games with intelligent opponents and a Gemini-powered research assistant.**

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [🎮 AI Games Hub](#-ai-games-hub)
    - [Chess](#chess)
    - [Nim](#nim)
    - [Tic Tac Toe](#tic-tac-toe)
  - [🌐 Gemini Research Agent](#-gemini-research-agent)
    - [Main Application](#main-application)
    - [Tools Module](#tools-module)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This repository contains two major AI‑driven projects:

1. **AI Games Hub** – Classic board games (Chess, Nim, Tic Tac Toe) with AI opponents using algorithms like Minimax and Alpha‑Beta Pruning.
2. **Gemini Research Agent** – A web‑based research assistant powered by Google’s Gemini AI, LangChain, and Streamlit. It can search the web, retrieve Wikipedia summaries, and save structured research data.

Both projects are built with Python and demonstrate practical applications of AI in gaming and information retrieval.

---

## Projects

### 🎮 AI Games Hub

A collection of three classic games featuring unbeatable or challenging AI opponents. Each game has its own folder with detailed documentation.

| Game          | Description                                                                 | AI Technique                     |
|---------------|-----------------------------------------------------------------------------|----------------------------------|
| **Chess**     | Full chess game with GUI, move validation, and AI opponent.                | Minimax with Alpha-Beta Pruning |
| **Nim**       | Mathematical strategy game where players remove objects from piles.        | Minimax with depth limiting      |
| **Tic Tac Toe** | Classic 3×3 board game against an unbeatable AI.                          | Minimax Algorithm                |

#### Chess
- **Location:** `/chess/`
- **Run:** `python chess_game.py`
- **Dependencies:** `pygame`, `chess`

#### Nim
- **Location:** `/nim/`
- **Run:** `python nim_game.py`
- **Dependencies:** Tkinter (built-in)

#### Tic Tac Toe
- **Location:** `/tic_tac_toe/`
- **Run:** `python tic_tac_toe.py`
- **Dependencies:** Tkinter (built-in)

---

### 🌐 Gemini Research Agent

An intelligent research assistant that leverages **LangChain**, **Google Gemini AI**, and **Streamlit** to perform real‑time research, fetch Wikipedia summaries, simulate web searches, and save results in structured JSON format.

#### Main Application

- **Location:** `/research_agent/` (or root, adjust as needed)
- **Run:** `streamlit run app.py`
- **Features:**
  - Interactive web interface with Streamlit.
  - Uses Gemini 2.0 Flash model for language understanding.
  - LangChain agent with tools: `search_tool`, `wiki_tool`, `save_tool`.
  - Structured JSON output with Pydantic validation.
- **Environment:** Create a `.env` file with `GEMINI_API_KEY=your_key`.

#### Tools Module

- **Location:** `/research_agent/tools.py`
- **Components:**
  - `search_tool(query)`: Simulated search results.
  - `wiki_tool(topic)`: Fetches Wikipedia summaries (supports English and Bengali).
  - `save_tool(data)`: Appends research data to `saved_research.json`.
- **Utility:** `check_models.py` lists available Gemini models.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Clone the Repository
```bash
git clone https://github.com/yourusername/ai-projects-hub.git
cd ai-projects-hub
```

### Install Dependencies
You can install all required packages at once using the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

#### requirements.txt
```
# Core
streamlit
langchain-google-genai
langchain-core
langchain-community
wikipedia-api
python-dotenv
pydantic

# Games
pygame
chess
```

> **Note:** Tkinter comes pre‑installed with Python; no extra installation needed.

---

## Usage

### Running the Games
Navigate to the respective game folder and execute the Python file. Example:
```bash
cd chess
python chess_game.py
```

### Running the Research Agent
1. Set up your Gemini API key in a `.env` file inside the research agent folder:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
2. Launch the Streamlit app:
   ```bash
   streamlit run research_agent/app.py
   ```
3. Open your browser at `http://localhost:8501` and enter a research query.

---

## Technologies

- **Python 3.8+**
- **Streamlit** – Web interface for the research agent.
- **LangChain** – Agent orchestration and tool integration.
- **Google Gemini AI** – Large language model for research.
- **Pygame** – Chess GUI.
- **Tkinter** – GUIs for Nim and Tic Tac Toe.
- **Wikipedia-API** – Fetching real Wikipedia data.
- **Minimax & Alpha-Beta Pruning** – AI decision-making in games.

---

## Contributing

Contributions are welcome! If you’d like to improve the code, add a new game, or enhance the research agent, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please ensure your code follows the existing style and includes appropriate comments.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

*Happy coding and researching!*

</div>

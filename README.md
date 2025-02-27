# CDP Support Chatbot

## Overview
The **CDP Support Chatbot** is a Flask-based chatbot designed to assist users with questions related to Customer Data Platforms (CDPs) such as **Segment, mParticle, Lytics, and Zeotap**. The chatbot processes user queries using NLP and retrieves relevant documentation to provide accurate responses.

## Features
- **Natural Language Processing (NLP):** Uses spaCy to extract intent and CDP platform from user queries.
- **Document Indexing & Search:** Utilizes Whoosh to index and retrieve relevant documentation.
- **Flask Backend:** Handles user requests and returns chatbot responses.
- **Interactive Frontend:** A simple HTML/CSS/JS interface for chat interactions.

## Project Structure
```
cdp-chatbot/
│
├── app.py                  # Flask backend
├── static/                 # Frontend assets (CSS, JS)
├── templates/              # HTML templates
│   └── index.html          # Chatbot interface
├── data/                   # Processed documentation
├── nlp/                    # NLP utilities
│   └── processor.py        # NLP processing logic
├── indexer/                # Document indexing logic
│   └── search.py           # Document search logic
└── README.md               # Project documentation
```

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.x** installed along with `pip`.

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/cdp-chatbot.git
   cd cdp-chatbot
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Download the NLP model:**
   ```bash
   python -m spacy download en_core_web_sm
   ```
5. **Run the Flask app:**
   ```bash
   python app.py
   ```
6. **Access the chatbot:**
   Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage
1. Enter a question related to a CDP platform (e.g., *"How do I set up tracking in Segment?"*).
2. The chatbot processes the query and searches indexed documentation.
3. It returns a relevant response based on the retrieved information.

## Core Components
### 1. **Flask Backend (`app.py`)**
- Routes requests to the chatbot interface (`index.html`).
- Processes user questions using NLP.
- Searches indexed documentation for relevant answers.

### 2. **NLP Processing (`nlp/processor.py`)**
- Uses spaCy to extract intent and CDP platform from user queries.

### 3. **Document Indexing & Search (`indexer/search.py`)**
- Uses Whoosh to create an index and search for relevant documentation.

### 4. **Frontend (`templates/index.html`)**
- Simple UI for chatbot interaction using JavaScript to handle user input and responses.

## Future Enhancements
- Improve NLP intent detection.
- Expand support for more CDP platforms.
- Enhance the frontend UI/UX with a chatbot widget.
- Implement a feedback mechanism to improve response accuracy.

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit: `git commit -m "Added new feature"`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.



CDP Support Chatbot
A chatbot designed to answer "how-to" questions related to Customer Data Platforms (CDPs) like Segment, mParticle, Lytics, and Zeotap. The chatbot extracts relevant information from the official documentation of these platforms to guide users on performing specific tasks or achieving outcomes.

Features
Answer "How-to" Questions:

Provides step-by-step instructions for tasks within Segment, mParticle, Lytics, and Zeotap.

Example: "How do I set up a new source in Segment?"

Extract Information from Documentation:

Retrieves relevant information from the official documentation of the CDPs.

Handle Variations in Questions:

Understands different phrasings of the same question.

Handles irrelevant questions gracefully.

Bonus Features:

Cross-CDP Comparisons: Answers questions about differences between platforms.

Advanced "How-to" Questions: Provides guidance on advanced configurations and integrations.

Setup Instructions
1. Prerequisites
Python 3.7 or higher

Install required libraries:

bash
Copy
pip install flask spacy whoosh requests beautifulsoup4
python -m spacy download en_core_web_sm
2. Project Structure
Copy
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
3. Running the Chatbot
Clone the repository or download the project files.

Navigate to the project directory:

bash
Copy
cd cdp-chatbot
Run the Flask app:

bash
Copy
python app.py
Open your browser and navigate to http://127.0.0.1:5000.

Usage
1. Asking Questions
Type your question in the input box and click "Send".

Example questions:

"How do I set up a new source in Segment?"

"How can I create a user profile in mParticle?"

"How do I build an audience segment in Lytics?"

"How can I integrate my data with Zeotap?"

2. Cross-CDP Comparisons
Ask questions comparing functionalities across platforms:

"How does Segment's audience creation process compare to Lytics'?"

3. Advanced Questions
Ask advanced "how-to" questions:

"How do I set up server-side tracking in Segment?"

"How can I use mParticle's identity resolution features?"

4. Irrelevant Questions
The chatbot will respond to irrelevant questions with a fallback message:

Example: "Which movie is releasing this week?" → "Sorry, I can only answer questions related to Segment, mParticle, Lytics, and Zeotap."

Technologies Used
Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

NLP: spaCy

Document Indexing: Whoosh

Data Sources: Official documentation of Segment, mParticle, Lytics, and Zeotap.

Contributing
Contributions are welcome! If you'd like to improve the chatbot, follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Submit a pull request with a detailed description of your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or feedback, please contact:

Bathala Akshay

Email: akshay.bathala20@gmail.com

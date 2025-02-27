import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def process_question(question):
    """
    Process user question to extract intent and CDP platform.
    """
    doc = nlp(question.lower())
    
    # Identify CDP platform
    cdps = ["segment", "mparticle", "lytics", "zeotap"]
    cdp = None
    for token in doc:
        if token.text in cdps:
            cdp = token.text
            break
    
    # Identify intent (simplified for demo)
    intent = " ".join([token.text for token in doc if token.is_alpha and token.text not in cdps])
    
    return intent, cdp
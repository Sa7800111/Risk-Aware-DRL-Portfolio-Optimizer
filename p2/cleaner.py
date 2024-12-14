import re
import string

class TextCleaner:
    def __init__(self):
        self.stop_words = set(["the", "a", "an", "and", "or", "but"])

    def clean_headline(self, text: str) -> str:
        text = text.lower()
        text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
        text = " ".join([word for word in text.split() if word not in self.stop_words])
        return text.strip()

    def remove_noise(self, body: str) -> str:
        body = re.sub(r'https?://\S+', '', body)
        body = re.sub(r'\d+', ' <NUM> ', body)
        return body
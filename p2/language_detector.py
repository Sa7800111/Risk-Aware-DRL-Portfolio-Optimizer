from langdetect import detect

class LanguageFilter:
    def is_english(self, text: str) -> bool:
        try:
            return detect(text) == 'en'
        except:
            return False
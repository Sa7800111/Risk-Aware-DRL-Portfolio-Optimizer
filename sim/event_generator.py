class MarketEventGen:
    def generate_news_impact(self, sentiment: float):
        return {
            "type": "NEWS_EVENT",
            "impact_vector": [sentiment * 0.5, abs(sentiment) * 0.2]
        }
import asyncio
from hume import HumeStreamClient
from hume.models.config import LanguageConfig
import os
import certifi


os.environ["SSL_CERT_FILE"] = certifi.where()

async def get_sentiment_scores(sentences):
    # Initialize the HumeStreamClient with your API key
    client = HumeStreamClient("GQDwE1zvBBBSkarwCtgGN26LGbDs8KhVJYnXcyIVq70nGwqx")

    config = LanguageConfig()
    async with client.connect([config]) as socket:
        sentiment_scores = []
        for sentence in sentences:
            result = await socket.send_text(sentence)
            emotions = result["language"]["predictions"][0]["emotions"]
            scores = [entry['score'] for entry in emotions]
            sentiment_scores.append(scores)
        return sentiment_scores





def getScores(sentencesList):
    scores = asyncio.run(get_sentiment_scores(sentencesList))
    return scores

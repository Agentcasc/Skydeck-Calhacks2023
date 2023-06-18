import asyncio
from hume import HumeStreamClient
from hume.models.config import LanguageConfig,  NerConfig
import os
import certifi
from pinecone_handler import addvector

os.environ["SSL_CERT_FILE"] = certifi.where()

text = """

My group and I spent a total of seven hours preparing five hundred bagged lunches for the extensive homeless community at Oakland. Out of all the obstacles that could have halted our progress, rain was the last thing on our minds. We were lucky enough to distribute three hundred lunches before the rain began to relentlessly pour down on us. There were a few hours left of daylight before we would be able to eat Iftar for Ramadan, so, an overwhelming majority of our group wanted to call it a day. However, there was still a large number of unsheltered and hungry homeless people throughout the city, and I could not bear to let all that food go to waste. So, I raced to one of our nearest vans, grabbed a bullhorn, and yelled to gather the attention of as many people as possible. I instructed them to form lines in front of our eleven vans in order to take everybody to the nearest homeless shelters with the promise of food and entertainment. We went to six other heavily concentrated areas to do the same thing, and within just five hours, nearly five hundred homeless individuals were transported.

This event is one of the dozens of community service projects I’ve performed in my role as vice-president of the youth faction of the Sudanese Association of Northern California (SANC). This Oakland food drive has left me with a sense of clarity of what it takes to get a project, event, or any other endeavor accomplished. The food drive was obviously a success, but what made this particularly memorable is the email the president of SANC sent me the following day: “You have a keen ability to synthesize and communicate anything quickly and effectively.” I realized the explicit connection between my forensics (speech and debate) career and my community service: the power that I carry in my voice can motivate others to do good. I have tried to apply this insight into each new endeavor since.

"""






async def main():
    # Initialize the HumeStreamClient with your API key
    client = HumeStreamClient("GQDwE1zvBBBSkarwCtgGN26LGbDs8KhVJYnXcyIVq70nGwqx")

    config = LanguageConfig()
    async with client.connect([config]) as socket:
        result = await socket.send_text(text)
        emotions = result["language"]["predictions"][0]["emotions"]
        print(emotions)
        numbers = [entry['score'] for entry in emotions]
        print(numbers)
        # addvector("UCLA-2", numbers, "pathways")









asyncio.run(main())




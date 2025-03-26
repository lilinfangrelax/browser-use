import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent

"""
load_dotenv()

# Initialize the model
llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.0,
)
task = 'Find the founders of browser-use and draft them a short personalized message'

agent = Agent(task=task, llm=llm)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())
"""

api_key = os.getenv('Silicon_Cloud_API_KEY')
base_url = os.getenv('Base_URL')
model = os.getenv('Model')

llm = ChatOpenAI(model=model, api_key=api_key, base_url=base_url)

async def main():
    agent = Agent(
        task="获取区块链CFX的价格",
        llm=llm,
        use_vision=False,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())

from crewai import Agent, LLM
from tools.news_tool import get_stock_news

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

news_agent = Agent(
    role="Financial News Sentiment Analyst",
    goal="Analyze recent stock-related news headlines and determine overall sentiment impact.",
    backstory=(
        "You are an expert in financial news interpretation. "
        "You evaluate whether news headlines suggest positive, "
        "negative, or neutral impact on stock performance."
    ),
    tools=[get_stock_news],
    llm=llm,
    verbose=True
)

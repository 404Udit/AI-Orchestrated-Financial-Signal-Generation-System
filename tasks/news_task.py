from crewai import Task
from agents.news_agent import news_agent

news_analysis = Task(
    description=(
        "Use the Stock News Fetch Tool to retrieve recent headlines for {stock}. "
        "Analyze overall sentiment impact on the stock price.\n\n"
    ),
    expected_output=(
        "Return STRICT JSON in format:\n"
        "{\n"
        '  "sentiment": "Positive | Neutral | Negative",\n'
        '  "confidence": float (0-1),\n'
        '  "summary": "Short explanation"\n'
        "}"
    ),
    agent=news_agent
)

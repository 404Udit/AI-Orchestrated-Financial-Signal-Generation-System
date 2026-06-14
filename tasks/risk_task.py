from crewai import Task
from agents.risk_agent import risk_agent
from tasks.analyse_task import get_stock_analysis
from tasks.news_task import news_analysis

risk_assessment = Task(
    description=(
        "Using BOTH the analyst report (technical indicators) and the news sentiment report, "
        "evaluate the overall stock risk level.\n\n"
        "- High volatility increases risk.\n"
        "- Bearish trend increases risk.\n"
        "- Negative news sentiment increases risk.\n"
        "- Positive sentiment may reduce risk.\n\n"
        "Return a structured assessment of overall risk level."
    ),
    expected_output=(
        "Return STRICT JSON:\n"
        "{\n"
          '  "risk_level": "Low | Medium | High",\n'
          '  "risk_reasoning": "..."\n'
        "}"
    ),
    agent=risk_agent,
    context=[get_stock_analysis,news_analysis]
)

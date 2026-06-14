from crewai import Task
from agents.analyst_agent import analyst_agent

get_stock_analysis = Task(
    description=(
        "Use the Live Stock Information Tool to fetch stock data for {stock}.\n"
        "- If end_date is provided, you MUST pass end_date exactly as given.\n"
        "- Do NOT assume current date.\n"
        "- Do NOT access any future information.\n\n"
        "Interpret trend, volatility, and moving averages.\n"
        "Base your reasoning strictly on tool output."
    ),
    expected_output=(
        "Return STRICT JSON in the following format:\n"
        "{\n"
        '  "stock": "...",\n'
        '  "current_price": float,\n'
        '  "trend": "Bullish | Bearish",\n'
        '  "volatility": float,\n'
        '  "market_summary": "string"\n'
        "}"
    ),
    agent=analyst_agent
)

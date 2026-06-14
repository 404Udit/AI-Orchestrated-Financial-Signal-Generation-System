from crewai import Task
from agents.trader_agent import trader_agent
from tasks.analyse_task import get_stock_analysis
from tasks.risk_task import risk_assessment

trade_decision = Task(
    description=(
        "Using both analyst report and risk assessment, "
        "make final trading decision."
    ),
    expected_output=(
        "Return STRICT JSON:\n"
        "{\n"
          '  "decision": "BUY | SELL | HOLD",\n'
          ' "confidence_score": 0-1,\n'
          '  "risk_level": "Low | Medium | High",\n'
          ' "justification": "..."\n'
        "}"
    ),
    agent=trader_agent,
    context=[get_stock_analysis, risk_assessment]
)

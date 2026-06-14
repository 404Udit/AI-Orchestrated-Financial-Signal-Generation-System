from crewai import Crew

# impor tthe agents and tasks we have created
from tasks.analyse_task import get_stock_analysis
from tasks.trade_task import trade_decision
from tasks.risk_task import risk_assessment
from tasks.news_task import news_analysis
from agents.analyst_agent import analyst_agent
from agents.trader_agent import trader_agent
from agents.risk_agent import risk_agent
from agents.news_agent import news_agent


Stock_Crew = Crew(
    agents=[analyst_agent,news_agent, risk_agent, trader_agent],
    tasks=[get_stock_analysis,news_analysis, risk_assessment, trade_decision],
    verbose=True
)

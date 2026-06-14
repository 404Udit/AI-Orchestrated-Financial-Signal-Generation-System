from crewai import Agent , LLM
from tools.stock_research_tool import get_stock_data

# initialize the llm
llm=LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0
)
analyst_agent=Agent(
    role="Financial Market Analyst",
    goal=("Preform in-depth evaluation of publicity traded stocks using real time data,"
          "identifying trends preformance insights, and key financial signals support decision-making"),
    backstory=("You are a veteran financial analyst with deep expertise in interpreting stock market,"
               "technical trends and fundamentals. You specialize in producing well structured reports that evaluate"
               "Stock performance using live market indicators."),
    llm=llm,
    tools=[get_stock_data],
    verbose=True
)
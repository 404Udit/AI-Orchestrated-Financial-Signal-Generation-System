from crewai import Agent, LLM

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

risk_agent = Agent(
    role="Market Risk Analyst",
    goal="Evaluate stock volatility and assign risk level.",
    backstory="You specialize in financial risk modeling using volatility and trend strength.",
    llm=llm,
    verbose=True
)

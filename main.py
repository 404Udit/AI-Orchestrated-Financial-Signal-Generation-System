from dotenv import load_dotenv
from crew import Stock_Crew

load_dotenv()
def run(stock:str):
    result=Stock_Crew.kickoff(inputs={"stock":stock})
    print(result)

if __name__=="__main__":
    run("TESLA")
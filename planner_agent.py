#Planner Agent: Which demands the structured output from the LLM. Output should contain List of Searches LLM intends to perform
#Each Search object should contain the reson ( As these models are good with reasoning) and query itself. 
from agents import Agent,trace, Runner
from pydantic import BaseModel, Field
import asyncio

no_of_searches = 5
model_name = "gpt-5.4-mini"

class WebSearchItem(BaseModel): 
    reason: str = Field(description = "Your reasoning for why this search is important to the query")
    query: str = Field(description="The search term used for the websearch")

class WebSearchHeader(BaseModel): 
    searches: list[WebSearchItem]

WebSearchHeader.model_json_schema()

lo_plnr_instruction = f""" - You are a Research Assistant. Given the search term, come up with web searches
to perform to best answer the query. Limit Output to {no_of_searches} searches"""

#Let's build the planner agent
lo_planner_agent = Agent(name= "Planner Agent", instructions=lo_plnr_instruction,model=model_name, output_type=WebSearchHeader)

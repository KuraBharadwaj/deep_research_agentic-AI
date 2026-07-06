from pydantic import BaseModel, Field
from agents import Agent


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report")
    follow_up_questions: list[str] = Field(description="Suggested topics to research further")

model_name = "gpt-5.4-mini"
lv_write_instructions = f"""
You are a senior researcher tasked with writing a cohesive report for a research query. 
You will be provided with the original query and some research. 
Generate a comprehensive report based on research and query. 
The final output should be in markdown format, and it should be length and detailed. Aim for 
5-10 pages of content atleast 1000 words"""

lo_writer_agent = Agent(name="Writing Expert", instructions=lv_write_instructions, model= model_name, 
                            output_type=ReportData)
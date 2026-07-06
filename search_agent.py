from agents import Agent, ModelSettings, WebSearchTool

model_name = "gpt-5.4-mini"
tools_required = ModelSettings(tool_choice="required")
lv_srch_instruction = f""" - You are a Research assistant. Given the search term, you search the web for that term and produce concise summary
                           - The summary must be 2 to 3 paragraphs and less than 300 words. 
                           - Capture the main points and the succint. 
                           - Reply only with Summary
                           - Search only from trusted websites not from random social media posts. """
lo_search_agent = Agent(name="Search Agent", instructions=lv_srch_instruction, model= model_name, tools =[WebSearchTool()] )


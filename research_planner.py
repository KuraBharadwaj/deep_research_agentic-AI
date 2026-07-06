from agents import trace, Runner
from planner_agent import lo_planner_agent
from search_agent import lo_search_agent
from writer_agent import lo_writer_agent
from push_agent import lo_sender_agent
import asyncio


class Research_Planner: 
    
    async def run_show(self,query_tsk): 
        usr_task = query_tsk
        with trace("Showtime - Agents Orchestration"):   
            yield ("status: Planning searches...")
            srch_results = await self.call_planner_agent(usr_task)
            yield ("status: Search results secured")
            yield ("status: Writing detailed report...")
            write_results = await self.call_writer_agent(usr_task,srch_results)
            yield ("status : Report ready")
            yield ("status: Sending notification...")
            r = await Runner.run(lo_sender_agent,input = write_results.markdown_report)
            yield ("status: All tasks complete")
            yield r.final_output

    async def call_search_agent(self, w):
        input_msg = f"Search term: {w.query}\nReason for searching: {w.reason}"
        srch_result = await Runner.run(lo_search_agent, input = input_msg)
        return srch_result.final_output

    #Next step is to pass the tasks from planner agent to websearch tool. 
    async def call_planner_agent(self, usr_task): 
        #Define the planner agent
        runner_result = await Runner.run(lo_planner_agent, input = usr_task)
        web_srch_tasks = runner_result.final_output.searches
        #Loop through web_srch_tasks and use the search tool to search the web. 
        srch_tasks = [self.call_search_agent(w) for w in web_srch_tasks]
        srch_results = await asyncio.gather(*srch_tasks)
        return srch_results

    async def call_writer_agent(self, query: str, results): 
        input_msg = f"""Query to the research: {query} and
        \n Research: {results} """
        write_results = await Runner.run(lo_writer_agent,input = input_msg)
        return write_results.final_output


if __name__ == "__main__": 
    lo_research_planner = Research_Planner()
    asyncio.run(lo_research_planner.run_show())




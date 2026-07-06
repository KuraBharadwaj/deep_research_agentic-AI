import gradio as gr
from dotenv import load_dotenv
from research_planner import Research_Planner

load_dotenv(override=True)

async def run(query:str):
    planner = Research_Planner() 
    async for status_update in planner.run_show(query_tsk=query):
        yield status_update

with gr.Blocks() as ui:
    query_textbox = gr.Textbox(label="What topic you would like to research")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")

    run_button.click(run,inputs=query_textbox,outputs = report)
    query_textbox.submit(run,inputs = query_textbox, outputs = report)

ui.launch(theme=gr.themes.Default(primary_hue="sky"))
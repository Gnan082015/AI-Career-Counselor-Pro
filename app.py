import gradio as gr
from resume_parser import extract_text
import ai_engine as ai

def safe_resume(file):
    if file is None:
        return "⚠️ Upload resume"
    return ai.resume_analysis(extract_text(file))

def safe_jobs(file):
    if file is None:
        return "⚠️ Upload resume"
    return ai.job_matching(extract_text(file))

with gr.Blocks(theme=gr.themes.Soft()) as app:

    gr.Markdown("# 🚀 AI Career Counselor Pro")

    with gr.Tabs():

        # 🎯 Career Tab
        with gr.Tab("🎯 Career"):
            inp = gr.Textbox()
            out = gr.Textbox()
            gr.Button("Analyze").click(ai.career_advice, inp, out)

        # 📄 Resume Tab
        with gr.Tab("📄 Resume"):
            file = gr.File()
            out2 = gr.Textbox()
            gr.Button("Analyze").click(safe_resume, file, out2)

        # 📚 Skills Tab
        with gr.Tab("📚 Skills"):
            goal = gr.Textbox()
            out3 = gr.Textbox()
            gr.Button("Get Plan").click(ai.skill_recommendation, goal, out3)

        # 💼 Jobs Tab
        with gr.Tab("💼 Jobs"):
            file2 = gr.File()
            out4 = gr.Textbox()
            gr.Button("Match").click(safe_jobs, file2, out4)

        # 🎤 Interview Tab (FIXED)
        with gr.Tab("🎤 Interview"):

            gr.Markdown("### 🎯 Choose Interview Mode")

            mode = gr.Dropdown(
                ["Text Interview", "Camera Interview"],
                label="Select Mode"
            )

            role = gr.Textbox(label="Enter Role")

            output = gr.Textbox(label="Result")

            def handle_mode(mode, role):
                if mode == "Text Interview":
                    return ai.interview_questions(role)
                else:
                    return ai.yolo_confidence()

            btn = gr.Button("Start")

            btn.click(
                fn=handle_mode,
                inputs=[mode, role],
                outputs=output
            )

app.launch(share=True)
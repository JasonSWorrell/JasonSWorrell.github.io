import gradio as gr

class GradioUI:
    def __init__(self, SUMMARIZER, NOTE_TAKER, TRANSCRIBER):
        self.summarizer = SUMMARIZER
        self.note_taker = NOTE_TAKER
        self.transcriber = TRANSCRIBER

        self.demo = gr.Blocks(theme=gr.themes.Soft())
        
        self.demo.Markdown("# 📝 AI Note-Taker Assistant")
        self.demo.Markdown("Record a meeting or upload an audio file to generate instant transcripts and action items.")    
        self.demo.Row().Column().Audio(sources=["microphone", "upload"], 
                                       type="filepath", 
                                       label="Input Audio Source"
                                       )       

        with self.demo.Row():
            with self.demo.Column():
                self.audio_input = gr.Audio(sources=["microphone", "upload"], type="filepath", label="Input Audio Source")
                self.submit_btn = gr.Button("Generate Notes", variant="primary")
                self.filename = gr.Textbox(label="File Name", placeholder="Name of file", lines=1, value="AI_Notes")
                self.PDF_btn = gr.Button("Generate Notes and PDF", variant="primary")
            with self.demo.Column():
                self.transcript_output = gr.Textbox(label="Full Transcript", lines=8)
                self.summary_output = gr.Textbox(label="AI Summary & Action Items", lines=6)
                self.notes_output = gr.Textbox(label="AI Notes", lines=12)

            self.submit_btn.click(
                fn=self.process_audio,
                inputs=[self.filename, self.audio_input],
                outputs=[self.transcript_output, self.summary_output, self.notes_output]
            )

            self.PDF_btn.click(
                fn=self.doc,
                inputs=[self.filename, self.audio_input],
                outputs=[self.transcript_output, self.summary_output, self.notes_output]
            )   

class KinterUI:
    def __init__(self, SUMMARIZER, NOTE_TAKER, TRANSCRIBER):
        self.summarizer = SUMMARIZER
        self.note_taker = NOTE_TAKER
        self.transcriber = TRANSCRIBER
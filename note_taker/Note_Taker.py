import gradio as gr
import torch
from pydub import AudioSegment
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM
from docx import Document
# 1. Initialize Speech-to-Text Pipeline 
transcriber = pipeline(
    "automatic-speech-recognition", 
    return_timestamps=True,
    model="openai/whisper-small", 
    device="cuda" if torch.cuda.is_available() else "cpu"
)

# 2. Initialize Summarization model
summary_model_name = "knkarthick/MEETING_SUMMARY"
tokenizer = AutoTokenizer.from_pretrained(summary_model_name)
summarizer = AutoModelForSeq2SeqLM.from_pretrained(
    summary_model_name,
    device_map="auto"
)

# 2.c Initialize second style notes taker
notes_model_name = "meta-llama/Llama-3.1-8B-Instruct"
notes_tokenizer = AutoTokenizer.from_pretrained(notes_model_name)
note_taker = AutoModelForCausalLM.from_pretrained(notes_model_name).to("cuda")

# 3. Process source audio and document into notes. 
def process_audio(audio_path): # audio_path is the input audio, may need to be a few seconds or few minutes at a time. 
    if audio_path is None:
        return "No audio source found."
    try:
        # Takeing the Audio from source and writing down every word.
        transcription_result = transcriber(audio_path)
        transcript = transcription_result["text"]
    except Exception as e:
        return f"Error during transcription: {str(e)}", ""

        # Summarize Text
    try: 
        inputs= tokenizer(
            f"Summary: {transcript}",
            return_tensors="pt",
            max_length=1024,
            truncation=True,
        ).to(summarizer.device)

        summary_ids= summarizer.generate(
            inputs["input_ids"],
            num_beams=6,
            min_length=30,
            max_length=1024,
            early_stopping=True
        )
        summary = tokenizer.decode(summary_ids[0], 
                                   skip_special_tokens=True
        )
    except Exception as e:
        summary = f"Error During Summary: {str(e)}"



    # Format into Notes
    try:
        note_paper=[
            {"role": "system", "content": """You are an expert analyst. Your task is to extract information from transcripts and output a strict 5-level hierarchical outline.
                                            You MUST use this exact numbering and indentation format:
                                            1. Subject topic
                                                A. First Major point
                                                    1. Supporting point - this is a really really long Supporting Point it goes 
                                                       to the end and all the way down to the following line.
                                                        a. Detail
                                                        b. Detail
                                                        c. Detail
                                                            1. Sub-detail
                                                            2. Sub-detail
                                                            3. Sub-detail
                                                    2. Supporting point
                                                        a. Detail - this is a really really long detail it goes to the end and all
                                                           the way down to the following line.
                                                        b. Detail
                                                        c. Detail
                                                            1. Sub-detail
                                                            2. Sub-detail
                                                            3. Sub-detail - this is a really really long Sub-detail it goes to the 
                                                               end and all the way down to the following line. It even goes down to
                                                               another line. This is the formate that should be used for multiple 
                                                               lines.

                                            Not all fields must be used but his is the format that must be followed. 
                                            Numbering and lettering follow traditional formats. For example: Supporting Point 1 should not have 5 Sub-Detail a's, 
                                            each sub detail should follow the alphabet and be labeled from a to b to c to d to e and so forth.
                                            each indented Topic, Point, Detail or Sub-detail should be completely contained in its own indention.
                                            If if consume two or more lines, each line after the first line of that indention should follow the same indention of the previous, as the examples
                                            above illustrate. (The above is just an example. Stay within the margins of the page.)"""},
            {"role": "user", "content": transcript},
        ]
        
        notes_input_tokens = notes_tokenizer.apply_chat_template(
            note_paper, 
            tokenize=True, 
            add_generation_prompt=True, 
            return_tensors="pt",
            return_dict=True,
            max_tokens = 4000,
        ).to(note_taker.device)
    
        output_ids = note_taker.generate(
            **notes_input_tokens,
            max_new_tokens=512,
            do_sample=False
        )

        generated_tokens = output_ids[0][notes_input_tokens["input_ids"].shape[1]:]
        notes = notes_tokenizer.decode(generated_tokens, skip_special_tokens=True)
    except Exception as e:
            notes = f"Error During Notes: {str(e)}"

    
    return transcript, summary, notes

def doc(filename,audio_path):
    transcription, summary, txt = process_audio(audio_path)

    document = Document()
    document.add_heading(f'{filename}', 0)

    document.add_paragraph(f"Summary: {summary}")
    document.add_paragraph(txt)
    document.save(f'Notes/{filename}.docx')
    return transcription, summary, txt

# 3. Build UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📝 AI Note-Taker Assistant")
    gr.Markdown("Record a meeting or upload an audio file to generate instant transcripts and action items.")
    
    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(sources=["microphone", "upload"], type="filepath", label="Input Audio Source")
            submit_btn = gr.Button("Generate Notes", variant="primary")
            filename = gr.Textbox(label="File Name", placeholder="Name of file", lines=1, value="AI_Notes")
            PDF_btn = gr.Button("Generate Notes and PDF", variant="primary")

            
        with gr.Column():
            transcript_output = gr.Textbox(label="Full Transcript", lines=8)
            summary_output = gr.Textbox(label="AI Summary & Action Items", lines=6)
            notes_output = gr.Textbox(label="AI Notes", lines=12)

            
    submit_btn.click(
        fn=process_audio,
        inputs=[filename, audio_input],
        outputs=[transcript_output, summary_output, notes_output]
    )

    PDF_btn.click(
        fn=doc,
        inputs=[filename, audio_input],
        outputs=[transcript_output, summary_output, notes_output]
    )



# 4. Launch

if __name__ == "__main__":
    demo.launch()
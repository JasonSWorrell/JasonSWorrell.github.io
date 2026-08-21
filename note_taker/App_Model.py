from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM


class AppModel():
    model:str
    device:str

    def __init__(self, MODEL:str, DEVICE:str):
        self.model = MODEL
        self.device = DEVICE
        self.tokenizer = AutoTokenizer.from_pretrained(self.model)

class Summarizer(AppModel):
    def __init__(self, MODEL:str, DEVICE:str):
        super().__init__(MODEL, DEVICE)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model, device_map="auto")

    def process_transcription(self, transcript:str):
        try:
            inputs= self.tokenizer(
                f"Summary: {transcript}",
                return_tensors="pt",
                max_length=1024,
                truncation=True,
            ).to(self.model.device)

            ids= self.model.generate(
                inputs["input_ids"],
                num_beams=6,
                min_length=30,
                max_length=1024,
                early_stopping=True
            )
            summary = self.tokenizer.decode(ids[0], skip_special_tokens=True)

        except Exception as e:
            summary = f"Error During Summary: {str(e)}"
        
        return summary
    

class NoteTaker(AppModel):
    def __init__(self, MODEL:str, DEVICE:str):
        super().__init__(MODEL, DEVICE)
        self.model = AutoModelForCausalLM.from_pretrained(self.model).to(self.device)

    def process_transcription(self, transcript:str):
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
        
        inputs= self.tokenizer(
            note_paper, 
            tokenize=True, 
            add_generation_prompt=True, 
            return_tensors="pt",
            return_dict=True,
            max_tokens = 4000,
        ).to(self.device)

        ids = self.model.generate(
                    **inputs,
                    max_new_tokens=512,
                    do_sample=False
                )
        tokens =ids[0][inputs["ids"].shape[1]:]
        notes = self.tokenizer.decode(tokens[0], skip_special_tokens=True)
        return notes

class Transcriber(AppModel):
    def __init__(self, MODEL:str, DEVICE:str):
        super().__init__(MODEL, DEVICE)
        self.model = pipeline(
            "automatic-speech-recognition", 
            return_timestamps=True,
            model=self.model, 
            device=self.device
        )

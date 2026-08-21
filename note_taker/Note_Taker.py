
from UI import AppGradioUI, AppKinterUI
import torch
from pydub import AudioSegment
from docx import Document
import sys




def main():
    if len(sys.argv) > 1:
        return "Acceptable commandline arguments are kinter or gradio. Otherwise please run the script without any command line arguments and the Gradio UI will launch automatically."
    else:
        if len(sys.argv) == 1:            
                
              
            if sys.argv[0] == "gradio":
                app = AppGradioUI()
            if sys.argv[0] == "kinter":
                app = AppKinterUI()
            else:
                print("The provided GUI argument was invalid. ")
                app = AppGradioUI()
            app.demo.launch()
        if len(sys.argv) == None:
            app = AppGradioUI()
            app.demo.launch()




if __name__ == "__main__":
    main()

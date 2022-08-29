import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import speech_recognition as sr
from googletrans import Translator, constants
from pprint import pprint



root = tk.Tk()
canvas = tk.Canvas(root,height=300, width=800)
canvas.grid(columnspan =3, rowspan =6)

# image
logo = Image.open('language_logo.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="select a sound file (wav format) on your computer \n to convert to text", font = 'arial')
instructions.grid(columnspan = 3, column=0, row=1)


#browse
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text,command=lambda:open_file(), font = 'arial',bg='#20bebe',fg="white", height=1, width=15)
browse_text.set('Browse')
browse_btn.grid(column=1,row =2)



canvas = tk.Canvas(root,height=250, width=800)
canvas.grid(columnspan =3)

root.grid_rowconfigure(4, minsize=10)  # Here


def open_file():
    browse_text.set('Loading...')
    file = askopenfile(parent =root, mode = 'rb', title = "choose a file", filetype= [("Sound file", "*.wav")])
    if file:
        r = sr.Recognizer()

        with sr.AudioFile(file) as source:
            audio_text = r.listen(source)
        try:

            # using google speech recognition
            text = r.recognize_google(audio_text, language="zh")
            print('Converting audio transcripts into text ...')
            print(text)
            f = open("voicetotext4.txt", 'a+', encoding="utf-8")
            f.write(text)
            f.close()


        except:
            print('Sorry.. run again...')


        page = "Converted text from sound file :" + text
        page_content = page

        #my_label = tk.Label(root, text="Converted text from sound",font = 'arial')
        #my_label.grid(column=1,row=3)
        text_box = tk.Text(root, height=8, width=30, padx=10, pady=10)
        text_box.insert(1.0, page_content)
        text_box.tag_config('center', justify='center')
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(column=1, row=5)

        translator = Translator()
        translation = translator.translate(text)
        converted_content = f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})"


        text_box = tk.Text(root, height=8, width=30, padx=10, pady=10)
        text_box.insert(1.0, converted_content)
        text_box.tag_config('center', justify='center')
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(column=1, row=6)


        browse_text.set('Browse')

root.mainloop()

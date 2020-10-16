import pyttsx3    # Package to create audio files
import os
import fitz       # Package to read PDF files


def save_audio(file):
    # Reading PDF file
    with fitz.open(file) as doc:
        text = ''
        for page in doc:
            text += page.getText()
    
    # Deleting all useless whitespaces
    text = text.strip()

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('volume', 1)           # Volume of speech
    engine.setProperty('rate', 190)           # Rate of speech (speed)
    engine.setProperty('voice', voices[2].id) # 0 index for russian, 1-3 for english speech

    if len(text) < 180000:                             # If the text is small -> save to one file
        engine.save_to_file(text, text[:10]+'.mp3')

    else:                                              # Else create multiple audio files
        os.makedirs(text[:10])
        os.chdir(text[:10])

        for part in range(0, len(text), 50000):
            print(f'From {part} to {part+50000}')
            engine.save_to_file(text[part:part+50000],
                                str(part//50000)+' Part.mp3')

    engine.runAndWait()
    engine.stop()


save_audio('sample.pdf')

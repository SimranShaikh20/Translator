import tkinter as tk
from deep_translator import GoogleTranslator

def translate():
    src_lang = src_var.get()
    dest_lang = dest_var.get()
    text = src_text.get("1.0", "end-1c")
    translator = GoogleTranslator(source=src_lang, target=dest_lang)
    result = translator.translate(text)
    dest_text.delete("1.0", "end")
    dest_text.insert("end", result)

root = tk.Tk()
root.title("Language Translator")

src_var = tk.StringVar()
dest_var = tk.StringVar()

src_label = tk.Label(root, text="Source Language")
src_label.pack()
src_option = tk.OptionMenu(root, src_var, "english", "franch", "hindi", "gujarati")
src_option.pack()

dest_label = tk.Label(root, text="Destination Language")
dest_label.pack()
dest_option = tk.OptionMenu(root, dest_var, "english", "franch", "hindi", "gujarati")
dest_option.pack()

src_text_label = tk.Label(root, text="Source Text")
src_text_label.pack()
src_text = tk.Text(root, height=10, width=40)
src_text.pack()

translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack()

dest_text_label = tk.Label(root, text="Destination Text")
dest_text_label.pack()
dest_text = tk.Text(root, height=10, width=40)
dest_text.pack()

root.mainloop()
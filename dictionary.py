#This program translates words in the specified languages to English

from tkinter import *

def translate():
    word = entry.get()
    lang = language.get()

    translation = dictionary.get(lang, {}).get(word)
    if translation:
      result_label.config(text="English Translation: " + translation)    
    else:
      result_label.config(text="No translation found.") 

# dictionary with some words and translations
dictionary = {
    "French": {
        "bonjour": "good morning", "merci": "thank you", "au revoir": "goodbye",
        "oui": "yes", "non": "no", "bon": "good", "grand": "big", "petit": "small",
        "maison": "house", "chien": "dog", "chat": "cat", "vie": "life", "eau": "water",
        "soleil": "sun", "lune": "moon", "viens": "come", "humaine": "human", "feu": "fire",
        "traduire": "translate", "chirurgie": "surgery"
    },
    "Spanish": {
        "hola": "hello", "gracias": "thank you", "adios": "goodbye", "si": "yes",
        "no": "no", "casa": "house", "aqua": "water", "vida": "life", "sol": "sun",
        "grande": "big", "bueno": "good", "malo": "bad", "perro": "dog", "amor": "love",
        "gate": "cat", "feliz": "happy", "cielo": "heaven", "traducir": "translate", "fuego": "fire",
        "humana": "human"
    },
  "Hausa": { "sannu": "hello", "nagode": "thank you", "zo": "come", "sai da safe": "goodbye (morning)",
     "eh": "yes", "karami": "small", "muni": "bad", "girma": "big", "rayuwa": "life", "rana": "sun", "ruwa": "water",
     "kyau": "good", "kare": "dog", "mukule": "cat", "likita": "doctor", "fadi": "fall", "alkawari": "appointment",
     "wani": "somebody", "mutum": "man", "mache": "woman",
    },
  "Yoruba":  {"wa": "come", "iwo": "you", "oruko": "name",  "omo": "child", "ile": "house",
    "oloye": "king",  "agbara": "strength", "omolode": "beautiful",  "eniyan": "person", "oko": "husband",
    "iyawo": "wife", "ounje": "food","omi": "water", "orun": "heaven", "aye": "earth", "okan": "heart", "owo": "hand",
    "oko": "farm", "ojo": "day", "orun": "sleep" 
},

  "Igbo": { "ndewo": "Hello", "daalu": "Thank you", "biko": "Please", "ezigbo ututu": "Good morning",
    "ezigbo ehihie": "Good afternoon", "ezigbo mgbede": "Good evening", "Ka o di": "How are you?",
    "o di mma": "I am fine", "Gini ka i naeme?": "What are you doing?","aga m": "I am going", "ebe a": "Here", "ebe ahu": "There",
    "ee": "Yes", "mba": "No", "aha m bu": "My name is", "kedu aha gi?": "What is your name?", "nri": "Food",
    "mmiri": "Water", "ulo": "House", "nwoke": "Man/Male"
    }

}

window = Tk()
window.title("Multi-Language Dictionary")
window.configure(bg="green")

languages = ["French", "Spanish", "Hausa", "Yoruba", "Igbo"] 
language = StringVar(window)
language.set("Select Language") 
language_menu = OptionMenu(window, language, *languages)
language_menu.config(bg="lightblue", fg="black")
language_menu.pack(pady=10)

words_label = Label(window, text="Enter Word:", bg="green", fg="black")
words_label.pack(pady=5)

entry = Entry(window, bg="white", fg="black")
entry.pack(pady=5)

translate_button = Button(window, text="Translate", command=translate)
translate_button.pack(pady=10)

result_label = Label(window, text="", bg="green", fg="black")
result_label.pack(pady=5)

window.mainloop()

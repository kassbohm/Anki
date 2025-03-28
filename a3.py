#! /usr/bin/python3

# import anki
# import anki.collection
# from anki.importing.apkg import AnkiPackageImporter

from gtts import gTTS
import genanki
import random
import csv
from string import ascii_letters
from os import system
import codecs
# from googletrans import Translator
import itertools
from re import sub

from sys import argv


from TTS.api import TTS
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False, gpu=False)

# tts --list_models


models = ["coqui", "gtts"]

# help(anki.collection)
# exit()
# importer = AnkiPackageImporter(col=coll, file='path/to/your/deck.apkg')

# translator = Translator()

# tmp = translator.translate('mit etwas beginnen', dest='en')
# print(tmp.text)

# style = """
# .card {
#   font-size: 19px;
#   text-align: center;
#   color: #404040;
#   background-color: white;
#   b, strong {
#   color: red;
#   };
# }
# .replay-button svg path {
# stroke: white;
# fill: #404040;
# }
# """

style = """
.card {
  font-size: 19px;
  text-align: center;
  color: #ffffff;
  background-color: #282a36;
  b, strong {
  color: red;
  };
}
.replay-button svg path {
stroke: white;
fill: #404040;
}
"""

# Colors:
# Dark background = "#282a36"
# Less dark background = "#6272a4"

old = False


# level = "A1"
# level = "A2"
# level = "B1"
# level = "B2"
# level = "C1"
# level = "C2"

# Netzwerk_neu:
# A1.1:
# old = False

# level = "Adjektiv_02"
# blooket = False

# level = "Verb_01"
# blooket = True

# level = "Verb_02"
# blooket = True
# level = "Verb_02"
# blooket = True

# level = "Verb_trennbar"
# blooket = True

# level = "Verb_unregelm"
# blooket = True

# level = "Mix_01_A"
# blooket = False

# level = "Mix_01_B"
# blooket = False

# level = "Mix_01_C"
# blooket = False

# level = "Mix_03"
# blooket = True


# level = "Substantiv_01"
# blooket = True

# level = "Substantiv_02_A" 
# blooket = True

# level = "Substantiv_02_B" 
# blooket = True

# level = "Substantiv_03_A" 
# blooket = True

# level = "Substantiv_03_B" 
# blooket = True

# level = "Substantiv_04" 
# blooket = True

# level = "Datum_0"
# blooket = False

# level = "Datum_A"
# blooket = False

# level = "Datum_B"
# blooket = False

# level = "Datum_C"
# blooket = True

# level = "Datum_D"
# blooket = True

# level = "Datum_E"
# blooket = True


# level = "A1.1_Netzwerk_neu_01"
# level = "A1.1_Netzwerk_neu_Unr._Verb_Präsens"

# A1.2:
# level = "Netzwerk_neu_A1_07"
# level = "Netzwerk_neu_A1_08"
# level = "Netzwerk_neu_A1_09"
# level = "Netzwerk_neu_A1.2_Test"


tmp_file = argv[1]
blooket = True
if "Uhrzeit" in tmp_file:

    blooket = False

level = tmp_file[4:-4]

# if len(argv)==2:
#     tmp_file = argv[1]
# else:
#     tmp_file = "./txt/"+level + ".txt"
    
with open(tmp_file) as f:
    lines = [x.rstrip() for x in f]

if blooket:
    blooket_file = "./csv/" + level + "_Blooket" + ".csv"
    system("cp ./csv/x_start.csv " + blooket_file)

randint_deck = random.randint(100000000, 100000000000000000)
randint_model = random.randint(1000, 100000000)

tuples = []
media_files = []

# system("trash-put ./*.csv")
# system("cp ./template.txt " + blooket_file)

line_no = 0

for line in lines:
    line_no += 1

    if line[0:2] == "//":
        line_no -= 1
        continue

    line = line.split("§", maxsplit=1)

    img_word = line[0]

    if "|" in img_word:
        tmp = img_word.split("|")
        img = tmp[0]
        word = tmp[1]
    else:
        img = None
        word = img_word

    word_color = "#ffffff" # white

    if old:
        q = '<a style="color:DodgerBlue"; href="https://www.dwds.de/wb/'

    else:
        # q = '<a style="color:' + word_color + '"; href="https://www.verbformen.com/?w='
        q = '<a href="https://www.verbformen.com/?w='

    if "/" not in word:
        q += word
        q += '"style="color: white;";><u>'
        q += word
        q += "</u>"
    else:
        word = word.split("/")
        q += word[1]
        # q += '";><u>'
        q += '"style="color: white;";><u>'
        q += word[0]
        q += "</u>"
    q += "</a>"
    if level == "Datum_A" or level == "Datum_B" or level == "Datum_C" or level == "Datum_D":
        q = '<a style="color: #ffffff">'+word+'</a>' 
    if level[:7]=="W-Frage" or level[:4]=="Satz" :
        q = word 
    # print(q)
    # print(line)
    
    a = line[1]
    
    a = a.split(", =")
    english = a[1].replace("**","")


    tmp = a[1].split("**")
    if len(tmp[2]) != 0:
        # br = True
        br = False
    else:
        br = False

    a[1] = a[1].strip()
    a[1] = "<br>"+a[1]
    
    a[1] = a[1].replace("** ", "**", 1)

    a[1] = a[1].replace(
        "{",
        # '<br><font style="color: #bd93f9;">',
        '<br>'
    )
    a[1] = a[1].replace(
        "}",
        "",
    )

    # a[1] = a[1].replace("**", '<font style="color: #0090ff;">', 1)
    a[1] = a[1].replace("**", '<b><font style="color: #ffffff;">', 1)
    a[1] = a[1].replace("**", "</font></b> ", 1)
    # a[1] = a[1].replace("**", '<font style="color: #f1fa8c;">', 1)
    # a[1] = a[1].replace("**", "</font> ", 1)

    # a[1] = a[1].replace("**", '<font-weight: bold, font style="color: #f1fa8c;">', 1)
    # a[1] = a[1].replace("**", "</font> ", 1)

    # light blue = "#0090ff" 
    # green = "#50fa7b"
    # dark green = "#00FA9A"
    # 
    # pink = "#ff79c6"
    # purple = "#bd93f9"
    # yellow = "#"
    # orange = "#ff9600"
    # turquoise = "#00e4e4" 

    ac = a.copy()[0]

    tmp = ac.strip().split(" ")
    # print(tmp[1])
    if level[0:5] != "Datum":
        if tmp[0]=="der":
            tmp[1]='<b><font style="color: #1e90ff;">'+tmp[1]+"</font></b>" # 
        elif tmp[0]=="die":
            tmp[1]='<b><font style="color: #ff79c6;">'+tmp[1]+"</font></b>"
        elif tmp[0]=="das":
            tmp[1]='<b><font style="color: #1abc9c;">'+tmp[1]+"</font></b>"


    ac = " ".join(tmp)


    ac = ac.replace(
        "(((",
        '<font style="color: #bd93f9;">',
    )
    ac = ac.replace(
        ")))",
        "</font>",
    )

    ac = ac.replace(
        " **",
        ' <font style="color: #50fa7b;">', 
    )
    ac = ac.replace(
        "**",
        "</font>",
    )
    ac = ac.replace(
        "(",
        '<font style="color: #50fa7b;">',
    )
    ac = ac.replace(
        ")",
        "</font>",
    )
    ac = ac.replace(
        "[[[",
        '<u style="color: #ffb663;">',
    )
    ac = ac.replace(
        "]]]",
        "</u>",
    )

    ac = ac.replace(
        "[[",
        '<i style="italic; color: #ffb663;">',
    )
    ac = ac.replace(
        "]]",
        "</i>",
    )
    ac = ac.replace(
        "[",
        '<font style="color: #ffb663;">',
    )
    ac = ac.replace(
        "]",
        "</font>",
    )
    ac = ac.replace(
        "{{",
        '<font style="color: #bd93f9;">',
    )
    ac = ac.replace(
        "}}",
        "</font>",
    )
    ac = ac.replace(
        "{",
        # '<br><font style="color: #bd93f9;">',
        '<br><font style="color: #ffffff;">',
    )
    ac = ac.replace(
        "}",
        "</font>",
    )
    text = a[0]
    
    text = text.replace(
        "!Pause!",
        "!",
    )
    ac = ac.replace(
    "!Pause!",
    "", 
    )
    

    text = text.replace(
        " **",
        " ",
    )
    text = text.replace(
        "**",
        "",
    )
    text = text.replace(
        "(",
        "",
    )
    text = text.replace(
        ")",
        "",
    )
    text = text.replace(
        "[[",
        "",
    )
    text = text.replace(
        "]]",
        "",
    )
    text = text.replace(
        "[",
        "",
    )
    text = text.replace(
        "]",
        "",
    )
    text = text.replace(
        "{{",
        "",
    )
    text = text.replace(
        "}}",
        "",
    )
    text = text.replace(
        "{",
        "",
    )
    text = text.replace(
        "}",
        "",
    )

    text = text.strip()
    # acopy
    # acopy[1] = acopy[1].replace("**g**","<i style=\"color:Green;\">",1)
    # acopy[1] = acopy[1].replace("**g**","</i>",1)

    # a[0] = a[0].replace("**g**","<font style=\"color:Green;\">",1)
    # a[0] = a[0].replace("**g**","</font>",1)

    # a[0] = a[0][1:-1]
    # a[2] = a[2].replace("/", " oder ")

    # tts:
    print(line_no)
    # print(word)
    print(text)
    # exit()


    # write csv for Blooket:
    if blooket:
        months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        days = ["erste", "zweite", "dritte", "vierte", "fünfte", "sechste", "siebente", "achte", "neunte", "zehnte", \
               "elfte", "zwölfte", "dreizehnte", "vierzehnte", "fünfzehnte", "sechzehnte", "siebenzehnte", "achtzehnte", "neunzehnte", "zwanzigste", \
               "einundzwanzigste", "zweiundzwanzigste", "dreiundzwanzigste", "vierundzwanzigste", "fünfundzwanzigste", "sechsundzwanzigste", \
                "siebenundzwanzigste", "achtundzwanzigste", "neunundzwanzigste", "dreißigste", "einunddreißigste", "letzte"
                ]
        nouns = ["Semester", "Tag", "Monat", "Woche", "Jahr"]

        with open(blooket_file, mode="a") as f:
            eggs = csv.writer(f,
                              delimiter=",",
                              quotechar='"',
                              quoting=csv.QUOTE_MINIMAL)
            # if level == "Substantiv_01":
            #     tmp = text.split(" ")
            #     question = tmp[0] + " " + tmp[1]
            # else:
            question = word
            if level == "Substantiv_02_A" \
                    or level == "Substantiv_02_B"  \
                    or level == "Substantiv_01"    \
                    or level == "Substantiv_03_A"  \
                    or level == "Substantiv_03_B"  \
                    or level == "Substantiv_04_A"  \
                    or level == "Substantiv_04_B":    
                    
                tmp = text.split(" ")
                try:
                    idx = tmp.index("!")
                    tmp = tmp[:idx]
                except:
                    tmp = tmp
                
                tmp = " ".join(tmp)
                tmp = tmp.strip()
                # print(tmp)
                # exit()
                correct = tmp
            elif level == \
                    "Verb_01" or level == \
                    "Verb_02" or level == \
                    "Verb_trennbar" or level == \
                    "Verb_unregelm" or level == \
                    "Adjektiv_02" \
                    or level[0:4]=="Verb":
                tmp = text
                tmp = tmp.split("!")
                tmp = tmp[0]
                tmp = tmp.split("-")
                corrects = [tmp[0].strip(), tmp[1].strip()]
                if level ==  "Adjektiv_02":
                    correct = corrects[0]
                else:    
                    correct = random.choice(corrects)
            else:
                correct = text

            correct = correct.replace("kein Singular", "")
            correct = correct.replace("kein Plural", "")
            correct = correct.replace("kein Plural", "")

            # if level[:7]=="W-Frage":
            #     tmp = correct.split(".")
            #     corrects = [(tmp[0]+".").strip(), tmp[1].strip()+"."]
            #     correct = random.choice(corrects)

            indices = []
            for n, i in enumerate(correct):
                if i != " " and i != "-" and i !=",":
                    indices.append(n)

            # print(indices)

            # if level == "Datum_C":
            #     tmp = text
            #     correct=tmp
            #     tmp = correct.split(",")
            #     tmp = [tmp[0].strip(), tmp[1].strip(), tmp[2].strip()]
                
            #     wrong = []
            #     while len(wrong) != 3:
            #         idx = random.choice([0, 1, 2])
            #         rndm = random.choice(months)
            #         tmp_c = tmp.copy()
            #         while rndm not in tmp_c:
            #             tmp_c[idx]=rndm
            #             if tmp_c not in wrong:
            #                 wrong.append(tmp_c)
            #     t0, t1, t2 = ", ".join(wrong[0]), ", ".join(wrong[1]), ", ".join(wrong[2])
            #     row = [line_no, question.strip(), correct, t0, t1, t2, 10, "1"]    
            if level[0:5] == "Datum":
                tmp = text
                correct=tmp.split("=")[0]
                correct=tmp.split("!")[0]
                tmp = correct.split(" ")

                try:
                    tmp = [tmp[0].strip(), tmp[1].strip(), tmp[2].strip(), tmp[3].strip() ]
                except:
                    tmp = [tmp[0].strip(), tmp[1].strip(), tmp[2].strip()]
                # change = "months"
                if level == "Datum_G":
                    change = random.choice(["nouns", "days"])
                elif level == "Datum_E":
                    change = random.choice(["months"])
                    month_idx = 0
                else:
                    change = random.choice(["months", "days"])
                if change == "months":
                    wrong = []
                    while len(wrong) != 3:
                        idx = 1
                        # idx = month_idx
                        rndm = random.choice(months)
                        tmp_c = tmp.copy()
                        while rndm not in tmp_c:
                            tmp_c[idx]=rndm
                            if tmp_c not in wrong:
                                wrong.append(tmp_c)
                elif change == "days":
                    wrong = []
                    while len(wrong) != 3:
                        idx = 1
                        rndm = random.choice(days)
                        tmp_c = tmp.copy()
                        while rndm not in tmp_c:
                            tmp_c[idx]=rndm
                            if tmp_c not in wrong:
                                wrong.append(tmp_c)
                elif change == "nouns":
                    wrong = []
                    while len(wrong) != 3:
                        idx = 2
                        rndm = random.choice(nouns)
                        tmp_c = tmp.copy()
                        while rndm not in tmp_c:
                            tmp_c[idx]=rndm
                            if tmp_c not in wrong:
                                wrong.append(tmp_c)
                else:
                    exit()
                Y = [" ".join(wrong[0]), " ".join(wrong[1]), " ".join(wrong[2])]
                row = [line_no, question.strip(), correct, Y[0],Y[1],Y[2], 10, "1"]    
            else:
                X = []
                for i in range(8):  # make more than needed.
                    # sam = random.sample(indices, 2)
                    sam = random.sample(indices, 1)
                    letts = iter(random.sample(ascii_letters, 2))
                    lst = list(correct)
                    for ind in sam:
                        lst[ind] = next(letts).lower()
                    tmp = "".join(lst)
                    if tmp == question or tmp == correct:
                        continue
                    # print(tmp)
                    X.append(tmp)
                    Y = set(X)
                    Y = list(Y)
                    if len(Y)==3:
                        break
                english = english.split("{")[0]
                if level[:7]=="W-Frage":
                    row = [line_no, question.strip(), correct, Y[0], Y[1], Y[2], 10, "1"]
                else:
                    row = [line_no, question.strip() + " = " + english.strip(), correct, Y[0], Y[1], Y[2], 10, "1"]
            eggs.writerow(row)

    sound_fn = text + ".mp3"
    sound_fn = sound_fn.strip()
    media_files.append(sound_fn)

    if img:
        image_fn = "img/Uhr/" + img
        media_files.append(image_fn)
    else:
        pass
        # media_files.append(None)
    # Improve sounds:

    if "?" in text or "19" in text or "Uhr" in text: 
        model = "gtts"
    else:
        model = random.choice(models)

        # print(model)
    
    if model=="coqui":
        text = text.replace("siebente", "siehmte")
        text = text.replace("Siebente", "Siehmte")
        tmp = tts.tts_to_file(text=text+".", file_path=sound_fn)
    elif model == "gtts":
        text = text.replace(", log,", ", lohk,")
        text = text.replace(", grub,", ", gruhb,")
        text = text.replace(", stach,", ", staach,")
        text = text.replace(", sog,", ", sook,")
        text = text.replace("das Formular", "das Formulaahr")
        text = text.replace("Formulare", "Formulaahre")
        text = text.replace("Montage", "Mohntage")
        text = text.replace("Wohnort", "Wohn-Ort")
        text = text.replace("Wohnorte", "Wohn-Orte")
        tmp = gTTS(text=text, lang="de", slow=True)
        tmp = gTTS(text=text, lang="de", slow=False)
        tmp.save(sound_fn)
    else:
        print("Exiting.")
        exit()

    # a = "<br>".join(a)
    a = ac + "<br>" + a[1]
    assert "*" not in a

    if img:
        i = '<img src="' + img + '">'
    else:
        i = ""
    tuples.append((q, i, a, "[sound:" + sound_fn + "]"))


model = genanki.Model(
    randint_model,
    "Simple Model",
    fields=[
        {
            "name": "Question"
        },
        {
            "name": "Image"
        },
        {
            "name": "Answer"
        },
        {
            "name": "Sound"
        },
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}<br><br>{{Image}}",
            # 'qfmt': '{{Question}}<br>',
            "afmt": "{{FrontSide}}<hr>{{Answer}}<br>{{Sound}}",
        },
    ],
    css=style,
)

# Generate Anki cards and add them to a deck:
name = level

deck = genanki.Deck(randint_deck, name)

for q, i, a, s in tuples:
    note = genanki.Note(model=model, fields=[q, i, a, s])
    deck.add_note(note)
# Save the deck to an Anki package (*.apkg) file:
package = genanki.Package(deck)
package.media_files = media_files
package.write_to_file("./apkg/"+name + ".apkg")

system("\\rm ./*.mp3")

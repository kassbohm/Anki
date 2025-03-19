# import anki
# import anki.collection
from anki.importing.apkg import AnkiPackageImporter

from gtts import gTTS
import genanki
import random
import csv
from string import ascii_letters
from os import system
import codecs
from googletrans import Translator

# help(anki.collection)
# exit()
# importer = AnkiPackageImporter(col=coll, file='path/to/your/deck.apkg')

translator = Translator()

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




# level = "A1"
# level = "A2"
# level = "B1"
# level = "B2"
# level = "C1"
# level = "C2"

# Netzwerk_neu:
# A1.1:
old = False
blooket = True

# Ready:

level = "A1.1_Dr.Kai_Substantive_01"  # Netzwerk 01
level = "A1.1_Dr.Kai_Substantive_02_A"  # Netzwerk 02
level = "A1.1_Dr.Kai_Substantive_02_B"  # Netzwerk 02
level = "A1.1_Dr.Kai_Verben_01"
# level = "A1.1_Dr.Kai_Verben_unregelmäßig"



# level = "A1.1_Kai_01"
# level = "A1.1_Kai_02"
# level = "A1.1_Netzwerk_neu_01"
# level = "A1.1_Netzwerk_neu_Unr._Verben_Präsens"
# level = "A1.1_Netzwerk_neu_Uhrzeiten"

# A1.2:
# level = "Netzwerk_neu_A1_07"
# level = "Netzwerk_neu_A1_08"
# level = "Netzwerk_neu_A1_09"
# level = "Netzwerk_neu_A1.2_Test"
#

if blooket:
    blooket_file = level + "_Blooket" + ".csv"

randint_deck = random.randint(1000000, 999999999999)
randint_model = random.randint(100000, 99999999999)

with open(level + ".txt") as f:
    lines = [x.rstrip() for x in f]

tuples = []
media_files = []

system("trash-put ./*.csv")
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

    if "(" in word:
        word = word.replace("(", "")
        word = word.replace(")", "")
        word_color = "#ff9600"
    else:
        # word_color = "DodgerBlue"
        word_color = "#50fa7b" # green


    if old:
        q = '<a style="color:DodgerBlue"; href="https://www.dwds.de/wb/'
    else:
        q = '<a style="color:' + word_color + '"; href="https://www.verbformen.com/?w='

    if "/" not in word:
        q += word
        q += '";><u>'
        q += word
        q += "</u>"
    else:
        word = word.split("/")
        q += word[1]
        q += '";><u>'
        q += word[0]
        q += "</u>"
    q += "</a>"

    # print(q)

    a = line[1]
    a = a.split(", =")

    tmp = a[1].split("**")
    if len(tmp[2]) != 0:
        # br = True
        br = False
    else:
        br = False

    # a[1] = a[1].strip()
    a[1] = a[1].replace("** ", "**", 1)
    # a[1] = a[1].replace("**", '<font style="color: #0090ff;">', 1)
    a[1] = a[1].replace("**", '<font style="color: #f1fa8c;">', 1)
    a[1] = a[1].replace("**", "</font> ", 1)


    # green = "#50fa7b"
    # pink = "#ff79c6"
    # purple = "#bd93f9"
    # yellow = "#f1fa8c"

    ac = a.copy()[0]
    ac = ac.replace(
        " **",
        ' <font style="color: #50fa7b;">', 
    )
    ac = ac.replace(
        "**",
        "</font>",
    )
    ac = ac.replace(
        " (",
        ' <font style="color: #f1fa8c;">',
    )
    ac = ac.replace(
        ")",
        "</font>",
    )
    ac = ac.replace(
        " [",
        ' <font style="color: #bd93f9;">',
    )
    ac = ac.replace(
        "]",
        "</font>",
    )
    ac = ac.replace(
        " {",
        '<br><font style="color: #bd93f9;">',
    )
    ac = ac.replace(
        "}",
        "</font>",
    )

    text = a[0]
    text = text.replace(
        " **",
        " ",
    )
    text = text.replace(
        "**",
        "",
    )
    text = text.replace(
        " (",
        " ",
    )
    text = text.replace(
        ")",
        "",
    )
    text = text.replace(
        " [",
        " ",
    )
    text = text.replace(
        "]",
        "",
    )
    text = text.replace(
        " {",
        " ",
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
    # print(text)
    # exit()

    # write csv for Blooket:
    if blooket:
        with open(blooket_file, mode="a") as f:
            eggs = csv.writer(f,
                              delimiter=",",
                              quotechar='"',
                              quoting=csv.QUOTE_MINIMAL)
            if level == "A1.1_Dr.Kai_Substantive_01":
                tmp = text.split(" ")
                question = tmp[0] + " " + tmp[1]
            else:
                question = word
            print(question)

            # if level == "A1.1_Dr.Kai_Substantive_01" or level == "A1.1_Dr.Kai_Verben_01" or level == "A1.1_Dr.Kai_Verben_unregelmäßig"  :
            if level == "A1.1_Dr.Kai_Substantive_02_A" or level == "A1.1_Dr.Kai_Substantive_02_B" or level == "A1.1_Dr.Kai_Substantive_01" or level == "A1.1_Dr.Kai_Verben_01":
                tmp = text.split(" ")
                tmp = tmp[:5]
                tmp = " ".join(tmp)
                tmp = tmp.strip()
                # print(tmp)
                # exit()
                 # tmp = tmp.split("-")
                correct = tmp
                # print(correct)
                # exit()
                # corrects = [tmp[0].strip(), tmp[1].strip()]
                # correct = random.choice(corrects)
            else:
                correct = text
            # print("Correct:")
            # print(correct)

            indices = []
            for n, i in enumerate(correct):
                if i != " ":
                    if i != "-":
                        indices.append(n)

            X = []
            for i in range(8):  # make more than needed.
                sam = random.sample(indices, 1)
                # print(sam)
                letts = iter(random.sample(ascii_letters, 1))
                lst = list(correct)
                for ind in sam:
                    lst[ind] = next(letts).lower()
                tmp = "".join(lst)
                if tmp == question or tmp == correct:
                    continue
                X.append(tmp)
                Y = set(X)
                Y = list(Y)
                if len(Y)==3:
                    break
            row = [line_no, question, correct, Y[0], Y[1], Y[2], 10, "1"]
            eggs.writerow(row)

    sound_fn = text + ".mp3"
    sound_fn = sound_fn.strip()
    media_files.append(sound_fn)

    if img:
        image_fn = "Img/Uhr/" + img
        media_files.append(image_fn)
    else:
        pass
        # media_files.append(None)
    # Improve sounds:
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

    tmp.save(sound_fn)

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
    # print(q)
    # print(i)
    # print(a)
    # print(s)
    # print("\n")

    note = genanki.Note(model=model, fields=[q, i, a, s])
    deck.add_note(note)
# Save the deck to an Anki package (*.apkg) file:
package = genanki.Package(deck)
package.media_files = media_files
package.write_to_file(name + ".apkg")

system("trash-put ./*.mp3")

# print(line_no)
# if blooket:
#     with open(blooket_file, mode="a") as f:
#         eggs = csv.writer(
#             f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
#         )
#         for i in range(100-line_no):
#             row = [line_no+i+1, "" , "", "", "", "", "", ""]
#             eggs.writerow(row)

from gtts import gTTS
import genanki
import random
import csv
from string import ascii_letters
from os import system

from googletrans import Translator
translator = Translator()

# tmp = translator.translate('mit etwas beginnen', dest='en')
# print(tmp.text)

style = """
.card {
  font-size: 19px;
  text-align: center;
  color: #404040;
  background-color: white;
  b, strong {
  color: red;
  };
}
.replay-button svg path {
stroke: white;
fill: #404040;
}
"""

# level = "A1"
# level = "A2"
# level = "B1"
# level = "B2"
# level = "C1"
# level = "C2"


# Netzwerk_neu:
# A1.1:
# Ready:
# level = "A1.1_Netzwerk_neu_Unr._Verben_Präsens"
# level = "A1_Netzwerk_neu_01"
level = "A1.1_Netzwerk_neu_Uhrzeiten"
# level = "A1.1_01"
# level = "A1.1_02"
# Work in Progress:


# A1.2:
# level = "Netzwerk_neu_A1_07"
# level = "Netzwerk_neu_A1_08"
# level = "Netzwerk_neu_A1_09"
# level = "Netzwerk_neu_A1.2_Test"
#
# DeutschFuchs-Vokabular:


if level == "A1":
  random.seed(1)
elif level == "A2":
  random.seed(2)
elif level == "B1":
  random.seed(3)
elif level == "B2":
  random.seed(4)
elif level == "C1":
  random.seed(5)
elif level == "C2":
  random.seed(6)
elif level == "Netzwerk_neu_A1_07":
  random.seed(100)
elif level == "Netzwerk_neu_A1_08":
  random.seed(100)
elif level == "Netzwerk_neu_A1.2_Test": 
  random.seed(20)
elif level == "A1.1_01":
  random.seed(7)
elif level == "A1.1_02":
  random.seed(8)
elif level == "Netzwerk_neu_A1_01":
  random.seed(9)
elif level == "A1.1_Netzwerk_neu_Unr._Verben_Präsens":
  random.seed(10)
elif level == "A1.1_Netzwerk_neu_Uhrzeiten":
  random.seed(11)

randint_deck = random.randint(10000, 99990)
randint_model = random.randint(1000, 9999)
# print(randint_deck)
# print(randint_model)

with open(level + ".txt") as f:
  lines = [x.rstrip() for x in f]

tuples = []
media_files =  []

system("trash-put ./*.csv") 
system("cp ./intro.txt ./eggs.csv") 
# system("trash-put ./*.apkg") 

line_no = 0

for line in lines:

  line_no += 1

  if line[0]=="#":
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

  q = "<a style=\"color:DodgerBlue\"; href=\"https://www.dwds.de/wb/"

  if "/" not in word:
    q += word
    q += "\";><u>"
    q += word
    q += "</u>"
  else:
    word = word.split("/")
    q += word[1]
    q += "\";><u>"
    q += word[0]
    q += "</u>"
  q += "</a>"

  # print(q)

  a = line[1]
  a = a.split(", =")
 
  a[1] = a[1].replace("**","<font style=\"color: #0090ff;\">",1)
  a[1] = a[1].replace("**","</font>",1)


  ac = a.copy()[0]
  ac = ac.replace(" **"," <font style=\"color: #0090ff;\">", )
  ac = ac.replace("**","</font>", )
  ac = ac.replace(" ("," <font style=\"color: #0cc93f;\">", )
  ac = ac.replace(")","</font>", )
  ac = ac.replace(" ["," <font style=\"color: #ff9600;\">", )
  ac = ac.replace("]","</font>", )
  ac = ac.replace(" {"," <font style=\"color: #e500fa;\">", )
  ac = ac.replace("}","</font>", )



  text = a[0]
  text = text.replace(" **"," ", )
  text = text.replace("**","", )
  text = text.replace(" ("," ", )
  text = text.replace(")","", )
  text = text.replace(" ["," ", )
  text = text.replace("]","", )
  text = text.replace(" {"," ", )
  text = text.replace("}","", )
  # acopy
  # acopy[1] = acopy[1].replace("**g**","<i style=\"color:Green;\">",1)
  # acopy[1] = acopy[1].replace("**g**","</i>",1)

  # a[0] = a[0].replace("**g**","<font style=\"color:Green;\">",1)
  # a[0] = a[0].replace("**g**","</font>",1)

  # a[0] = a[0][1:-1]
  # a[2] = a[2].replace("/", " oder ")
  
  # tts:
  print(line_no)
  print(text)

  # # write csv for Blooket:
  # with open('eggs.csv', mode='a') as efile:
  #   eggs = csv.writer(efile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  #   correct = " - ".join(a)
  #   print(correct)

  #   indices = []
  #   for n, i in enumerate(correct):
  #     if i != " ":
  #       if i!= "-":
  #         indices.append(n)

  #   sam = random.sample(indices, 3)
  #   print(sam)

  #   letts =  iter(random.sample(ascii_letters, 3))
  #   lst = list(correct)
  #   for ind in sam:
  #     lst[ind] = next(letts)

  #   print("".join(lst))

  #   row = [line_no, correct , "falsch", "auch falsch"]
  #   eggs.writerow(row)

  sound_fn = text+".mp3"
  media_files.append(sound_fn) 

  if img:
    image_fn = "Img/Uhr/"+img
    media_files.append(image_fn) 
  else:
    pass
    # media_files.append(None)
  # Improve sounds:
  text = text.replace(", log,", ", lohk,")
  text = text.replace(", grub,", ", gruhb,")
  text = text.replace(", stach,", ", staach,")
  text = text.replace(", sog,", ", sook,")

  tmp = gTTS(text=text, lang='de', slow=True)
  tmp.save(sound_fn)
  
  # a = "<br>".join(a)
  a = ac+"<br>"+a[1]
  assert "*" not in a


  if img:
    i = "<img src=\"" + img + "\">"
  else:
    i = ""
  tuples.append((q, i, a, "[sound:"+sound_fn+"]"))

model = genanki.Model(
  randint_model,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Image'},
    {'name': 'Answer'},
    {'name': 'Sound'},
    
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}<br><br>{{Image}}',
      'afmt': '{{FrontSide}}<hr>{{Answer}}<br>{{Sound}}',
    },
  ],
  css = style
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
package.write_to_file(name + ".apkg")

system("trash-put ./*.mp3") 
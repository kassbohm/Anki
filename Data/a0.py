from gtts import gTTS
import genanki
import random
import csv
from string import ascii_letters

from os import system


style = """
.card {
  font-size: 19px;
  text-align: center;
  color: #404040;
  background-color: white;
}
.replay-button svg path {
stroke: white;
fill: #404040;
}
"""


level = "A1"
# level = "A2"
# level = "B1"
# level = "B2"
# level = "C1"
# level = "C2"
# level = "test"

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
elif level == "test":
  random.seed(100)



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

line_no = 0
for line in lines:

  line_no += 1

  line = line.split(maxsplit=1)
  
  word = line[0]

  extra = ""
  if word[0]=="¹":
    extra = "#1"
  elif word[0]=="²":
    extra = "#2"

  q = "<a href=https://www.dwds.de/wb/"
  if extra == "":
    q += word
  else:
    q += word[1:]
  q += extra
  q += ">"
  q += word
  q += "</a>"

  a = line[1]
  a = a.split(",")


  a[0] = a[0][1:-1]
  


  a[2] = a[2].replace("/", " oder ")

  if level == "A1":
    a = [a[0], a[2]]

  # tts:
  text = ", ".join(a)

  print(line_no)
  print(a)

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

  # Improve sounds:
  text = text.replace(", log,", ", lohk,")
  text = text.replace(", grub,", ", gruhb,")
  text = text.replace(", stach,", ", staach,")
  text = text.replace(", sog,", ", sook,")

  tmp = gTTS(text=text, lang='de', slow=True)
  tmp.save(sound_fn)
  
  a = "<br>".join(a)
  assert "*" not in a

  tuples.append((q, a, "[sound:"+sound_fn+"]"))

model = genanki.Model(
  randint_model,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'Sound'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr>{{Answer}}<br>{{Sound}}',
    },
  ],
  css = style
   )

# Generate Anki cards and add them to a deck:
name = level + "_Starke_Verben"

deck = genanki.Deck(randint_deck, name)

for q, a, s in tuples:
    note = genanki.Note(model=model, fields=[q, a, s])
    deck.add_note(note)

# Save the deck to an Anki package (*.apkg) file:
package = genanki.Package(deck)
package.media_files = media_files
package.write_to_file(name + ".apkg")

system("trash-put ./*.mp3") 

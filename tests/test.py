from nltk.corpus import wordnet as wn
import string
import numpy
import matplotlib.pyplot as plt

### Synonym checker using nltk package
# def check_synonym(word, sent):
#     word_synonyms = []
#     for synset in wn.synsets(word):
#         for lemma in synset.lemma_names():
#             if lemma in sent and lemma != word:
#                 word_synonyms.append(lemma)
#     return word_synonyms

# sent = input("what do you want to say")
# said = sent.split(" ")
# word_synonyms = check_synonym(word, sent)

goodDays = 0
badDays = 0
neutralDays = 0

goodWords = 0
badWords = 0
neutralWords = 0

# extract info from keywords.txt
# make and fill dictionary
kfile = open("keywords.txt", "r", encoding="utf‐8")
dictk = {}
words = kfile.readlines()
for i in range(len(words)):
    line = words[i]
    # print(line)
    line = line.split(",")
    keyword = line[0]
    sentimentvalue = int(line[1])
    dictk [keyword] = sentimentvalue
num = 0

### REMOVE commented line for demo static string
phrase = input("what do you want to say?")
#phrase = "I’m afraid to work, but I’m also afraid to refuse unsafe work. I want to help, but I don’t want to get sick or die either. If all the health professionals get sick, who will care for the patients?"

line = phrase.split(" ")

# Calculate happiness score
happinessScore = 0
score = 0
noofkeywords = 0
for i in range(len(line)):
    line[i] = line[i].lower()
    if line[i] in dictk:
        score += dictk[line[i]]
        noofkeywords += 1
        word = dictk[line[i]]
        if word > 6:
            goodWords += 1
        elif happinessScore < 4:
            badWords += 1
        else:
            neutralWords += 1
            

if noofkeywords > 0 and score > 0:
    happinessScore = score/noofkeywords
# print(dictk)
print(happinessScore)
# print(score)

if happinessScore > 6:
    print("today was a good day :)")
    goodDays+=1
elif happinessScore < 4:
    print("today was a bad day :(")
    badDays+=1
else:
    print("today was ok :| ")
    neutralDays+=1

print("num good words:", goodWords)
print("num bad words:", badWords)
print("num neutral words:", neutralWords)

labels = 'Good', 'Bad', 'Neutral'
sizes = [goodWords, badWords, neutralWords]
explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.show()

# print ("WORD:", word)
# print ("SENTENCE:", sent)
# print ("SYNONYMS FOR '" + word.upper() + "' FOUND IN THE SENTENCE: " + ", ".join(word_synonyms))
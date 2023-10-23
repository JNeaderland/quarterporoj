#Author: Jacob Neaderland

#Verbs
#Setting the number of words needed
minrangev = int(2)
#Asking for the words
verb = input("What are your 2 verbs? ")
#Splitting the long string into each word
verbs = verb.split()
#Loop to make sure the right number of words were given
while len(verbs) < minrangev:
    verb = input("What are your 2 verbs? ")
    verbs = verb.split()
    print (verbs)
#Setting maxing the string at the number of words needed
verbf = verbs[0:2]

#Past tense verb
minrangepv = int(1)
verbp = input("What is your past tense verb? ")
verbps = verbp.split()
while len(verbps) < minrangepv:
    verbp = input("What is your past tense verb? ")
    verbps = verbp.split()
    print (verbps)
verbpf = verbps[0:1]

#Verbs ending in ing
minrangeving = int(5)
verbing = input("What are your 5 verbs ending in ing? ")
verbings = verbing.split()
while len(verbings) < minrangeving:
    verbing = input("What are your 5 verbs ending in ing? ")
    verbings = verbing.split()
    print (verbings)
verbingf = verbings[0:5]

#Singular nouns
minrangesn = int(12)
snoun = input("What are your 12 nouns? ")
snouns = snoun.split()
while len(snouns) < minrangesn:
    snoun = input("What are your 12 nouns? ")
    snouns = snoun.split()
    print (snouns)
snounf = snouns[0:13]

#plural nouns
minrangepn = int(1)
pnoun = input("What is your plural noun? ")
pnouns = pnoun.split()
while len(pnouns) < minrangepn:
    pnoun = input("What is your plural noun? ")
    pnouns = pnoun.split()
    print (pnouns)
pnounf = pnouns[0:1]

#Adjectives
minrangea = int(20)
adj = input("What are your 20 adjectives? ")
adjs = adj.split()
while len(adjs) < minrangea:
    adj = input("What are your 20 adjectives? ")
    adjs = adj.split()
    print (adjs)
adjf = adjs[0:20]

#Names
minrangena = int(2)
name = input("What are your 2 names? ")
names = name.split()
while len(names) < minrangena:
    name = input("What are your 2 names? ")
    names = name.split()
    print (names)
namesf = names[0:2]

#I did not write this story, ChatGPT did
#Breaking the storie down into their sentences
sentence0 = "Once upon a time in a " + adjf[0] + "faraway land, there lived a group of " + snounf[0] + "Jesuits who were known for their " + adjf[1] + "intelligence and " + adjf[2] + "dedication."
sentence1 = "They were " + verbingf[0] + "tirelessly to spread the message of " + snounf[1] + "knowledge and " + snounf[2] + "enlightenment. "
sentence2 = "One day, a " + adjf[3] + "and " + adjf[4] + "young Jesuit named " + namesf[0] + "set out on a(n) " + adjf[5] + "mission. "
#Combining sentences into paragraphs
paragraph0 = sentence0 + sentence1 + sentence2

sentence3 = "He was tasked with " + verbingf[1] + "to a remote " + snounf[3] + "island, known as " + namesf[1] + ", to establish a " + adjf[6] + "mission there. "
paragraph1 = sentence3

sentence4 = "As he embarked on his journey, he faced many " + adjf[7] + "challenges, from treacherous " + pnounf[0] + "to " + adjf[8] + "storms at sea."
sentence5 = "But his unwavering " + snounf[4] + "faith and " + snounf[5] + "determination kept him going. He knew that the people on the island were in need of " + snounf[6] + "guidance and " + adjf[9] + "support. "
paragraph2 = sentence4 + sentence5

sentence6 = "Upon arriving on the island, " + namesf[0] + "was greeted by " + adjf[10] + "villagers who were curious about the " + snounf[7] + "teachings he had to offer."
sentence7 = "He began " + verbingf[2] + "with the locals, sharing stories and" + verbingf[3] + "about the wonders of the" + snounf[8] + "universe."\
paragraph3 = sentence6 +sentence7

sentence8 = "The Jesuits worked together with the islanders to build a " + adjf[11] + "chapel where they could " + verbf[0] + "pray and " + verbf[1] + "meditate." 
sentence9 = "They also set up a " + adjf[12] + "school where the children could receive a " + adjf[13] + "education. "
paragraph4 = sentence8 + sentence9

sentence10 = "Over time, the island transformed into a place of " + adjf[14] + "harmony and " + snounf[9] + "unity." 
sentence11 = "The Jesuits had successfully " + verbpf[0] + "the people with their " + adjf[15] + "wisdom, and the islanders had embraced their " + snounf[10] + "teachings. "
paragraph5 = sentence10 + sentence11

sentence12 = namesf[0] + "returned to his homeland, knowing that he had made a " + adjf[16] + "difference in the lives of the islanders." 
sentence13 = "The Jesuits continued their " + adjf[17] + "mission, spreading " + snounf[11] + "enlightenment wherever they went. "
paragraph6 = sentence12 + sentence13

sentence14 = "And so, the story of the Jesuits and their " + adjf[18] + "adventures continued, as they dedicated themselves to " + verbingf[4] + "the world with their " + adjf[19] + "knowledge and " + snounf[12] + "faith."
paragraph7 = sentence14

story = paragraph0 + "\n" + paragraph1 + "\n" + paragraph2 + "\n" + paragraph3 + "\n" + paragraph4 + "\n" + paragraph5 + "\n" + paragraph6 +  "\n" + paragraph7
print (story)

#Author: Jacob Neaderland
  
#Asking the user for words and making sure that the number they give is the amount needed

#Verbs
minrangev = int(2)
verb = input("What are your 2 verbs? ")
verbs = verb.split()
#Loop to make sure the right number of words were given
while len(verbs) < minrangev:
    verb = input("What are your 2 verbs? ")
    verbs = verb.split()
    print (verbs)
verbf = verbs[0:2]

#Past tense verb
minrangepv = int(1)
verbp = input("What is your past tense verb? ")
verbps = verbp.split()
#Loop to make sure the right number of words were given
while len(verbps) < minrangepv:
    verbp = input("What is your past tense verb? ")
    verbps = verbp.split()
    print (verbps)
verbpf = verbps[0:1]

#Verbs ending in ing
minrangeving = int(5)
verbing = input("What are your 5 verbs ending in ing? ")
verbings = verbing.split()
#Loop to make sure the right number of words were given
while len(verbings) < minrangeving:
    verbing = input("What are your 5 verbs ending in ing? ")
    verbings = verbing.split()
    print (verbings)
verbingf = verbings[0:5]

#Singular nouns
minrangesn = int(12)
snoun = input("What are your 12 nouns? ")
snouns = snoun.split()
#Loop to make sure the right number of words were given
while len(snouns) < minrangesn:
    snoun = input("What are your 12 nouns? ")
    snouns = snoun.split()
    print (snouns)
snounf = snouns[0:13]

#plural nouns
minrangepn = int(1)
pnoun = input("What is your plural nouns? ")
pnouns = snoun.split()
#Loop to make sure the right number of words were given
while len(pnouns) < minrangesn:
    pnoun = input("What is your plural nouns? ")
    pnouns = pnoun.split()
pnounf = pnouns[0:1]

#Adjectives
minrangea = int(20)
adj = input("What are your 20 adjectives? ")
adjs = adj.split()
#Loop to make sure the right number of words were given
while len(adjs) < minrangesn:
    adj = input("What are your 20 adjectives? ")
    adjs = adj.split()
adjf = adjs[0:20]

#Names
minrangena = int(2)
name = input("What are your 2 names? ")
names = name.split()
#Loop to make sure the right number of words were given
while len(names) < minrangena:
    name = input("What are your 2 names? ")
    names = name.split()
namesf = names[0:2]

#I did not write this story, ChatGPT did

story1 = "Once upon a time in a " + adjf[0] + "faraway land, there lived a group of " + snounf[0] + "Jesuits who were known for their " + adjf[1] + "intelligence and " + adjf[2] + "dedication. They were " + verbingf[0] + "tirelessly to spread the message of " + snounf[1] + "knowledge and " + snounf[2] + "enlightenment. "
story2 = "One day, a " + adjf[3] + "and " + adjf[4] + "young Jesuit named " + namesf[0] + "set out on a(n) " + adjf[5] + "mission. He was tasked with " + verbingf[1] + "to a remote " + snounf[3] + "island, known as " + namesf[1] + ", to establish a " + adjf[6] + "mission there. "
story3 = "As he embarked on his journey, he faced many " + adjf[7] + "challenges, from treacherous " + pnounf[0] + "to " + adjf[8] + "storms at sea. But his unwavering " + snounf[4] + "faith and " + snounf[5] + "determination kept him going. He knew that the people on the island were in need of " + snounf[6] + "guidance and " + adjf[9] + "support. "
story4 = "Upon arriving on the island, " + namesf[0] + "was greeted by " + adjf[10] + "villagers who were curious about the " + snounf[7] + "teachings he had to offer. He began " + verbingf[2] + "with the locals, sharing stories and" + verbingf[3] + "about the wonders of the" + snounf[8] + "universe."
story5 = "The Jesuits worked together with the islanders to build a " + adjf[11] + "chapel where they could " + verbf[0] + "pray and " + verbf[1] + "meditate. They also set up a " + adjf[12] + "school where the children could receive a " + adjf[13] + "education. "
story6 = "Over time, the island transformed into a place of " + adjf[14] + "harmony and " + snounf[9] + "unity. The Jesuits had successfully " + verbpf[0] + "the people with their " + adjf[15] + "wisdom, and the islanders had embraced their " + snounf[10] + "teachings. "
story7 = namesf[0] + "returned to his homeland, knowing that he had made a " + adjf[16] + "difference in the lives of the islanders. The Jesuits continued their " + adjf[17] + "mission, spreading " + snounf[11] + "enlightenment wherever they went. "
story8 = "And so, the story of the Jesuits and their " + adjf[18] + "adventures continued, as they dedicated themselves to " + verbingf[4] + "the world with their " + adjf[19] + "knowledge and " + snounf[12] + "faith."
print(story1 + story2 + story3 + story4 + story5 + story6 + story7 + story8)

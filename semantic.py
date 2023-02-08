import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Model finds higher similarity between the two animals than the fruit and animals

# My example
word1 = nlp("Australia")
word2 = nlp("New Zealand")
word3 = nlp("Sydney")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# Finds higher similarity between the 2 countries (1 & 2) and the two that relate to same country (1&3)

tokens = nlp('cat apple monkey banana potato chips')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# the 'md' module seems to be a more powerful model than 'sm'
# the similarity correlations are stronger from abstract content
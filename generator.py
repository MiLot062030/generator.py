
import random

def getWords(filename):
    with open(filename, 'r') as file:
        return tuple(word.strip() for word in file.readlines())

def sentenceGenerator(nouns, verbs, articles, prepositions):
    noun1 = random.choice(nouns)
    verb = random.choice(verbs)
    article1 = random.choice(articles)
    preposition = random.choice(prepositions)
    noun2 = random.choice(nouns)
    return f"{article1.capitalize()} {noun1} {verb} {preposition} {article1} {noun2}."

def main():
    nouns = getWords('nouns.txt')
    verbs = getWords('verbs.txt')
    articles = getWords('articles.txt')
    prepositions = getWords('prepositions.txt')

    num_sentences = int(input(" Enter the number of sentence. "))
    for _ in range(num_sentences):
        print(sentenceGenerator(nouns, verbs, articles, prepositions))

if __name__ == "__main__":
    main()
# imports
from numpy import true_divide
import spacy
from jisho_api import sentence as s
import os
import re

def get_known_words():
    # read known words from "known" directory next to the script

    result = set()
    for filename in os.listdir("./known"):
        with open(os.path.join("./known/", filename), 'r') as f: # open in readonly mode
            
            for line in f:
                split_line = line.split("\t")
                result.add(split_line[0])

    return result
            

def get_sentences_for_word(target_word:str):
    # get sentences from jishos with the word

    sentences_found = []

    # get sentences with that word from api
    # following function returns a list
    jisho_results = s.Sentence.request(target_word).data

    for sentence_found in jisho_results:
        japanese_sentence = sentence_found.japanese
        # remove furigana
        # jisho includes furigana in () and []
        # example sentence: 今日(きょう)は行(い)かない。
        japanese_sentence = re.sub("[\(\[].*?[\)\]]", "", japanese_sentence)

        sentences_found.append(japanese_sentence)

    return sentences_found

def split_sentence_to_words(nlp:spacy.language, sentence:str):
    # split a sentence to its words (nouns, adjectives, adverbs, adjectives)

    result = []
    doc = nlp(sentence)

    include_types = ["NOUN", "VERB", "ADJ", "ADV", "PRON"]

    for token in doc:
        if token.pos_ in include_types:
            result.append(token.lemma_)

    return result

def find_i_plus_one(nlp:spacy.language, sentences:list, known_words:list):
    # finds i+1 sentences
    # i+1 sentences are defined according to https://en.wikipedia.org/wiki/Input_hypothesis#Input_hypothesis


    # populate and return a list of i+1 sentences:
    # 1. Go through sentences, filter them according to known_words list and count unknown words.
    # 2. If amount of unknown words equal to 1, add that sentence to the list.
    result = []
    
    for sentence in sentences:
        unknown_word_count = 0
        
        words = split_sentence_to_words(nlp, sentence)
        for word in words:
            if not word in known_words:
                unknown_word_count += 1
            
        if unknown_word_count == 1:
            stripped_sentence = sentence.replace(" ", "")
            result.append(stripped_sentence)
                
    return result

if __name__=="__main__":

    #word_to_test = "姿"
    word_to_test = input("Please enter a word: ")

    # load nlp model
    nlp = spacy.load("ja_ginza")

    # get a list of sentences and a list of known words
    sentences = get_sentences_for_word(word_to_test)
    known_words = get_known_words()

    # find i+1s
    i_plus_one_sentences = find_i_plus_one(nlp, sentences, known_words)

    # save result
    with open("result.txt", "w") as f:
        f.write("Target:\t"+word_to_test+"\n")
        print("Target:\t"+word_to_test)
        for sentence in i_plus_one_sentences:
            f.write(sentence + "\n")
            print(sentence)
    
    
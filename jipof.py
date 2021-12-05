# imports
from numpy import true_divide
import spacy
import json
import urllib.request
from werkzeug.urls import url_fix
import os

def get_known_words():
    result = set()
    for filename in os.listdir("./known"):
        with open(os.path.join("./known/", filename), 'r') as f: # open in readonly mode
            
            for line in f:
                split_line = line.split("\t")
                result.add(split_line[0])

    return result
            

def get_sentences_for_word(target_word:str):

    sentences_found = []

    # https://tatoeba.org/en/sentences/search?from=jpn&query=%3D明日&to=eng
    target_word = "https://tatoeba.org/en/api_v0/search?from=jpn&query=" + target_word + "&sort=random"

    search_url = url_fix(target_word)

    with urllib.request.urlopen(search_url) as url:
        data = json.load(url)
        
        for sentence in data["results"]:
            sentences_found.append(sentence["text"])

    return sentences_found

def does_have_tag(tag:str, tags:str):
    # check if tags of a word is included in tag

    temp = " ".join(tags.split("-"))

    result = (" " + tag + " ") in (" " + temp + " ")
    return result

def split_sentence_to_words(nlp:spacy.language, sentence:str):
    # split a sentence to its words

    result = []
    doc = nlp(sentence)

    for token in doc:
        if does_have_tag("動詞", token.tag_) or does_have_tag("名詞", token.tag_):
            #print(f"{token.text}\t{token.lemma_}\t{token.tag_}")
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

    # load nlp model
    nlp = spacy.load("ja_ginza")

    # get a list of sentences and a list of known words
    sentences = get_sentences_for_word("暇")
    known_words = get_known_words()

    # find i+1s
    i_plus_one_sentences = find_i_plus_one(nlp, sentences, known_words)

    # save result
    with open("result.txt", "w") as f:
        for sentence in i_plus_one_sentences:
            #f.write(sentence + "\n")
            print(sentence)
    
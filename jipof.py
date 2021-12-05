# imports
import spacy

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
            print(f"{token.text}\t{token.lemma_}\t{token.tag_}")
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
            if not (word in known_words):
                unknown_word_count += 1
            
        if unknown_word_count == 1:
            stripped_sentence = sentence.replace(" ", "")
            result.append(stripped_sentence)
                
    return result

if __name__=="__main__":

    # load nlp model
    nlp = spacy.load("ja_ginza")

    # get a list of sentences and a list of known words
    # list of known words are placeholders
    sentences = ["明日は学校に行く。", "昨日は学校に行った。", "今日は木曜日だから学校に行く。", "座るために椅子を買いました。"]
    known_words = set(["行く", "学校", "座る", "買う", "ため"])

    # find i+1s
    i_plus_one_sentences = find_i_plus_one(nlp, sentences, known_words)

    # save result
    with open("result.txt", "w") as f:
        for sentence in i_plus_one_sentences:
            f.write(sentence + "\n")
    
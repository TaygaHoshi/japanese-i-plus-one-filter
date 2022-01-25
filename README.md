# Japanese i+1 Filter
Finds i+1 sentences from Jisho.org, all of which include a word. The term "i+1" is described as explained [in this wikipedia article](https://en.wikipedia.org/wiki/Input_hypothesis#Input_hypothesis).

# How does it work?
1. Get a word from user
2. Search sentences for that word in [Jisho.org](https://jisho.org)
3. Divide sentences to words using ja_ginza and take important words (nouns, adjectives, verbs and so on)
4. Compare words of each sentence to words in known words set
5. Count unknown words found in step 4
6. If there are exactly 1 unknown word in a sentence, add it to results list
7. Show result(s)

# Requirements
## General Requirements
* Made using Python 3.10.0
* Access to Jisho.org

## External Libraries
* [ja_ginza](https://github.com/megagonlabs/ginza) and its dependencies
* [jisho-api](https://pypi.org/project/jisho-api/#description)

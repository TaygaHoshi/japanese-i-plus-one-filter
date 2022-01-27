# Japanese i+1 Filter
Finds i+1 sentences from Jisho.org, all of which include a word. The term "i+1" is described as explained [in this wikipedia article](https://en.wikipedia.org/wiki/Input_hypothesis#Input_hypothesis).

# How does it work?
1. User creates "words.txt" next to the .py file.
2. User adds words to "words.txt", one word per line.
3. Load "words.txt".
4. Search sentences for each word in [Jisho.org](https://jisho.org)
5. Divide sentences to words using ja_ginza and take important words (nouns, adjectives, verbs and so on).
6. Compare words of each sentence to words in known words set.
7. Count unknown words found in step 4.
8. If there are exactly 1 unknown word in a sentence, it's an i+1 sentence.
9. Save results in "results.txt".

# Requirements
## General Requirements
* Made using Python 3.10.0
* Access to Jisho.org

## External Libraries
* [ja_ginza](https://github.com/megagonlabs/ginza) and its dependencies
* [jisho-api](https://pypi.org/project/jisho-api/#description)

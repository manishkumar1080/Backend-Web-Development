#This is the file where the statements are there for generating a square wordcloud from the text file using default arguments.

#This statement is used for importing the various modules from the wordcloud library

from wordcloud import WordCloud
import matplotlib.pyplot as plt


#This is the function which is used for generating wordcloud
def generate_words():

    #This statement is used for reading the whole text.
    text = open('wordcloud.txt').read()

    #This statement is used to generate a word cloud image
    wordcloud = WordCloud().generate(text)


    #This statement displays the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
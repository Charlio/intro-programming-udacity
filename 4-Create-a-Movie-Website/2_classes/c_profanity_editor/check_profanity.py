# Lesson 3.3: Use Classes
# Mini-Project: Check Profanity

# Typos can be embarassing! Imagine how you'd feel if you
# accidentally sent your boss an email that said "I'll take
# a sh!t at it" instead of "I'll take a shot at it". Write
# a program that can detect curse words in a string of text.

# Use this space to describe your approach to the problem.
#
#
#
#

import urllib

def read_text():
    # Your code here.
    txt_path = r"C:\Users\chali\Documents\Work\Artificialintelligence\intro-programming-Udacity\4-Create-a-Movie-Website\2_classes\c_profanity_editor\movie_quotes.txt"
    quotes = open(txt_path)
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()    
    print('\n')
    check_profanity(contents_of_file)
    
def check_profanity(text):
    # Your code here.
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    print(output)
    
read_text()
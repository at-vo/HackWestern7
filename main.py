##
# Name: Abdalla Abdelhady
# Student Number: 250856115
# This module defines a functions that takes two files, one with tweets and one with keywords and sentiment values,
#and calculates an average sentiment value for each timezone in continental United States
#

#This part imports the module with the function that calculates sentiment values
import sentiment_analysis

#This part asks the user for the names of the files
tfile = input("What is the name of the file with tweets? ")
kfile = input("What is the name of the file with keywords? ")

finalvalues = sentiment_analysis.compute_tweets(tfile, kfile)

#This part outputs the results from the function in a format the user can read
print ("The (happiness_score, number_of_keyword_tweets, number_of_tweets) in the eastern, central, mountain and pacific regions respectively are as shown below:\n", finalvalues)

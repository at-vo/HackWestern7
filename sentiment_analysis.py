##
# Name: Abdalla Abdelhady
# Student Number: 250856115
# This module defines a functions that takes two files, one with tweets and one with keywords and sentiment values,
#and calculates an average sentiment value for each timezone in continental United States
#

#This part defines the name of the function
def compute_tweets(tfile, kfile):

#This part imports the string module to be used to remove punctuatuion
    import string

#This part defines all the variables, lists and dictionaries used in function
    finalvalues = []
    dictk = {}
    ekeywordtweets = 0
    etweets = 0
    esumofhappinessscore = 0
    eregionhappinessscore = 0
    ckeywordtweets = 0
    ctweets = 0
    csumofhappinessscore = 0
    cregionhappinessscore = 0
    mkeywordtweets = 0
    mtweets = 0
    msumofhappinessscore = 0
    mregionhappinessscore = 0
    pkeywordtweets = 0
    ptweets = 0
    psumofhappinessscore = 0
    pregionhappinessscore = 0
    eastern = [0,0,0]
    central = [0,0,0]
    mountain = [0,0,0]
    pacific = [0,0,0]
    p1   =  [49.189787,67.444574]
    p2   =  [24.660845,67.444574]
    p3   =  [49.189787,87.518395]
    p4   =  [24.660845,87.518395]
    p5   =  [49.189787,101.998892]
    p6   =  [24.660845,101.998892]
    p7   =  [49.189787,115.236428]
    p8   =  [24.660845,115.236428]
    p9   =  [49.189787,125.242264]
    p10  =  [24.660845,125.242264]
    region = [0,0]

#This part tries to open the files and raises and error if the files don't exist and outputs an empty set
    try:
        tfile1 = open(tfile, "r", encoding="utf‐8")
        kfile2 = open(kfile, "r", encoding="utf‐8")
    except IOError:
        return finalvalues

#This part reads the keywords file and makes a dictionary out of the data in it
    keywords = kfile2.readlines()
    for i in range(0,len(keywords)):
        line = keywords[i]
        line = line.split(",")
        keyword = line[0]
        sentimentvalue = int(line[1])
        dictk [keyword] = sentimentvalue

#This part reads the tweets file and formats the lines and words to remove punctuation and identify region of tweet
    tweet = tfile1.readlines()
    for i in range(0,len(tweet)):
        line = tweet[i]
        line = line.split(" ")
        happinessscore = 0
        score = 0
        noofkeywords = 0
        for i in range(0, len(line)):
            line[i] = line[i].strip(string.punctuation)
        region[0] = float(line[0])
        region[1] = float(line[1])

#This part identifies if there are keywords in the tweet and calculates sentimental scores
        for i in range(5, len(line)):
            line[i] = line[i].lower()
            if line[i] in dictk:
                score += dictk[line[i]]
                noofkeywords += 1

        if noofkeywords > 0 and score > 0:
            happinessscore = score/noofkeywords

#This part inputs the calculated scores into the respective regions
        if region[0] < p1[0] and region[0] > p2[0] and region[1] > p1[1] and region[1] < p3[1]:
            etweets += 1
            if happinessscore > 0:
                ekeywordtweets += 1
                esumofhappinessscore += happinessscore
                eregionhappinessscore = esumofhappinessscore/ekeywordtweets
            eastern[0] = eregionhappinessscore
            eastern[1] = ekeywordtweets
            eastern[2] = etweets
        elif region[0] < p1[0] and region[0] > p2[0] and region[1] > p3[1] and region[1] < p5[1]:
            ctweets += 1
            if happinessscore > 0:
                ckeywordtweets += 1
                csumofhappinessscore += happinessscore
                cregionhappinessscore = csumofhappinessscore/ckeywordtweets
            central[0] = cregionhappinessscore
            central[1] = ckeywordtweets
            central[2] = ctweets
        elif region[0] < p1[0] and region[0] > p2[0] and region[1] > p5[1] and region[1] < p7[1]:
            mtweets += 1
            if happinessscore > 0:
                mkeywordtweets += 1
                msumofhappinessscore += happinessscore
                mregionhappinessscore = msumofhappinessscore/mkeywordtweets
            mountain[0] = mregionhappinessscore
            mountain[1] = mkeywordtweets
            mountain[2] = mtweets
        elif region[0] < p1[0] and region[0] > p2[0] and region[1] > p7[1] and region[1] < p9[1]:
            ptweets += 1
            if happinessscore > 0:
                pkeywordtweets += 1
                psumofhappinessscore += happinessscore
                pregionhappinessscore = psumofhappinessscore/pkeywordtweets
            pacific[0] = pregionhappinessscore
            pacific[1] = pkeywordtweets
            pacific[2] = ptweets

#This part creates tuples out of the final lists formed and then adds these tuples to a final list
    eastern = tuple(eastern)
    central = tuple(central)
    mountain = tuple(mountain)
    pacific = tuple(pacific)

    finalvalues = [eastern, central, mountain, pacific]

#This part closes the two files
    tfile1.close()
    kfile2.close()

#This part returns the final list of tuples
    return finalvalues












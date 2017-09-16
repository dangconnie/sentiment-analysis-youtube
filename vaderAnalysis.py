from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



analyser = SentimentIntensityAnalyzer()
def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(snt)))
print_sentiment_scores("It's 1:33am and I don't know why I'm still up doing this analysis.")




# Some other example i found that doesn't really work. not sure what issue is...yet.
# from vaderSentiment import vaderSentiment

# sentences = [
#                 "The plot was good, but the characters are uncompelling and the dialog is not great.", 
#                 "A really bad, horrible book.",       
#                 "At least it isn't a horrible book."
#             ]
# for sentence in sentences:
#     print sentence
#     sentiment = vaderSentiment(sentence)
#     print "\n\t" + str(sentiment)






# how to best visualize this info aside from charts? word cloud?
# what libraries can i use


# http://www.nltk.org/howto/sentiment.html
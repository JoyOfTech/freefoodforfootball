# Joy's python project: what sports deals do you get?

# 1) request scores from user, tell which deals they get (you will have to do lots of deal research!)
# 2) hit api or write web scraper to get the scores on demand, tell which deals you get
# 3) put it on a server somewhere! Have it scrape and store info, and be able to generate deals on demand without more scraping
# 3a) web front-end (noninteractive)
# 3b) tweet eligible deals
# 4) interactive web front-end where someone can add their e-mail address and get customized email updates with daily deals


def add_two_numbers(x,y):
    return x+y
    
    
def count_to_n(n):
    for i in range(0,n):
        print(i)
    
    
    
def get_scores_from_user():
    #have the user enter the scores from last night using raw_input
    #store the things you care about in a dictionary
    #note: everything that comes from raw_input is a string, even if it looks like a number to you
    #you will probably have to fix that.
    return {}
    
def find_deals(scores):
    #this is where all the if statements would be to find out whether you get the deal
    #this would probably be best if scores is a dictionary with all the values you care about, like
    #{"home":17, "away":10, "played_at_home":True...} note that this is going to be the output of the method get_scores_from_user()
    return "some deals"
    
    
scores = get_scores_from_user()
find_deals(scores)
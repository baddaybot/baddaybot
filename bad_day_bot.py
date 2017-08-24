"""Bad Day Bot - Every One Deserves Some Morning Unpleasantries"""
import random
from time import sleep
import yaml
import tweepy


def load_yaml(input_file):
    """Load YAML File"""
    with open(input_file, 'r') as infile:
        data = yaml.load(infile)

    return data


def build_statement(unpleasantries):
    """Build your unpleasantries"""
    base_statement = "You're dishonest & terrible at your job"

    random_unpleasantry = random.randint(0, len(unpleasantries)-1)
    joined_statement = "{0}. {1}.".format(base_statement, unpleasantries[random_unpleasantry])

    return random_unpleasantry, joined_statement


def tweet(api, tweet_text, user):
    """Tweet These Terrible Cretins"""
    try:
        real_text = "Morning @{0},\n{1}".format(user, tweet_text)
        tweet_length = len(real_text)
        if tweet_length <= 140:
            print('\nTweeting')
            print("User: @{0}".format(user))
            print("Message: \n{0}".format(real_text))
            api.update_status(real_text)
            sleep(120)
        else:
            print('\nTweet exceeds 140 Characters - Not Tweeting')
            print("User: @{0}".format(user))
            print("Message: \n{0}".format(real_text))
    except tweepy.TweepError as error:
        print(error.reason)
        sleep(2)


def main():
    """Main Bot Program"""
    # Load Credentials for Twitter API
    credentials = load_yaml('credentials.yaml')
    auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
    auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])

    # Generate API Object
    api = tweepy.API(auth)

    # Generate list of People to Tweet
    bad_people = load_yaml('people.yaml').get('bad_people')

    # Generate list of Snarky Morning Unpleasantries
    unpleasantries = load_yaml('unpleasantries.yaml').get('unpleasantries')

    # Tell Bad People to have a bad day
    for user in bad_people:
        index, tweet_text = build_statement(unpleasantries)
        unpleasantries.pop(index)
        tweet(api, tweet_text, user)


if __name__ == '__main__':
    main()

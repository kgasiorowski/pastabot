import praw
import config


def get_pastas():

    reddit = praw.Reddit(client_id=config.reddit_id,
                         client_secret=config.reddit_secret,
                         user_agent='pastabot',
                         username=config.reddit_user,
                         password=config.reddit_pw)

    hot_subreddit = reddit.subreddit('copypasta').hot(limit=20)

    return [(post.title, post.selftext) for post in hot_subreddit if 0 < len(post.selftext) < 2000]

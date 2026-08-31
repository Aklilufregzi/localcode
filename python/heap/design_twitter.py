"""
LeetCode 355. Design Twitter (Medium)
https://leetcode.com/problems/design-twitter/

Design a simplified Twitter: postTweet(userId, tweetId), getNewsFeed(userId)
returning the 10 most recent tweet ids from the user and followees (most
recent first), follow(followerId, followeeId), unfollow(followerId, followeeId).

Run just this file:   python heap/design_twitter.py
Run its tests:        pytest heap/design_twitter.py -v
"""


class Twitter:
    def __init__(self):
        ...  # TODO: implement

    def postTweet(self, userId: int, tweetId: int) -> None:
        ...  # TODO: implement

    def getNewsFeed(self, userId: int) -> list[int]:
        ...  # TODO: implement

    def follow(self, followerId: int, followeeId: int) -> None:
        ...  # TODO: implement

    def unfollow(self, followerId: int, followeeId: int) -> None:
        ...  # TODO: implement


# ---------------------------- tests ----------------------------

def test_official_example():
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]


def test_feed_caps_at_ten_most_recent():
    twitter = Twitter()
    for tweet_id in range(1, 13):  # user 1 posts tweets 1..12
        twitter.postTweet(1, tweet_id)
    assert twitter.getNewsFeed(1) == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3]


def test_empty_feed_and_unfollow_nonfollowee():
    twitter = Twitter()
    assert twitter.getNewsFeed(1) == []
    twitter.unfollow(1, 2)  # should not crash
    twitter.postTweet(2, 7)
    assert twitter.getNewsFeed(1) == []


if __name__ == "__main__":
    # Debugging playground — set breakpoints here.
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))  # expected [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))  # expected [6, 5]
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))  # expected [5]

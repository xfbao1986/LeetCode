"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

    postTweet(userId, tweetId): Compose a new tweet.
    getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
    follow(followerId, followeeId): Follower follows a followee.
    unfollow(followerId, followeeId): Follower unfollows a followee.
    Example:

    Twitter twitter = new Twitter();

    // User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 5);

    // User 1's news feed should return a list with 1 tweet id -> [5].
    twitter.getNewsFeed(1);

    // User 1 follows user 2.
    twitter.follow(1, 2);

    // User 2 posts a new tweet (id = 6).
    twitter.postTweet(2, 6);

    // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
    // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.getNewsFeed(1);

    // User 1 unfollows user 2.
    twitter.unfollow(1, 2);

    // User 1's news feed should return a list with 1 tweet id -> [5],
    // since user 1 is no longer following user 2.
    twitter.getNewsFeed(1);
"""



from Queue import PriorityQueue as PQ
class Twitter(object):
    """
    since we don't have auto-increment id from data base,
    we need to maintain a global count (post_count) and map tweetid to postcount for ordering (id_map)
    poster_map to map tweet to its poster
    follow_map user to its follower

    to get news feed, we use a PQ, everytime:
        we put the latest tweet from each followee into PQ
        get one from the heap
        find it's poster
        and put another from the same poster onto heap and repeat until exausted or number 10 reached
    """
    def __init__(self):
        self.post_count = 2147483647 #auto dec counter so new post has smaller count (python only has min heap ... don't want to do the negation trick
        self.count_map = {}   #map tweet -> post_count
        self.owner_map = {}   #list (ordered) of tweets -> same owner
        self.poster_map = {}  #map tweet -> poster
        self.follow_map = {}  #map followee -> follower in a set (also need to add self as followee as self-posted need to be fetched for news feed)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int        :type tweetId: int        :rtype: void
        """
        self.count_map[tweetId] = self.post_count
        self.owner_map[userId] = self.owner_map.get(userId, []) + [tweetId]
        self.poster_map[tweetId] = userId
        if userId not in self.follow_map: self.follow_map[userId] = {userId} #make sure I can see the posts by myself
        self.post_count -= 1 #finally increment global count


    def getNewsFeed(self, userId, n = 10):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int        :rtype: List[int]
        """
        if userId not in self.follow_map: return [] #no follower
        ans = []
        pq = PQ() #for quick sorting of tweets
        idx_map = {k: len(self.owner_map.get(k,[]))-1 for k in self.follow_map[userId]} #to track the last tweet retrieved from each followee

        #prime the PQ with the latest feed from each followee
        for f in self.follow_map[userId]:
            if idx_map[f] < 0: continue #this guy has no tweet
            one_feed = self.owner_map[f][idx_map[f]]
            one_feed_count = self.count_map[one_feed]
            pq.put((one_feed_count, one_feed,))

        while n > 0:
            if pq.empty(): break
            new_feed = pq.get()[1] #disregard [0] which has the count
            new_feed_poster = self.poster_map[new_feed]
            ans.append(new_feed)
            #find the next new feed from the same poster
            idx_map[new_feed_poster] -= 1
            if idx_map[new_feed_poster] >= 0:
                one_feed = self.owner_map[new_feed_poster][idx_map[new_feed_poster]]
                one_feed_count = self.count_map[one_feed]
                pq.put((one_feed_count, one_feed,))
            n -= 1
        return ans


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int       :type followeeId: int        :rtype: void
        """
        #currently we cannot verify if followeeId is valid or not (??? non-existing followee)
        #automaticall follow self
        self.follow_map[followerId] = self.follow_map.get(followerId, {followerId}).union({followeeId})


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int        :type followeeId: int        :rtype: void
        """
        if followerId == followeeId: return #noop not allowed to unfollow your self
        try: self.follow_map[followerId].remove(followeeId)
        except: pass

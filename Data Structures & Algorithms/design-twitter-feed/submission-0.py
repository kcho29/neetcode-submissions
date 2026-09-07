import heapq
class Twitter:

    def __init__(self):
        self.tweetDict = {} # key: userId, value: ordered list of tuples(tweetNum, tweets (oldest to recent))
        self.followDict = {} # key: userId, value: set of following userIds
        self.tweetNum = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetDict:
            self.tweetDict[userId] = []
        self.tweetDict[userId].append((self.tweetNum, tweetId)) # userId: set((tweetNum, tweetId))
        self.tweetNum -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        tweets = []

        if userId in self.tweetDict and self.tweetDict[userId]:
            tweets.append((self.tweetDict[userId][-1][0], self.tweetDict[userId][-1][1], userId, -1))
        
        if userId in self.followDict:
            for user in self.followDict[userId]:
                if user in self.tweetDict and self.tweetDict[user]:
                    tweets.append((self.tweetDict[user][-1][0], self.tweetDict[user][-1][1], user, -1))

        heapq.heapify(tweets)

        while len(out) < 10 and tweets:
            tweetNum, tweetId, user, num = heapq.heappop(tweets)
            out.append(tweetId)
            num -= 1
            if len(self.tweetDict[user]) >= abs(num):
                heapq.heappush(tweets, (self.tweetDict[user][num][0],self.tweetDict[user][num][1] , user, num))
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followDict:
            self.followDict[followerId] = set()
        self.followDict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followDict:
            self.followDict[followerId] = set()
        self.followDict[followerId].discard(followeeId)

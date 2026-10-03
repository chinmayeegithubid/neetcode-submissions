import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for user in self.following[userId] | {userId}:
            tweets = self.tweets[user]
            if tweets:
                index = len(tweets) - 1
                time, tweet_id = tweets[index]
                heap.append((-time, tweet_id, user, index))

        heapq.heapify(heap)
        result = []

        while heap and len(result) < 10:
            _, tweet_id, user, index = heapq.heappop(heap)
            result.append(tweet_id)

            if index > 0:
                time, older_id = self.tweets[user][index - 1]
                heapq.heappush(
                    heap, (-time, older_id, user, index - 1)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
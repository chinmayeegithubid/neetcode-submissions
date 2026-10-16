from collections import defaultdict
from heapq import heapify, heappop, heappush


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = {}
        self.cuisines = {}
        self.heaps = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.ratings[food] = rating
            self.cuisines[food] = cuisine
            self.heaps[cuisine].append((-rating, food))

        for heap in self.heaps.values():
            heapify(heap)

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[food] = newRating
        cuisine = self.cuisines[food]
        heappush(self.heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]

        while -heap[0][0] != self.ratings[heap[0][1]]:
            heappop(heap)

        return heap[0][1]
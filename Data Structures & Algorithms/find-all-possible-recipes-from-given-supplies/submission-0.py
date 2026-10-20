from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dependents = defaultdict(list)
        remaining = [len(items) for items in ingredients]

        for i, items in enumerate(ingredients):
            for ingredient in items:
                dependents[ingredient].append(i)

        queue = deque(supplies)
        answer = []

        while queue:
            available = queue.popleft()

            for i in dependents.get(available, ()):
                remaining[i] -= 1

                if remaining[i] == 0:
                    answer.append(recipes[i])
                    queue.append(recipes[i])

        return answer
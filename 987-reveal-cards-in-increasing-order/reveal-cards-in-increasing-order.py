class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        queue = deque(range(len(deck)))
        for c in deck:
            i = queue.popleft()
            result[i] = c

            if queue:
                queue.append(queue.popleft())
        return result
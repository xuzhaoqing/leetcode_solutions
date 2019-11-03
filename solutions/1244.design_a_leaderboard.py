import heapq
class Leaderboard:

    def __init__(self):
        self.h = []

    def addScore(self, playerId: int, score: int) -> None:
        for i in range(len(self.h)):
            if self.h[i][1] == playerId:
                score = score + self.h[i][0]
                self.h[i] = (score, playerId)
                return 
        heapq.heappush(self.h,(score,playerId))

    def top(self, K: int) -> int:
        return sum([x[0] for x in heapq.nlargest(K,self.h)])

    def reset(self, playerId: int) -> None:
        for i in range(len(self.h)):
            if self.h[i][1] == playerId:
                self.h = self.h[:i] + self.h[i+1:]
                return 
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        team = 0
        n = len(rating)
        
        for i in range(1,n):
            lles ,rles = 0,0
            lmor, rmor = 0,0
            for j in range(i):
                if rating[j] < rating[i]:
                    lles += 1
                elif rating[j] > rating[i]:
                    lmor += 1
            for k in range(i+1,n):
                if rating[k] > rating[i]:
                    rmor += 1
                elif rating[k] < rating[i]: 
                    rles += 1
            team += lles*rmor + lmor*rles
        return team


        return team
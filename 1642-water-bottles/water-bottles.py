class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        maxi = numBottles
        emp = numBottles


        while emp>= numExchange:
            maxi += emp // numExchange
            emp = emp%numExchange + emp // numExchange


        return maxi 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_set = set()
        for i in range (len(nums)):
            if i >= k+1 :  # window is formed / sliding just slide an discard old value 
              window_set.remove(nums[i-k-1]) # remove last value that window left behind after sliding  
            if nums[i] in window_set: # we have found a dup within window range 
                return True 
            window_set.add(nums[i])
        return False
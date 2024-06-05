class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peak_indices_length=[]
        for idx in range(1,len(mountain)-1):
            if mountain[idx-1] < mountain[idx] > mountain[idx+1]:
                peak_indices_length.append(idx)
        return peak_indices_length
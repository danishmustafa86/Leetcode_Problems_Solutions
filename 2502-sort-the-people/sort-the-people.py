class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        sorted_heights = [(val,idx) for idx,val in enumerate(heights)]
        sorted_heights.sort()
        sorted_heights.reverse()
        new_names = [None] * len(names)
        indices = [tup[1]   for tup in sorted_heights]
        print(indices)
        for i, val in enumerate(indices):
            new_names[i] = names[val]
        print(new_names)
        return new_names
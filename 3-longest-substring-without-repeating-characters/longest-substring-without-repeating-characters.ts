
function lengthOfLongestSubstring(s: string): number {
  // if(s.length < 2) return s.length;
  let i =0, j =0, max = 0;

  let mySet = new Set();
  while(j < s.length) {
    if(!mySet.has(s[j])) {
      mySet.add(s[j++]);
      max = Math.max(max, mySet.size);
    } else mySet.delete(s[i++]);
  }
  return max;
}
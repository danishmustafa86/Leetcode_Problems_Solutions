function thirdMax(nums: number[]): number {
    // const set=new Set(nums)
    // let max1=Math.max(...set)
    //     if (nums.length<3) return max1
    // set.delete(max1)
    // let max2=Math.max(...set)
    // set.delete(max2)
    // let max3=Math.max(...set)
    //    return max3    
          const set = new Set(nums);
  const first = Math.max(...set);
  if (set.size < 3) return first;
  set.delete(first);
  const second = Math.max(...set);
  set.delete(second);
  return Math.max(...set);
    };
function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
  let answer: boolean[] = []
  let maxkinds = Math.max(...candies)
  candies.map((e) => {
    if (e + extraCandies >= maxkinds) {
      answer.push(true)
    }
    else {
      answer.push(false)
    }
  })
  return answer
};
console.log(kidsWithCandies([2, 4, 345, 341], 4));

// function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
//     let maximumNum=math.max(...candies)
// for(let i=0;i<candies.length;i++){
//     let n=candies[i+extraCandies]
// if(candies[i+extraCandies]{math.max(n)}}};
function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    const maxNumber: number = Math.max(...candies);
    return candies.map(el => el + extraCandies >= maxNumber );
};
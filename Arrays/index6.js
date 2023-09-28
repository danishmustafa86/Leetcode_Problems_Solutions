function kidsWithCandies(candies, extraCandies) {
    var answer = [];
    var maxkinds = Math.max.apply(Math, candies);
    candies.map(function (e) {
        if (e + extraCandies >= maxkinds) {
            answer.push(true);
        }
        else {
            answer.push(false);
        }
    });
    return answer;
}
;
console.log(kidsWithCandies([2, 4, 345, 341], 4));

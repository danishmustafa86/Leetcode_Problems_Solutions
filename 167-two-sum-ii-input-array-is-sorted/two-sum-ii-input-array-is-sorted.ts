function twoSum(numbers: number[], target: number): number[] {
    let arr=[]
    for( let i=0; i<numbers.length;i++){
        for(let j=i+1;j<numbers.length;j++){
            if(numbers[i]+numbers[j]==target){
                arr.push(i+1,j+1)
            }
        }
    }
    return arr
};
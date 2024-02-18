function replaceElements(arr: number[]): number[] {
    let array:number[]=[]
    if(arr.length==0){
        return array
    }
    let result =-1
    for(let i=arr.length-1;i>=0;i--){
        array[i]=result
        result=Math.max(result,arr[i])
    }
    return array

}; 
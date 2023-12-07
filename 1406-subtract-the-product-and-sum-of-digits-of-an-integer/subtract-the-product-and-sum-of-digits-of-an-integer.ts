function subtractProductAndSum(n: number) {
let st:string=n.toString()
let product:number=1;
let sum:number=0
    for(let i=0;i<st.length;i++){
let n2:number=parseInt(st[i])
product=product*n2
sum=sum+n2
console.log(n2);


}
console.log(product);
console.log(sum);
return product-sum
};
console.log(subtractProductAndSum(2783));


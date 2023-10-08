function largestAltitude(ga: number[]): number {
 let c=0
 let m=0
 for(let i=0;i<ga.length;i++){
     c+=ga[i]
     m=Math.max(c,m)
 }
 return m
};
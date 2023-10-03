function largestAltitude(gain: number[]): number {
 let currentgain=0
 let maxgain=0
 for(let i=0;i<gain.length;i++){
     currentgain+=gain[i]
     maxgain=Math.max(currentgain,maxgain)
 }
 return maxgain
};
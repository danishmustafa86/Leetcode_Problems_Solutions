function minCostToMoveChips(position: number[]): number {
let even:number=0
let odd:number=0
for (let i = 0; i < position.length; i++) {
    if (position[i]%2==0) {
        even++
    }
    if (position[i]%2==1) {
        odd++
    }
    if (even==position.length||odd==position.length) {
        return 0
    }
}
return Math.min(even,odd)
};
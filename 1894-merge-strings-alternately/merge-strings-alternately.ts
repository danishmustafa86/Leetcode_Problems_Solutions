function mergeAlternately(w1:string,w2:string):string{
    let merg="";
    for(let i:number=0;i<Math.max(w1.length,w2.length);i++){
        if(i<w1.length) merg+=w1[i]
        if(i<w2.length) merg+=w2[i]
    }
    return merg
}
mergeAlternately
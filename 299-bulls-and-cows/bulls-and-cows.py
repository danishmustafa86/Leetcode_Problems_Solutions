class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        smap,gmap = {},{}
        cow,bull = 0,0
        for i,j in zip(secret, guess):
            if i == j:
                bull += 1
            else:
                smap[i] = smap.get(i,0) + 1
                gmap[j] = gmap.get(j,0) + 1
        for i in smap:
            if i in gmap:
                cow += min(smap[i],gmap[i])
        return f"{bull}A{cow}B"

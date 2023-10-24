function defangIPaddr(address: string):string {
let mstring:string=address.replace(/\./g,"[.]")
return mstring
}
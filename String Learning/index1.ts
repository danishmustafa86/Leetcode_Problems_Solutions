//  Input: address = "1.1.1.1"
// Output: "1[.]1[.]1[.]1"
function defangIPaddr(address: string):string {
let mstring:string=address.replace(/\./g,"[.]")
return mstring
}

const address = "1.1.1.1";
const formattedAddress = defangIPaddr(address);
console.log(formattedAddress); // Output: "1[.]1[.]

    
         
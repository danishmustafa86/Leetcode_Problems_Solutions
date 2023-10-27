//  Input: address = "1.1.1.1"
// Output: "1[.]1[.]1[.]1"
function defangIPaddr(address) {
    var mstring = address.replace(/\./g, "[.]");
    return mstring;
}
var address = "1.1.1.1";
var formattedAddress = defangIPaddr(address);
console.log(formattedAddress); // Output: "1[.]1[.]
// let len:number=address.length
// let mString:string=""
// for (let i = 0; i < address.length; i++) {
//            if (i%2==0) {
//     } else {
//     }

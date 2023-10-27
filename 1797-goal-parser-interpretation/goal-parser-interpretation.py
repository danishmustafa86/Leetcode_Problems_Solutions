# Typescript code

#    let str:string=""
# for (let i = 0; i < command.length; i++) {
#     if (command[i]=="G") {
#         str=str.concat("G")
#     }
#     else if (command[i]=="(" && command[i+1]==")") {
#         str=str.concat("o")
#     }
#     else if (command[i]=="(" && command[i+3]==")") {
#         str=str.concat("al")
#     }
#     else{
#         str=str.concat("")
#     }
# }
# return str
# };
class Solution(object):
    def interpret(self, command):
        result = ""
        i = 0

        while i < len(command):
            if command[i] == "G":
                result += "G"
                i += 1
            elif command[i] == "(" and command[i + 1] == ")":
                result += "o"
                i += 2
            elif command[i] == "(" and command[i + 3] == ")":
                result += "al"
                i += 4
            else:
                i += 1

        return result

let inputs = readLine()!
var tmp = ""
var flag = false
for i in inputs.indices {
    if(flag == false && inputs[i] == "<"){
        print(String(tmp.reversed()), terminator: "")
        tmp = "<"
        flag = true
    }
    else if(inputs[i] == ">"){
        tmp += ">"
        flag = false
        print(tmp, terminator: "")
        tmp = ""
    }
    else if(flag == true){
        tmp += String(inputs[i])
    }
    else if(inputs[i] == " "){
        print(String(tmp.reversed())+" ", terminator: "")
        tmp = ""
    }
    else if( i == inputs.index(before: inputs.endIndex) ){
        tmp += String(inputs[i])
        print(String(tmp.reversed()))
    }
    else{
        tmp += String(inputs[i])
    }
}

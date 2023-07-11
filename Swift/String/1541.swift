let inputs = readLine()!+"\n"
var ans = 0
var s = 0
var flag = false
var tmp = ""
for i in inputs.indices {
    if(inputs[i] != "+" && inputs[i] != "-" && inputs[i] != "\n"){
        tmp += String(inputs[i])
    }
    else if(inputs[i] == "+"){
        ans = flag == true ? ans - Int(tmp)! : ans + Int(tmp)!
        tmp = ""
    }
    else if(inputs[i] == "-"){
        ans = flag == true ? ans - Int(tmp)! : ans + Int(tmp)!
        flag = true
        tmp = ""
    }
    else{
        ans = flag == true ? ans - Int(tmp)! : ans + Int(tmp)!
    }
}
print(ans)

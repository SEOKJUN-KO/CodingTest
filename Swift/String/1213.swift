let inputs = readLine()!

var dict = [Character: Int]()
for i in inputs.indices{
    dict[inputs[i]] = dict[inputs[i], default: 0] + 1
}

var ans = ""
if inputs.count%2 == 0{
    for k in dict.keys.sorted(){
        if(dict[k]!%2 == 1){
            ans = "No"
            break
        }
        ans += String(repeating: k, count: dict[k]!/2)
    }
    if(ans == "No"){
        print("I'm Sorry Hansoo")
    }
    else{
        print(ans+String(ans.reversed()))
    }
}
else{
    var flag = false
    var odd = ""
    for k in dict.keys.sorted(){
        if(dict[k]!%2 == 1 && flag == false){
            flag = true
            odd = String(k)
            ans += String(repeating: k, count: dict[k]!/2)
        }
        else if(dict[k]!%2 == 1 && flag){
            ans = "No"
            break
        }
        else{
            ans += String(repeating: k, count: dict[k]!/2)
        }
    }
    if(ans == "No"){
        print("I'm Sorry Hansoo")
    }
    else{
        print(ans+odd+String(ans.reversed()))
    }
}

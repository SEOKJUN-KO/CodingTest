var S = Array(readLine()!)
var T = Array(readLine()!)

if( S.count > T.count ){
    ( S, T ) = ( T, S )
}

while(S.count < T.count){
    if( T.last! == "A" ){
        _ = T.popLast()
    }
    else{
        _ = T.popLast()
        T = Array(T.reversed())
    }
}
if(S == T){
    print(1)
}
else{
    print(0)
}

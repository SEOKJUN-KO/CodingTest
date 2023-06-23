class minHeap {
    var nodes: [Int] = [-1]
    
    func isNotEmpty() -> Bool {
        if(nodes.count > 1){
            return true
        }
        return false
    }
    
    func heappush(_ val: Int) {
        nodes.append(val)
        swapUp(nodes.count-1)
    }
    
    func swapUp(_ index: Int){
        if(index == 1){
            return
        }
        if(nodes[index] < nodes[index/2]){
            ( nodes[index], nodes[index/2] ) = ( nodes[index/2], nodes[index] )
            swapUp(index/2)
        }
    }
    
    func heappop() -> Int {
        let out = nodes[1]
        nodes[1] = nodes.last!
        var _ = nodes.popLast()
        if(isNotEmpty()){
            swapDown(1)
        }
        
        return out
    }
    
    func swapDown(_ index: Int) {
        if(index > nodes.count-1){
            return
        }
        let right = index*2+1
        let left = right - 1
        var tmp = index
        if( left < nodes.count && nodes[tmp] > nodes[left] ){
            tmp = left
        }
        if( right < nodes.count && nodes[tmp] > nodes[right] ) {
            tmp = right
        }
        if(tmp != index){
            ( nodes[index], nodes[tmp] ) = ( nodes[tmp], nodes[index] )
            swapDown(tmp)
        }
    }
}

var heapq = minHeap()

let input = readLine()!

for i in input.unicodeScalars {
    heapq.heappush(Int(i.value))
}
while(heapq.isNotEmpty()){
    print(Character(UnicodeScalar(heapq.heappop())!))
}

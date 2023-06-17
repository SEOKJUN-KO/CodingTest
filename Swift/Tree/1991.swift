import Foundation

let n = Int(readLine()!)!
var dic = [String: [String]]()
for _ in 0...n-1 {
    let nodes = readLine()!.split(separator: " ").map{String($0)}
    dic[nodes[0], default:[]].append(nodes[1])
    dic[nodes[0], default:[]].append(nodes[2])
}
func preOrdered(_ node: String) {
    if (node == ".") {
        return
    }
    print(node, terminator: "")
    preOrdered(dic[node, default: [".", "."]][0])
    preOrdered(dic[node, default: [".", "."]][1])
}
func inOrdered(_ node: String) {
    if (node == ".") {
        return
    }
    inOrdered(dic[node, default: [".", "."]][0])
    print(node, terminator: "")
    inOrdered(dic[node, default: [".", "."]][1])
}
func postOrdered(_ node: String) {
    if (node == ".") {
        return
    }
    postOrdered(dic[node, default: [".", "."]][0])
    postOrdered(dic[node, default: [".", "."]][1])
    print(node, terminator: "")
}
preOrdered("A")
print()
inOrdered("A")
print()
postOrdered("A")

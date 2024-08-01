import Foundation


func superDigit(n: String, k: Int) -> Int {
    var arr = n.map{ Int(String($0))! }
    var flag = true
    while(arr.count > 1) {
        if flag {
            arr = Array(String(arr.reduce(0, +)*k)).map{ Int(String($0))! }
            flag = false
        }
        else{
            arr = Array(String(arr.reduce(0, +))).map{ Int(String($0))! }
        }
    }
    
    return arr[0]
}

let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let firstMultipleInputTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }
let firstMultipleInput = firstMultipleInputTemp.split(separator: " ").map{ String($0) }

let n = firstMultipleInput[0]

guard let k = Int(firstMultipleInput[1])
else { fatalError("Bad input") }

let result = superDigit(n: n, k: k)

fileHandle.write(String(result).data(using: .utf8)!)
fileHandle.write("\n".data(using: .utf8)!)

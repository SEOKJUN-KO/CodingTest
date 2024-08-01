import Foundation

func isBalanced(s: String) -> String {
    var stack = [String.Element]()
    for c in s {
        if stack == [] {
            stack.append(c)
            continue
        }
        if (stack.last! == "[" && c == "]") || (stack.last! == "(" && c == ")" ) || (stack.last! == "{" && c == "}"){
            _ = stack.popLast()
        }
        else {
            stack.append(c)
        }
    }
    if stack == [] {
        return "YES"
    }
    else {
        return "NO"
    }
    
}

let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let t = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

for tItr in 1...t {
    guard let s = readLine() else { fatalError("Bad input") }

    let result = isBalanced(s: s)

    fileHandle.write(result.data(using: .utf8)!)
    fileHandle.write("\n".data(using: .utf8)!)
}

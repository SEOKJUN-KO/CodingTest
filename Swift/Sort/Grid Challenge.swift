import Foundation

func gridChallenge(grid: [String]) -> String {
    var arr = [[String]]()
    for i in 0..<grid.count {
        arr.append(Array(grid[i].map{ String($0) }).sorted())
        if i == 0 { continue }
        for j in 0..<arr[i].count {
            if arr[i-1][j] > arr[i][j] { return "NO" }
        }
    }
    
    return "YES"
}

let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let t = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

for tItr in 1...t {
    guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
    else { fatalError("Bad input") }

    var grid = [String]()

    for _ in 1...n {
        guard let gridItem = readLine() else { fatalError("Bad input") }

        grid.append(gridItem)
    }

    guard grid.count == n else { fatalError("Bad input") }

    let result = gridChallenge(grid: grid)

    fileHandle.write(result.data(using: .utf8)!)
    fileHandle.write("\n".data(using: .utf8)!)
}

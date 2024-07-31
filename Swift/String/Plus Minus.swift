import Foundation

func plusMinus(arr: [Int]) -> Void {
  var plusCnt = 0, minusCnt = 0, zeroCnt = 0
  for value in arr {
    if (value > 0) { plusCnt += 1 }
    else if (value == 0) { zeroCnt += 1}
    else { minusCnt += 1}
  }
  print( String(format: "%.6f", Double(plusCnt)/Double(arr.count)) )
  print( String(format: "%.6f", Double(minusCnt)/Double(arr.count)) )
  print( String(format: "%.6f", Double(zeroCnt)/Double(arr.count)) )
}

guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

guard let arrTemp = readLine()?.replacingOccurrences(of: "\\s+$", with: "", options: .regularExpression) else { fatalError("Bad input") }

let arr: [Int] = arrTemp.split(separator: " ").map {
    if let arrItem = Int($0) {
        return arrItem
    } else { fatalError("Bad input") }
}

guard arr.count == n else { fatalError("Bad input") }

plusMinus(arr: arr)

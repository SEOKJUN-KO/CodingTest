var arr = [[String]]()
var dict = [String: [String]]()
var store = [String]()
var L = 0
func backT(from: String) {
    if store.count == L {
        return
    }
    if dict[from] == nil { return }
    for i in 0..<dict[from]!.count {
        if !dict[from]![i].isEmpty {
            let to = dict[from]![i]
            dict[from]![i] = ""
            store.append(to)
            backT(from: to)
            if store.count == L { return }
            _ = store.popLast()
            dict[from]![i] = to
        }
    }
}

func solution(_ tickets:[[String]]) -> [String] {
    arr = tickets.sorted(by: { ($0[0], $0[1]) < ($1[0], $1[1]) })
    L = arr.count + 1
    for a in arr {
        let (from, to) = (a[0], a[1])
        if dict[from] == nil { dict[from] = [] }
        dict[from]!.append(to)
    }
    store.append("ICN")
    backT(from: "ICN")
    return store
}

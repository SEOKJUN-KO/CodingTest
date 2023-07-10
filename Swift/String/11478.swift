let inputs = readLine()!
var s = Set<Substring>()
for i in inputs.indices{
    for j in inputs[i...].indices{
        s.insert(inputs[i...j])
    }
}
print(s.count)

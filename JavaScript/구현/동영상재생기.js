function numToString(totalSecond) {
    let [m, s] = [Math.floor(totalSecond/60), totalSecond%60]
        .map(v => (v < 10 ? "0"+v : ""+v));
    return m + ":" + s;
}


function pre(now) {
    const [m, s] = now.split(":").map((d) => Number(d))
    let totalSecond = Math.max(m*60 + s - 10, 0)
    return numToString(totalSecond)
}

function next(now, video_len) {
    const [m, s] = now.split(":").map((d) => Number(d))
    const [M, S] = video_len.split(":").map((d) => Number(d))
    let totalSecond = Math.min(m*60 + s + 10, M*60+S)
    return numToString(totalSecond)
}

function isInOP(now, op_start, op_end) {
    const [m, s] = now.split(":").map((d) => Number(d))
    const [m_s, s_s] = op_start.split(":").map((d) => Number(d))
    const [m_e, s_e] = op_end.split(":").map((d) => Number(d))
    if (60*m_s+s_s <= 60*m+s && 60*m+s <= 60*m_e+s_e) { return true }
    return false
}

function solution(video_len, pos, op_start, op_end, commands) {
    var ans = '';
    let now = pos;
    commands.forEach((c) => {
        if ( isInOP(now, op_start, op_end) ) {
            now = op_end
        }
        if (c === "prev") { now = pre(now) }
        else { now = next(now, video_len)}
        if ( isInOP(now, op_start, op_end) ) {
            now = op_end
        }
    })
    return now
}
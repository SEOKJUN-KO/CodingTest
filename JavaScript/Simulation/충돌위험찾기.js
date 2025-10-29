// 충돌 지점 찾기
// 이동 중 같은 좌표에 로봇이 2대 이상 모인 경우

const positions = new Map()
function makePosition(points) {
    for ( let i in points ) {
        let [y, x] = points[i]
        positions.set(Number(i)+1, [y, x])
    }
}

const robots = new Map()
function makeRobot(routes) {
    for (let i in routes) {
        let arr = routes[i]
        robots.set(Number(i)+1, {'now': positions.get(arr[0]), 'target': 1, 'arr': arr })
    }
}

function move(nowP, targetP) {
    
    let [nowY, nowX] = nowP
    let [targetY, targetX] = targetP
    // 위
    if ( nowX === targetX && nowY > targetY ) {
        return [nowY-1, nowX]
    }
    // 아래
    if ( nowX === targetX && nowY < targetY ) {
        return [nowY+1, nowX]
    }
    // 왼쪽
    if ( nowY === targetY && nowX > targetX ) {
        return [nowY, nowX-1]
    }
    // 오른쪽
    if ( nowY === targetY && nowX < targetX ) {
        return [nowY, nowX+1]
    }
    
    // 위
    if (nowY > targetY) {
        return [nowY-1, nowX]
    }
    // 아래
    if (nowY < targetY) {
        return [nowY+1, nowX]
    }
}

function checkCrush(visit) {
    let cnt = 0
    for ( let [key, value] of visit.entries() ) {
        if (value >= 2) cnt += 1
    }
    return cnt
}

function calculateCrush() {
    let answer = 0    
    visit = new Map()
    for ( let [key, value] of robots.entries() ) {
        now = value['now']
        let qwer = String(now[0])+" "+String(now[1])
        if ( visit.get(qwer) === undefined ) { visit.set(qwer, 0) }
        visit.set(qwer, visit.get(qwer)+1)
    }
    answer += checkCrush(visit)
    while(robots.size > 0) {
        let keyStore = []
        visit = new Map()
        for ( let [key, value] of robots.entries() ) {
            now = value['now']
            target = value['target']
            arr = value['arr']
            targetP = positions.get(arr[target])
            now = move(now, targetP)
            let qwer = String(now[0])+" "+String(now[1])
            if ( visit.get(qwer) === undefined ) { visit.set(qwer, 0) }
            visit.set(qwer, visit.get(qwer)+1)
            
            if (now[0] === targetP[0] && now[1] === targetP[1]) {
                target += 1
                if (arr.length === target) {
                    keyStore.push(key)
                }
                else robots.set(key, {'now': now, 'target': target, 'arr': arr })
            }
            else {
                robots.set(key, {'now': now, 'target': target, 'arr': arr })
            }
        }
        
        for (let k of keyStore) {
            robots.delete(k)
        }
        answer += checkCrush(visit)
    }
    return answer
}

function solution(points, routes) {
    makePosition(points)
    makeRobot(routes)
    return calculateCrush();
}
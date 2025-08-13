function attack(status, damage, attackIdx) {
    status -= damage
    attackIdx += 1
    return [status, attackIdx, 0]
}

function heal(cnt, status, bandage, health) {
    cnt += 1
    if (cnt === bandage[0]) { status += (bandage[1] + bandage[2]); cnt = 0}
    else { status += bandage[1]}
    status = Math.min(status, health)
    return [status, cnt]
}

function eachSecond(bandage, health, attacks) {
    let lastAttackTime = attacks[attacks.length-1][0]
    let status = health
    let attackIdx = 0
    let cnt = 0
    
    for( let i = 1; i <= lastAttackTime; i++ ) {
        if (attackIdx < attacks.length && i === attackTime) {
            const [attackTime, damage] = attacks[attackIdx]
            [status, attackIdx, cnt] = attack(status, damage, attackIdx)
            if (status <= 0) { return -1 }
        }
        else {
            [status, cnt] = heal(cnt, status, bandage, health)
        }
    }
    return status
}

function solution(bandage, health, attacks) {
    var ans = 0;
    return eachSecond(bandage, health, attacks)
}
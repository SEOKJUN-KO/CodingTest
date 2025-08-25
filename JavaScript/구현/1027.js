function degree(ynow, xnow, ynext, xnext) {
    return (ynext - ynow) / (xnext - xnow);
}

function left(buildings) {
    let lrr = [0];
    for (let i = 1; i < buildings.length; i++) {
        let [ynow, xnow] = [buildings[i], i];
        let D = Number.MAX_VALUE;
        let c = 0;
        for (let j = i - 1; j >= 0; j--) {
            let [ynext, xnext] = [buildings[j], j];
            const d = degree(ynow, xnow, ynext, xnext);
            if (d < D) {
                D = d;
                c += 1;
            }
        }
        lrr.push(c);
    }
    return lrr;
}

function right(buildings) {
    let rrr = [];
    for (let i = 0; i < buildings.length; i++) {
        let [ynow, xnow] = [buildings[i], i];
        let D = -Number.MAX_VALUE;
        let c = 0;
        for (let j = i + 1; j < buildings.length; j++) {
            let [ynext, xnext] = [buildings[j], j];
            const d = degree(ynow, xnow, ynext, xnext);
            if (d > D) {
                D = d;
                c += 1;
            }
        }
        rrr[i] = c;
    }
    return rrr;
}

function main() {
    const fs = require("fs");
    const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

    const _ = Number(input[0]); // N
    const buildings = input[1].split(" ").map(Number);

    let lrr = left(buildings);
    let rrr = right(buildings);

    let arr = [];
    for (let i = 0; i < buildings.length; i++) {
        arr.push(lrr[i] + rrr[i]);
    }
    console.log(Math.max(...arr));
}

main();

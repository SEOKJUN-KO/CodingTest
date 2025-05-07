// ✅ 1. 1차원 숫자 배열 정렬
const nums = [5, 2, 8, 1, 3];

const numsAsc = [...nums].sort((a, b) => {
  if (a > b) return 1;
  if (a < b) return -1;
  return 0;
});

const numsDesc = [...nums].sort((a, b) => {
  if (a < b) return 1;
  if (a > b) return -1;
  return 0;
});

console.log("🔢 1차원 숫자 배열");
console.log("오름차순:", numsAsc);   // [1, 2, 3, 5, 8]
console.log("내림차순:", numsDesc); // [8, 5, 3, 2, 1]


// ✅ 2. 1차원 문자열 배열 정렬
const words = ["banana", "apple", "cherry"];

const wordsAsc = [...words].sort((a, b) => {
  if (a > b) return 1;
  if (a < b) return -1;
  return 0;
});

const wordsDesc = [...words].sort((a, b) => {
  if (a < b) return 1;
  if (a > b) return -1;
  return 0;
});

console.log("\n🔤 1차원 문자열 배열");
console.log("오름차순:", wordsAsc);   // ["apple", "banana", "cherry"]
console.log("내림차순:", wordsDesc); // ["cherry", "banana", "apple"]


// ✅ 3. 2차원 숫자 배열 정렬: [0] 오름차순, [1] 내림차순
const twoDimNum = [
  [2, 3],
  [1, 5],
  [2, 5],
  [1, 2],
  [2, 1]
];

twoDimNum.sort((a, b) => {
  if (a[0] > b[0]) return 1;
  if (a[0] < b[0]) return -1;
  if (a[1] < b[1]) return 1;
  if (a[1] > b[1]) return -1;
  return 0;
});

console.log("\n🔢 2차원 숫자 배열 정렬 [0 오름차순, 1 내림차순]");
console.log(twoDimNum);
// 결과: [[1,5], [1,2], [2,5], [2,3], [2,1]]


// ✅ 4. 2차원 문자열 배열 정렬: [0] 오름차순, [1] 내림차순
const twoDimStr = [
  ["banana", "cat"],
  ["apple", "dog"],
  ["banana", "ant"],
  ["apple", "zebra"]
];

twoDimStr.sort((a, b) => {
  if (a[0] > b[0]) return 1;
  if (a[0] < b[0]) return -1;
  if (a[1] < b[1]) return 1;
  if (a[1] > b[1]) return -1;
  return 0;
});

console.log("\n🔤 2차원 문자열 배열 정렬 [0 오름차순, 1 내림차순]");
console.log(twoDimStr);
// 결과: [["apple", "zebra"], ["apple", "dog"], ["banana", "cat"], ["banana", "ant"]]
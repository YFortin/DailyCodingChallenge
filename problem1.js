

function betterAnswer (numbers, k) {
    const remainders = new Set();
    for (number of numbers) {
        if (number <= k) {
            if (remainders.has(number)) {
                return true;
            } else {
                remainders.push(k - number);
            }
        }
    }
    return false;
}

function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
  }

function makeList() {
    const nums = []
    for (i = 0; i < 100000; i++) {
        nums.push(getRandomArbitrary(1, 100));
    }
    return nums;
}


const start = new Date();
const liste = makeList();
betterAnswer(liste, 0);
const stop = new Date() - start;
console.log(stop/1000);
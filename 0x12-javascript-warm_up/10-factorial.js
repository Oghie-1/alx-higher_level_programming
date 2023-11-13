#!/usr/bin/node

//prints factorial
//must use function
//must be recursive


function factorial (n) {
	if ((isNaN(n)) || (n === 1)) {
		return 1;
	} else {
		return n * factorial(n - 1);
	}
}

console.log(factorial(parseInt(process.argv[2])));

#!/usr/bin/node

// Prints the size of the square
// argv is the size of the square


if (isNaN(process.argv[2])) {
    console.log("Missing size");
} else {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
        console.log('X'.repeat(parseInt(process.argv[2])));
    }
}

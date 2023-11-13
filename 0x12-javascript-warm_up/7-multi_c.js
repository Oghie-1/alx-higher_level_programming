#!/usr/bin/node

// Prints x times of "C is fun"
// If the argument can't be converted to an integer, print "Missing Number of occurrences"

const lang = 'C is Fun';

if (isNaN(process.argv[2])) {
    console.log("Missing number of occurrences");
} else {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
        console.log(lang);
    }
}

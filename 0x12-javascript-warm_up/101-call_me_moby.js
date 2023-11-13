#!/usr/bin/node
//executes xtimes the function


exports.callMeMoby = function (x, theFunction) {
	for (let i = 0; i < x; i++) {
		theFunction();
	}
};

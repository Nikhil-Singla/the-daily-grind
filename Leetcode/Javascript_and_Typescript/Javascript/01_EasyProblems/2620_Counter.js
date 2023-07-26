/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) 
{
    let adder = -1;
    return function() 
    {
        adder+=1;
        return n+adder;    
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
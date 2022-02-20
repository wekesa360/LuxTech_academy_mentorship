// program to check if number is fibonacci

/**
 * isPerfectSquare - checks if number is a perfect square
 * @n - a number of type int
 * 
 * return - true if n is perfect square else false
 */
function isPerfectSquare(n){
    let value = parseInt(Math.sqrt(n));
    return (value * value === n);
}

/**
 * isFibonacci - checks if a number is Fibonacci
 * @n - a number of type int
 * 
 * return - true if n is Fibonacci else false
 */
function isFibonacci(n){

    // n is Fibonacci if one of 5*n*n - 4 or both
    // is a perfect square
    return (isPerfectSquare(5*n*n + 4) ||
            isPerfectSquare(5*n*n - 4));
}

for (let i = 0; i <= 30; i++){
    isFibonacci(i)? console.log(i + " is a Fibonacci number.") :
    console.log(i + " is not a Fibonacci number.");
}
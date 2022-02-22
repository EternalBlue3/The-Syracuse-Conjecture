function isEven(n) {
    return (n % 2 == 0);
};

function generate_collatz() {
    var n = parseInt(prompt("Enter a start number for collatz sequence: "));
    var output_collatz = [];
    while (n != 1)
    {
    output_collatz.push(" " + n)
    if ((n & 1) != 0) 
       n = 3*n + 1;
    else
       n = parseInt(n/2, 10);
    };
    alert("Generated Collatz Sequence: " + output_collatz + ", 1");};

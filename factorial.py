def factorial(n):      
    # find factorial 
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1); 
  

number = 5; 
print("Factorial of", number, 
      "is", factorial(number)); 
import os


def is_prime(n):
    #check if a  number is prime
    if n <=1:
        return False
    if n ==2:
        return True
    if n%2 ==0:
        return False
    for i in range(3,int(n**0.5)+1, 2):
        if n%i ==0:
            return False
        
    return True

#Generate prime numbers between 1 and 250
primes = [str(num) for num in range(1, 251) if is_prime(num)]

file_name = "results.txt"
abs_path = os.path.abspath(file_name)

#write to file
with open(file_name,"w") as f:
    f.write("Prime numbers between 1 and 250: \n")
    f.write(",".join(primes))

print(f"Prime numbers successfully writeen to: {abs_path}")
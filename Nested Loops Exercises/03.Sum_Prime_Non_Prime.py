prime_sum = 0
non_prime_sum = 0
line = input()
while line != "stop":
    number = int(line)

    if number < 0:
        print("Number is negative.")
    else:

        counter = 0
        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1

        if counter == 2:
            prime_sum += number
        elif counter > 2:
            non_prime_sum += number
    line = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")



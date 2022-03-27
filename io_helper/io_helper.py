from utility import utility

def input_integer(prompt):
    while True:
        try:
            integer_candidate = int(input(prompt))
            return integer_candidate
        except ValueError as e:
            print(f"The value you entered is not an integer")
            continue

def input_prime(prompt):
    while True:
        prime_candidate = int(input(prompt))
        if utility.is_prime(prime_candidate):
            return prime_candidate
        else:
            print(f"{prime_candidate} is not a prime number")

def input_generator(prime_number, prompt):
    while True: 
        generator_candidate = int(input(prompt))
        if utility.is_generator(generator_candidate, prime_number):
            return generator_candidate
        else:
            print(f"{generator_candidate} is not a valid generator")

def input_iv(prompt):
    while True:
        try:
            iv_candidate = int(input(prompt))
            if 0 <= iv_candidate and iv_candidate <= 255:
                return iv_candidate
            else:
                print("Please enter a valid IV [0, 255]")
        except ValueError as e:
            print(f"The value you entered is not an integer")
            continue
        

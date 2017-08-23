import random


# generate 4 digit random number
def num_gen():
    rand_num = []
    for i in range(0, 4):
        x = random.randint(0, 9)
        rand_num.append(x)
    return ''.join(map(str, rand_num))


# get user to input 4 digit number
# validate input is correct size
def get_input():
    validate = True
    while validate:
        user_input = input("Guess a number: ")
        if len(user_input) < 4 or len(user_input) > 4:
            print("Number must have 4 digits")
        else:
            validate = False
    return user_input


# convert integer numbers to list
def int_to_list(number):
    num_list = [int(x) for x in str(number)]
    return num_list


# compare random number list and user input list
# count the number of cows and bulls the user guessed
def compare_numbers(user_list, rand_list):
    cows_bulls = [0, 0]
    for i in range(0, 4):
        if user_list[i] in rand_list:
            if user_list[i] == rand_list[i]:
                cows_bulls[0] += 1
            else:
                cows_bulls[1] += 1
    return cows_bulls


# print the number of cows and bulls the user guessed in a string
def print_results(cows_bulls):
    print(str(cows_bulls[0]) + " cows, " + str(cows_bulls[1]) + " bulls")


def main():
    guess_count = 0
    pc = int_to_list(num_gen())
    check = True
    while check:
        human = int_to_list(get_input())
        guess_count += 1
        results = compare_numbers(pc, human)
        if results[0] < 4:
            print_results(results)
        else:
            check = False
    print_results(results)
    print("You won in " + str(guess_count) + " guesses")


if __name__ == "__main__":
    main()

# Exercise 1
numbers_1_to_10 = [1,2,3,4,5,6,7,8,9,10]
names = ['John', 'Emily', 'Thereza', 'Anna']
years = [1995,2024]

def iterate_list_numbers():
    for number in numbers_1_to_10:
        print(number)

def sum_odds():
    list_of_odds = []
    sum_of_odds = 0
    for number in numbers_1_to_10:
        if number % 2 == 0:
            continue
        else:
            list_of_odds.append(number)
            continue
    for number in list_of_odds:
        sum_of_odds = number + sum_of_odds
    print (f'A soma dos números ímpares é {sum_of_odds}')

def show_numbers_up_to_down():
    i=-1
    while i>-11:
        print (numbers_1_to_10[i])
        i = i-1
        
def show_the_table_of():
    i = 0
    user_request = int(input('Digite um número: '))
    while i<11:
        print(f'{user_request} X {i} = {user_request*i}')
        i=i+1

def sum_all_numbers():
    sum_total = 0
    for number in numbers_1_to_10:
        sum_total = number + sum_total
    print(f'A soma de todos os números é {sum_total}')

def average():
    sum_of_all = 0
    for number in numbers_1_to_10:
        sum_of_all = number + sum_of_all
    average = sum_of_all/len(numbers_1_to_10)
    print(f'A média dos número é {average}')
# Exercise 2
iterate_list_numbers()
# Exercise 3
sum_odds()
# Exercise 4
show_numbers_up_to_down()
#Exercise 5
show_the_table_of()
# Exercise 6
sum_all_numbers()
# Exercise 7
average()



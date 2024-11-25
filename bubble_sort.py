from random import randint as ri

big_number_list: list[int] = [ri(1, 10000) for _ in range(1000)]
some_numbers: list[int] = [5,7,21,6,9,0,3,45,98,12,32,49,52,1,36,84] #[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]#test numbers#
counter: int = 0
print(big_number_list)
while True:
    bubbled: bool = False
    counter += 1
    for i in range(len(big_number_list)-1):  
        if big_number_list[i] > big_number_list[i+1]:
            big_number_list[i+1], big_number_list[i] = big_number_list[i], big_number_list[i+1]
            bubbled = True
            
    if not bubbled:
        break

print(big_number_list)
print(f"Iterations: {counter}")
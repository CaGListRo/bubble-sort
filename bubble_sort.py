some_numbers = [5,7,21,6,9,0,3,45,98,12,32,49,52,1,36,84] #[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]#test numbers#
counter = 0
while True:
    bubbled = False
    counter += 1
    for i in range(len(some_numbers)-1):  
        if some_numbers[i] > some_numbers[i+1]:
            some_numbers[i+1], some_numbers[i] = some_numbers[i], some_numbers[i+1]
            bubbled = True
            
    if not bubbled:
        break

print(some_numbers)
print(f"Iterations: {counter}")
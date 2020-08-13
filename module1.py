#operator = input('Please enter the operator?')
#num1 = input('Please enter number 1?')
#num2 = input('Please enter number 2?')

def calc(operator,num1,num2):
    if operator == '+':
        result = int(num1) + int(num2)
    elif operator == '-':
        result = int(num1) - int(num2)
    elif operator == 'x':
        result = int(num1) * int(num2)
    elif operator == '/':
        result = int(num1) / int(num2)
    else:
        result = 'Error'
    print (result)

#file1 = open("C:\\Users\\p00012185\\Desktop\\step_2.txt", 'r')
with open('step_3.txt', 'r') as f:
    lines = f.read().splitlines()
for line in lines:
    list1 = line.split()
    print (list1)
    if list1[1] == 'calc':
        #calc(list1[2],list1[3],list1[4])
    #elif list

print (lines[5])

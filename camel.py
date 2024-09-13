camelcase = input("camelcase: ")
snake_case = ""
for i in range(len(camelcase)):
    if camelcase[i].isupper():
        snake_case = snake_case + '_' + camelcase[i].lower()
    else:
        snake_case += camelcase[i]
print("snake case: ",snake_case)

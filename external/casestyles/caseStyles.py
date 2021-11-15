snake_case = "snake_case"
camelCase = "camelCase"
PascalCase = "PascalCase"
# kebab-case = "kebab-case - not supported in Python" # generates Error
kebab_case1 = "kebab-case #1 - not supported in Python, var name is kebab_case (snake)"
kebab_case2 = "kebab-case #2 - used in HTML/CSS class / id"

caseStyles = (snake_case, camelCase, kebab_case1, kebab_case2, PascalCase)
for i in caseStyles:
    print(i)
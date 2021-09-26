dicionario = {
  "marca": "Volkswagen",
  "modelo": "Fusca",
  "ano": 1960
}

keys = []
for key in dicionario.keys():
  keys.append(key)

values = []
for value in dicionario.values():
  values.append(value)

print("Chaves(" + str(len(keys)) + "):")
for i in range (0, len(keys)):
    print(" - " + str(keys[i]))
    
print()

print("Valores(" + str(len(values)) + "):")
for i in range (0, len(values)):
    print(" - " + str(values[i]))

print()

for key in dicionario:
    print(key.capitalize(), end=": ")
    print(dicionario[key])
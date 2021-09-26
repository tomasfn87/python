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

print("Keys(" + str(len(keys)) + "):")
for i in range (0, len(keys)):
    print(" - " + str(keys[i]))
    
print()

print("Values(" + str(len(values)) + "):")
for i in range (0, len(values)):
    print(" - " + str(values[i]))
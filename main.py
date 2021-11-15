nome = input('Digite seu Nome: ')
nome_upper = nome.upper()

letters = {
    "A": "@",
    "E": "&",
    "I": "!",
    "O": "*",
    "U": "#"
}

for l in letters:
  print(l)
  nome_upper = nome_upper.replace(l, letters[l])

print (nome_upper)
  
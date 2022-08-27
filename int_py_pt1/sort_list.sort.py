def main():
	pets_lista = [
    ('Bisteca', 'C', 8),
    ('Churrasco', 'C', 6),
    ('Zig', 'F', 1),
	('Bidu', 'C', 15),
	]
#	sorted(pets_lista, key=lambda pets: pets[2])
	print("Alfabética: ", sorted(pets_lista, key=lambda ord: ord[0]))
	print("     Idade: ", sorted(pets_lista, key=lambda ord:  ord[2]))
main()
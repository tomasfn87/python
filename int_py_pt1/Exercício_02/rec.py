def main():

	nota = int(input("Insira a nota do aluno: "))

	if nota < 0 or nota > 10:
		nota = int(input("A nota deve ser entre 0 e 10. Insira novamente a nota do aluno: "))
		
	aRec = 0
		
	if ( nota >= 3 ) and ( nota <= 5 ): 
		aRec += 1
		if aRec == 0:
			print("Não tem nenhum aluno de rec")
		elif aRec == 1:
			print("Tem 1 aluno de rec")
		else:
			print("Tem", aRec, "alunos de rec")
main()

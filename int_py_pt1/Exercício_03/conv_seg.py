def main():
			
			ent_segs = input("Por favor, entre com o número de segundos que deseja converter: ")
			total_segs = int(ent_segs)
			
			dias = total_segs // (24*60**2)
			segs_rest1 = total_segs % (24*60**2)
			
			horas = segs_rest1 // (60**2)
			segs_rest2 = segs_rest1 % (60**2)
			
			minutos = segs_rest2 // 60
			segs_rest3 = segs_rest2 % 60
			
			print(dias, "dias,", horas, "horas,", minutos, "minutos e", segs_rest3, "segundos.")
main()
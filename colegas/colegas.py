def colegas_de_sala(salasprofs, professor):
	colegas = []
	sala = salasprofs[professor]
	for prof in salasprofs:
		if prof != professor and salasprofs[prof] == sala:
			colegas.append(prof)
	return colegas

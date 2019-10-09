safra = int(raw_input())
atacado = int(raw_input())
varejo = int(raw_input())

kg_atacado = safra/atacado
kg_varejo = safra%float(atacado)

print "Clientes no atacado = %ikg cada." %kg_atacado
print "Clientes no varejo = %.2fkg cada." %(kg_varejo/varejo)

# coding: UTF-8
# Seleção Projeto - TST - LUCAS GABRIEL


cre = float(raw_input())
experiencia = float(raw_input())
nota_entrevista = float(raw_input())

if cre < 7 and experiencia < 6:
    print "Candidato eliminado. CRE e experiência abaixo do limite."
elif cre < 7:
    print "Candidato eliminado. CRE abaixo do limite."
elif experiencia < 6:
    print "Candidato eliminado. Experiência abaixo do limite."
else:
    if nota_entrevista <= 3:
        print "Candidato classificado."
    else:
        print "Candidato aprovado."

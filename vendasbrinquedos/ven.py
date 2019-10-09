total = int(raw_input())
teresa = int(raw_input())
carla = int(raw_input())
joaquim = total-(teresa+carla)

print "Teresa vendeu %i (de %i) brinquedos. (%.2f%%)" %(teresa,total, (teresa*100.0/total))
print "Joaquim vendeu %i (de %i) brinquedos. (%.2f%%)" %(joaquim,total, (joaquim*100.0/total))
print "Carla vendeu %i (de %i) brinquedos. (%.2f%%)" %(carla,total, (carla*100.0/total))

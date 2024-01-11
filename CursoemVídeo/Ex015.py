d = int(input('Quantos dias você ficou com o carro: '))
km = float(input('Quantos km você rodou com o carro: '))
vd = d * 60
vkm = km * 0.15
vt = vd + vkm
print("O valor total a pagar é de R$ {:.2f}".format(vt))

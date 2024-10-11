
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]
n_pc = []
n_pb = []
n_pp = []

peso_mxn = 21.1739

for c in precios_comida:
    n_pc.append(round(c * peso_mxn,2))

for p in precios_bebida:
    n_pb.append(round(p * peso_mxn,2))

for b in precios_postres:
    n_pp.append(round(b * peso_mxn,2))

print(f'precios_comida = {n_pc}')
print(f'precios_bebida = {n_pb}')
print(f'precios_postres = {n_pp}')




lunas = ['Luna','Ceres','Deimos','Phobos']
print(lunas)

print(lunas[1:3])
print(lunas[0:2])
print(lunas[:3])
print(lunas[-1])
print(lunas[-2])

print(lunas[:-3])
print(lunas[:-2])
print(lunas[-3:-1])

print(lunas.append("Titan"))
print(lunas.insert(0,"Europa"))
print(lunas)

# lista[inicio:final:pasos]

print(lunas[::2])
print(lunas[1::3])

#orden inverso

print(lunas[::-1])

#append
lunas.append("Caronte")

#clear
a = [1,2,3]
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))
"""
del(a)
print(id(a))

"""
#copy

print("============")
b = lunas.copy()
print(id(lunas))
print(id(b))
b.pop()
print(lunas)
print(b)
print("********")

c = b

print(id(b))
print(id(c))

print("b: ",b)
print("c: ",c)

b.pop()
print("b: ",b)
print("c: ",c)

print(".........")
print("Veces que aparece Ceres en lunas: ",b.count("Ceres"))
print("..........")

#extend
A = [1,2,3]
B = [10,30,30]
A.extend(B)

print(A)
print(id(A))
print(id(B))
A.pop()
print(A)
print(B)

#index
indice = b.index("Deimos")
print(indice, ":", b[indice])
print("------------")
#Reverse
print(lunas[:-1])
lunas.reverse()
print(lunas)

#sort
print("..............")
lunas.sort()
print(lunas)
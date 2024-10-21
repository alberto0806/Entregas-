from math import factorial



def funcion_producto(n,k):
    producto = 1 
    for i in range(k + 1 ):
        producto *= (n - i +1)
    return producto


n = 4
k = 2
resultado = funcion_producto(n, k)
print(f"El resultado del producto es: {resultado}")


def producto_secuencia_geometrica(a1, r, k):
    product = 1 
    for n in range(1, k+1):
        an = a1 * (r**(n - 1))
        product *= an
    return product

print(' el producto de los primetos',k, 'terminos es',producto_secuencia_geometrica(3, 5, 2))

def numero_combinatorio(n,k):
    if k > n:
        return 'k debe ser menor que n'
    else:
        return factorial(n)// (factorial(k)*factorial(n-k))

print(numero_combinatorio(4, 2))


def s(n,k):
    if n<k:
        return 'n tiene que ser mayor que k'
    else:
        suma=0
        for i in range(k):
            numerador=((-1)**i)*numero_combinatorio(k+1, i+1)*((k-i)**n)
            suma += numerador
        return (suma/factorial(k))
    
print(s(4,2))


def f(x):
    return 2*x**2
def df(x):
    return 4*x
def newton(x0,tol,n):
    for k in range(n):
        x1=x0-f(x0)/df(x0)
        if abs(x1 - x0) < tol:
            print('x',k+1,'=',x1,' es la raiz')
            return 
        x0=x1
        print('x',k+1,'=',x1)

newton(3,0.01, 8)

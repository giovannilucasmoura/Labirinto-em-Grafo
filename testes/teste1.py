from Grafo import Grafo
from Vertice import Vertice

a = Vertice("a")
b = Vertice("b")
c = Vertice("c")
d = Vertice("d")
e = Vertice("e")
f = Vertice("f")
g = Vertice("g")
h = Vertice("h")
i = Vertice("i")
j = Vertice("j")
k = Vertice("k")

a.adicionarAresta(b)
a.adicionarAresta(c)
b.adicionarAresta(d)
b.adicionarAresta(e)
c.adicionarAresta(f)
c.adicionarAresta(g)
d.adicionarAresta(h)
e.adicionarAresta(i)
e.adicionarAresta(j)
f.adicionarAresta(k)
h.adicionarAresta(d)

GrafoBFS = Grafo([a, b, c, d, e, f, g, h, i, j])

print(GrafoBFS.buscaEmLargura(a, h))

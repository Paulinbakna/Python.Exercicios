**Semana 4: Estruturas de Dados**

- Listas, tuplas, conjuntos, dicionários
- Métodos e operações em listas e dicionários

---

========================== Exercícios ==============================

Ex1= Crie uma lista com 10 números e encontre o maior e o menor valor.

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Extruturas_de_dados/Ex1.py

---

Ex2= Construa um dicionário que armazene os nomes e idades de 5 pessoas e imprima a idade da pessoa mais velha.

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Extruturas_de_dados/Ex2.py

---

Ex3= Implemente um programa que remova duplicatas de uma lista.

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Extruturas_de_dados/Ex3.py

---

**Funções de Listas,Dicionarios e Tuplas** 


### Listas

As listas são coleções ordenadas e mutáveis de elementos. Elas são definidas usando colchetes `[]`.

**Exemplo de criação:**
```python
lista = [1, 2, 3, 'quatro', [5, 6]]
```

**Principais métodos e operações:**
- **`append(x)`**: Adiciona o elemento `x` ao final da lista.
- **`insert(i, x)`**: Insere o elemento `x` na posição `i`.
- **`remove(x)`**: Remove a primeira ocorrência do elemento `x`.
- **`pop([i])`**: Remove e retorna o elemento da posição `i` (por padrão, o último elemento).
- **`sort()`**: Ordena a lista in-place.
- **`reverse()`**: Inverte a lista in-place.
- **`index(x)`**: Retorna o índice da primeira ocorrência do elemento `x`.
- **`count(x)`**: Retorna o número de vezes que o elemento `x` aparece na lista.
- **`extend(iterável)`**: Adiciona todos os elementos de um iterável ao final da lista.

### Tuplas

As tuplas são coleções ordenadas e imutáveis de elementos. Elas são definidas usando parênteses `()`.

**Exemplo de criação:**
```python
tupla = (1, 2, 3, 'quatro')
```

**Principais operações:**
- As tuplas suportam a maioria das operações de listas (como indexação e fatiamento), mas como são imutáveis, não possuem métodos como `append` ou `remove`.

### Conjuntos

Os conjuntos são coleções não ordenadas de elementos únicos. Eles são definidos usando chaves `{}` ou a função `set()`.

**Exemplo de criação:**
```python
conjunto = {1, 2, 3, 4}
```

**Principais métodos e operações:**
- **`add(x)`**: Adiciona o elemento `x` ao conjunto.
- **`remove(x)`**: Remove o elemento `x` (gera um erro se `x` não estiver presente).
- **`discard(x)`**: Remove o elemento `x` (não gera erro se `x` não estiver presente).
- **`pop()`**: Remove e retorna um elemento aleatório do conjunto.
- **`union(iterável)`** ou `|`: Retorna a união de dois conjuntos.
- **`intersection(iterável)`** ou `&`: Retorna a interseção de dois conjuntos.
- **`difference(iterável)`** ou `-`: Retorna a diferença de dois conjuntos.
- **`symmetric_difference(iterável)`** ou `^`: Retorna a diferença simétrica de dois conjuntos.

### Dicionários

Os dicionários são coleções não ordenadas de pares chave-valor. Eles são definidos usando chaves `{}`.

**Exemplo de criação:**
```python
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
```

**Principais métodos e operações:**
- **`keys()`**: Retorna uma visão das chaves do dicionário.
- **`values()`**: Retorna uma visão dos valores do dicionário.
- **`items()`**: Retorna uma visão dos pares chave-valor do dicionário.
- **`get(chave, valor_padrao=None)`**: Retorna o valor para a chave `chave` se ela existir, senão retorna `valor_padrao`.
- **`update(outro_dicionario)`**: Atualiza o dicionário com os pares chave-valor de `outro_dicionario`.
- **`pop(chave)`**: Remove e retorna o valor associado à chave `chave`.
- **`popitem()`**: Remove e retorna o último par chave-valor inserido.
- **`clear()`**: Remove todos os itens do dicionário.

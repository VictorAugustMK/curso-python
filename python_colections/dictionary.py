"""

Dicionarios

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionarios são coleções do tipo chave/valor.

Dicionarios são representados por chaves {}.

print(type({}))

OBS: Sobre dicionarios
     - Chave e valor são separados por dois pontos 'chave:valor';
     - Tanto chave quanto valor pode ser de qualquer tipo de dado;
     - Podemos misturar tipos de dados;

# Criação de dicionarios
# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguia'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguia')

print(paises)
print(type(paises))

# Acessando elementos
# Forma 1 - Acessando via chaves, da mesma forma de uma lista/tupla

print(paises['br'])
# print(paises['ru'])
# OBS: Caso tentamos fazer uma acesso utilizando uma chave que não existe, temos um erro KeyError

# Forma 2 - Acessando de via get - Recomendado
print(paises.get('br'))
print(paises.get('ru'))

# Caso o get nao encontre o objeto com a chave informada sera retornado o valor None e nao sera gerado KeyErro

russia = paises.get('ru')

if russia:
    print(f'Encontrei o pais {pais}')
else:
    print('Não encontrei o pais')

# Podemos definir um valor padrao caso nao encontremos o objeto com a chave informada
pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o pais {pais}')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguia'}

# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusice lista, tupla dicionario, como chaves
# de dicionarios.

# Tuplas por exemplos sao interessantes de serem utilizadas como chave de dicionarios, pois as mesmas sao imutaveis
localidade = {
    (35.1231, 12.7631): 'Escritorio em Tokio',
    (40.6581, 74.8675): 'Escritorio em Nova York',
    (35.1297, 52.1261): 'Escritorio em São Paulo',
}

print(localidade)
print(type(localidade))

# Adicionar elementos em um dicionario
receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1

receita['abr'] = 350
print(receita)

# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado) # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionario
# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# CONCLUSAO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario e a mesma.
# CONCLUSAO 2: Em dicionarios, NAO podemos ter chaves repetidas.


# Remover dados de um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1
ret = receita.pop('mar')
print(ret)
print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso nao encontre o elemento, um KeyError e retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto e sempre retornado.

# Forma 2

del receita['fev']
print(receita)

# Se a chave nao existe sera gerado KeyError
# OBS: Neste caso o valor removido nao e encontrado

# Imagine que vc tem um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos

Carricho de Compras:
    Produto 1:
        - nome;
        - preco;
        - quantidade;
    Produto 2:
        - nome;
        - preco;
        - quantidade;

# 1 - Podemos utilizar uma lista para isso? Sim

carrinho = []
produto1 = ['PS 4',1, 2300.0]
produto2 = ['GOW 4',1, 150.0]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Teriamos que saber qual e o indice de cada informacao no produto.

# 2 - Poderiamos utilizar uma tupla para isso? Sim

produto1 = ('PS 4',1, 2300.0)
produto2 = ('GOW 4',1, 150.0)
carrinho = (produto1, produto2)

print(carrinho)
# Teriamos que saber qual e o indice de cada informacao no produto.

# 2 - Poderiamos utilizar uma dicionario para isso? Sim

carrinho = []
produto1 = {'nome':'PS 4', 'quantidade':1, 'valor':2300.0}
produto1 = {'nome':'GOW 4', 'quantidade':1, 'valor':150.0}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza
# ter a certeza sobre cada informacao.

# Metodos de dicionarios.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionario (Zerar dados)

d.clear()
print(d)

# Copiando um dicionario para outro

# Forma 1 # Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 # Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

"""

# Forma nao usual de criacao de dicionarios

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O metodo fromkeys recebe dois paramentros: um interavel e um valor.
# Ele vai gear para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11), 'novo')
print(veja)

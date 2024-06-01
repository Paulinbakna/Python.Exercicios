pessoas={'João':30,
         'Maria':25,
         'Clebin':35,
         'Junim':20,
         'Pedro':22}

pessoa_mais_velha= max(pessoas.values())
pessoa_mais_nova= min(pessoas.values())
for nome,idade in pessoas.items():
    if idade == pessoa_mais_velha:
        nome_mais_velho = nome
        break
for nome,idade in pessoas.items():
    if idade == pessoa_mais_nova:
        nome_mais_nova = nome
        break
print(f'A pessoa mais velha é : {nome_mais_velho} com  {pessoa_mais_velha} anos')
print(f'A pessoa mmais nova é : {nome_mais_nova} com {pessoa_mais_nova} anos')

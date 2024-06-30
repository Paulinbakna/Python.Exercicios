dados = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo",
    "habilidades": ["Python", "JavaScript", "SQL"]}

json_str = '{' + ', '.join(f'"{k}": "{v}"' if isinstance(v, str) else f'"{k}": {v}' if isinstance(v, int) else f'"{k}": ["' + '", "'.join(v) + '"]' for k, v in dados.items()) + '}'

open('dados_manual.json', 'w', encoding='utf-8').write(json_str)

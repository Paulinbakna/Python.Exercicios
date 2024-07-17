from datetime import datetime, timezone, timedelta
import time

# Definindo o fuso horário para UTC-3 (Brasília)
fuso_horario = timezone(timedelta(hours=-3))

# Obtendo a data e hora atuais com fuso horário
hora_hoje = datetime.now(fuso_horario)

# Extraindo o fuso horário
fuso_formatado = hora_hoje.strftime('%Z')

# Obtendo o nome do fuso horário local
nome_fuso_horario = time.tzname[time.localtime().tm_isdst]

print(f"Fuso horário: {nome_fuso_horario} {fuso_formatado}")

5. Datas e horários em diferentes fusos horários:

Converta a data e hora atuais para o fuso horário UTC+0 (Londres).

Crie uma variável que represente a data e hora em Nova York (fuso horário UTC-5).

Converta a variável de Nova York para o fuso horário local.
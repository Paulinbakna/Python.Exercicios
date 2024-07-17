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

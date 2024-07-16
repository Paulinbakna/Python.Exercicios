from datetime import datetime
import pytz

# Obtendo o horário UTC atual
utc_now = datetime.now(pytz.utc)

# Definindo a timezone desejada (por exemplo, America/Sao_Paulo)
timezone = pytz.timezone('America/Sao_Paulo')

# Convertendo o horário UTC para o horário local
local_now = utc_now.astimezone(timezone)

# Exibindo as informações
print(f"Fuso horário: {timezone}")
print(f"Horário local: {local_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

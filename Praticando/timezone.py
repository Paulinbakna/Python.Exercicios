from datetime import datetime
from zoneinfo import ZoneInfo

# Definindo a timezone desejada (por exemplo, America/Sao_Paulo)
timezone = ZoneInfo('America/Sao_Paulo')

# Obtendo o horário local na timezone definida
local_now = datetime.now(timezone)

# Exibindo as informações
print(f"Fuso horário: {timezone}")
print(f"Horário local: {local_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

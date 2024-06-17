class Usuario:
    def __init__(self,email):
        self._email=email
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,valor):
        if "@" not in valor or "." not in valor.split("@")[-1]:
            raise ValueError('Email inválido!')
        self._email=valor
        
    @email.deleter
    def email(self):
        self._email=None
        
try:
    usuario=Usuario('Junimdograu@gmail.com')
    print(f'Email do usuario: {usuario.email}')
    print('-'*15)
    usuario.email = 'Cleitindograu@gmail.com'
    print(f'Email do usuario: {usuario.email}')
    print('-'*15)
    usuario.email='Clebin.email'
except ValueError as e:
    print(e)
    
**Semana 2: Avançando em OOP**

- Herança
- Polimorfismo
- Encapsulamento

---

========================== Exercícios ==============================

Ex1= Crie uma classe `Veiculo` com atributos e métodos básicos, e herde essa classe para criar uma classe `Carro` e `Moto`.

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Avan%C3%A7ando%20em%20OOP/Ex1.py

---

Ex2= Adicione métodos específicos para `Carro` e `Moto` e demonstre polimorfismo entre eles.

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Avan%C3%A7ando%20em%20OOP/Ex2.py

---

Ex3: Encapsulamento e Herança Avançada
Crie uma classe ContaBancaria com atributos privados para saldo e numero_da_conta, e métodos públicos para depositar, sacar e consultar_saldo. Crie subclasses ContaCorrente e ContaPoupanca que herdam de ContaBancaria. A ContaCorrente deve ter um limite de cheque especial, e a ContaPoupanca deve ter uma taxa de juros.

Detalhes do Exercício
Classe Base ContaBancaria:

Atributos privados: saldo e numero_da_conta.
Métodos públicos: depositar, sacar e consultar_saldo.
Subclasses:

ContaCorrente:
Atributo adicional: limite_cheque_especial.
Método para consultar o limite.

ContaPoupanca:
Atributo adicional: taxa_juros.
Método para aplicar juros ao saldo.
Demonstração:

Crie instâncias de ContaCorrente e ContaPoupanca.
Utilize métodos de ambas as contas para demonstrar polimorfismo.
Mostre como a encapsulação protege os dados privados.

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Avan%C3%A7ando%20em%20OOP/Ex3.py

---

Ex4: Sistema de Biblioteca
Crie uma classe Livro com atributos privados para título, autor e número de páginas. 
Crie uma subclasse LivroDigital com um atributo adicional para o tamanho do arquivo (em MB). Implemente métodos para exibir informações sobre os livros e para calcular o tempo estimado de leitura (considerando uma taxa de leitura de 1 página por minuto).

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Avan%C3%A7ando%20em%20OOP/Ex4.py

---

Ex5: Sistema de Veículos
Crie uma classe Veiculo com atributos privados para marca e modelo, e métodos públicos para exibir essas informações. 
Crie subclasses Carro e Motocicleta que herdam de Veiculo. 
A classe Carro deve ter um atributo adicional para o número de portas e a classe Motocicleta deve ter um atributo adicional para o tipo de guidão. 
Implemente métodos para exibir as informações completas dos veículos.

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Avan%C3%A7ando%20em%20OOP/Ex5.py

---

Ex6: Sistema de Empregados
Crie uma classe Empregado com atributos privados para nome e salário. 
Crie uma subclasse Gerente com um atributo adicional para o bônus anual. 
Crie outra subclasse Desenvolvedor com um atributo adicional para a linguagem de programação. 
Implemente métodos para calcular o salário total (considerando bônus para Gerente) e para exibir as informações dos empregados.

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Avan%C3%A7ando%20em%20OOP/Ex6.py

---

Ex7: Sistema de Reservas de Hotel
Crie uma classe Reserva com atributos privados para nome do hóspede e número do quarto. 
Crie uma subclasse ReservaSimples e outra subclasse ReservaLuxo. 
A ReservaSimples deve ter um atributo adicional para a duração da estadia, enquanto a ReservaLuxo deve ter um atributo adicional para o serviço de quarto incluído. Implemente métodos para exibir informações sobre a reserva e calcular o custo total.

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Avan%C3%A7ando%20em%20OOP/Ex7.py

---

Ex8: Sistema de Gestão de Produtos
Crie uma classe Produto com atributos privados para nome e preço. 
Crie uma subclasse ProdutoPerecivel com um atributo adicional para a data de validade e uma subclasse ProdutoEletronico com um atributo adicional para a garantia. 
Implemente métodos para exibir informações sobre os produtos e para calcular o preço com desconto.

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Avan%C3%A7ando%20em%20POO/Ex8.py

---
 
Ex9: Sistema de Transporte
Crie uma classe Transporte com atributos privados para tipo e capacidade. 
Crie uma subclasse TransporteTerrestre com um atributo adicional para o tipo de combustível e uma subclasse TransporteAereo com um atributo adicional para a altitude máxima. 
Implemente métodos para exibir informações sobre os transportes e calcular a autonomia.

- Link no GitHub: https://github.com/Paulinbakna/Python.Exercicios/blob/main/Avan%C3%A7ando%20em%20POO/Ex9.py

---

Ex10: Sistema de Funcionários de Escola
Crie uma classe Funcionario com atributos privados para nome e salário. 
Crie uma subclasse Professor com um atributo adicional para a disciplina ensinada e uma subclasse Administrador com um atributo adicional para o departamento. 
Implemente métodos para calcular o salário anual e para exibir as informações dos funcionários.

- Link no GitHub: 

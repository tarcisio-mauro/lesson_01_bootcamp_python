# 1) O programa deve começar solicitando ao usuário que insira seu nome.
nome_de_usuario = input("Digite o seu nome: ")


# 2) Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. 
# Considere que este valor pode ser um número decimal.
salario = float(input("Insira o valor do seu salário: "))


# 3) Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, 
# que também pode ser um número decimal.
porcentagem_bonus = float(input("Insira a porcentagem do seu bônus: "))

# 4) O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
CONSTANTE_BONUS = 1000
valor_bonus = float(CONSTANTE_BONUS + (salario*porcentagem_bonus))

# 5) Finalmente, o programa deve imprimir uma mensagem no seguinte formato: 
# "Olá [nome], o seu valor bônus foi de 5000".
print(f"Olá {nome_de_usuario}, o seu valor bônus foi de {valor_bonus}")

# 6) Salve esse script python como kpi.py

# 7) Faça uma documentação simples de como executar esse programa, utilize o README

# 8) Salve no Git e no Github
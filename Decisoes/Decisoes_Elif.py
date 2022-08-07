nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa=input("O paciente possui doença infecciosa? (S/N): ").upper()
if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
elif doenca_infectocontagiosa == "Sim":
    print("O paciente " + nome + " deve ser encaminhado para sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO POSSUI atendimento prioritário e pode aguardar na sala comum!")

print("FIM DO PROGRAMA!")
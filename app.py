from translate import Translator

texto = input("O que você quer traduzir: ")

print("Opções de tradução: ")

print("1 - Inglês \n2 - Espanhol \n3 - Português")


def tradutor(texto, opcao):
    opcao = int(input("Qual a opção: "))

    if opcao == 1:
        lenguage = Translator(from_lang="autodetect", to_lang="english")
        traducao = lenguage.translate(texto)
        return traducao

    elif opcao == 2:
        lenguage = Translator(from_lang="autodetect", to_lang="spanish")
        traducao = lenguage.translate(texto)
        return traducao

    elif opcao == 3:
        lenguage = Translator(from_lang="autodetect", to_lang="portuguese")
        traducao = lenguage.translate(texto)
        return traducao

    else:
        print("Erro")


print()
traducao = tradutor(texto, 1)
print()
print(f"Frase para traduzir: {texto}")
print(f"Frase traduzida: {traducao}")

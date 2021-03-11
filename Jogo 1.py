#palavra = input('Escolha uma palavra: ')
palavra = "Yoga"
letra_digitadas =[]
chances = 5

while True:
    palavra_min = palavra.lower()
    letra = input("Escolha uma letra: ")
    letra_min = letra.lower()

    if len(letra) > 1:
        print("Escolha apenas uma letra!!!")
        continue

    letra_digitadas.append(letra_min)

    if letra_min in palavra_min:
        print(f'Parabens você acertou a {letra} letra da palavra secreta.')
    else:
        print(f'Infelizmente essa {letra} letra não tem na palavra secreta')
        letra_digitadas.pop()


    palavra_temp = ''
    for letra_secreta in palavra_min:
        if letra_secreta in letra_digitadas:
            palavra_temp += letra_secreta
        else:
            palavra_temp += '*'
    if palavra_temp == palavra_min:
        print(f'Parabéns você ganhou, a palavra era {palavra}')
        break
    else:
        print(f' A palavra esta assim: {palavra_temp}')



    if letra_min not in palavra_min:
        chances = chances - 1
        print(f"Você tem {chances} chances")
        if chances < 1:
            print(f"Infelizmente você perdeu, a palavra era {palavra}")
            break
    else:
        print(f"Você tem {chances} chances sobrando.")



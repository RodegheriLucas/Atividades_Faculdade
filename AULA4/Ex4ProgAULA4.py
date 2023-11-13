sis = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0}
loop = True
while loop:
    opt = int(input(f'1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\nQual o melhor Sistema Operacional para uso em servidores?: '))
    if opt>6 or opt<=0:
        print('Opção inválida.')
        loop = True 
    else:
        pass
        sis[str(opt)] += 1
    dnv = input('Deseja repetir?(s/n): ').lower()
    if dnv == 's':
        loop = True
    else:
        loop = False
        print(f'As preferências são\nWindows Server: {sis["1"]}\nUnix: {sis["2"]}\nLinux: {sis["3"]}\nNetware: {sis["4"]}\nMac OS: {sis["5"]}\nOutro: {sis["6"]}')      
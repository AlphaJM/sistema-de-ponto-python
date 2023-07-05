print('Bem vindo ao sistema de ponto da empresa Thunder!')

nome = str(input('Digite seu nome:'))

try:
    int(nome)
    print('Isso não é um nome!')
except:
    print('Ponto registrado em nome de: ', nome)

nome = str(input('Digite o nome completo: ')).strip()
mi = nome.lower()
ma = nome.upper()
jun = nome.split()
div = jun[0]
jc = nome.replace(' ', '')
cont = jc.__len__()
print('O nome com todas as letras minusculas é: {}'.format(mi))
print('O nome com todas as letras maiusculas é: {}'.format(ma))
print('O primeiro nome tem: {} letras'.format(div.__len__()))
print('O nome tem {} letras'.format(cont))


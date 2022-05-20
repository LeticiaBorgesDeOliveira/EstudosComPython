# Função média entre 5 notas/5 valores

def media():
    x = 0
    ac = 0
    while x < 5:
      num = int(input('digite o numero: '))
      x += 1
      ac += num
      media = ac / x
    return media
print(media())
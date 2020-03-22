def es_primo(num, aux):
    if aux == 1:
        return True
    elif num % aux == 0:
        return False
    else:
        return es_primo(num, aux-1)


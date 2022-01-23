# Trabalho 2 – Loja de Produtos Esportivos
# Disciplina: Redes
# David de Moura Marques
# 20172bsi0505
# 23/01/2022

def GetTypeOfInput(input):
    try:
        # Convert it into integer
        val = int(input)
        return 'int'
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return 'float'
        except ValueError:
            return 'str'
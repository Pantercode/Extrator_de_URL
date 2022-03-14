endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio da Ostras, Rj,  23440-120"

import re # Regula Expression -- RegEx

# 5 digitos + hifén (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #match
if busca:
    cep = busca.group()
    print(cep)

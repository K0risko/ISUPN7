#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nóbrega
#
# Created:     19/07/2023
# Copyright:   (c) Nóbrega 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas as pd

def buscar_codigo_sip(tabela, codigo_isup):
    # Procura o código SIP correspondente ao código ISUP fornecido
    filtro = tabela['Codigo_ISUP'] == codigo_isup
    resultado = tabela.loc[filtro, 'Codigo_SIP'].values
    return resultado[0] if resultado else None

def buscar_descricao(tabela, codigo):
    # Procura a descrição correspondente ao código SIP ou ISUP fornecido
    filtro = (tabela['Codigo_SIP'] == codigo) | (tabela['Codigo_ISUP'] == codigo)
    resultado = tabela.loc[filtro, 'Descricao'].values
    return resultado[0] if resultado else None

def main():
    # Exemplo de uso
    dados = {
        'Codigo_SIP': [100, 200, 300, 400],
        'Codigo_ISUP': [10, 20, 30, 40],
        'Descricao': ['Descrição 1', 'Descrição 2', 'Descrição 3', 'Descrição 4']
    }

    # Criando a tabela utilizando pandas DataFrame
    tabela = pd.DataFrame(dados)

    # Testando as funções de busca
    codigo_isup = 20
    codigo_sip = buscar_codigo_sip(tabela, codigo_isup)
    descricao = buscar_descricao(tabela, codigo_sip)

    print(f"Código SIP correspondente ao Código ISUP {codigo_isup}: {codigo_sip}")
    print(f"Descrição correspondente ao Código SIP {codigo_sip}: {descricao}")

if __name__ == "__main__":
    main()

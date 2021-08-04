def multiplica_iguais(m1, m2):
    produto, p_linha, m2_coluna, m2_linha = [], 0, 0, 0
    
    for linha_m1 in m1:
        produto.append([])
        for coluna_m1 in linha_m1:
            produto[p_linha].append(coluna_m1 * m2[m2_linha][m2_coluna])
            m2_coluna += 1
        m2_coluna = 0
        m2_linha += 1
        p_linha += 1

    return produto
def transpor_matriz(m):
    n_linhas = len(m)
    n_colunas = len(m[0])
    m_transposta = []
    
    for i in range(n_colunas):
        m_transposta.append([])
        for j in range(n_linhas):
            m_transposta[i].append(m[j][i])
        
    return m_transposta

m1 = [[1,2,3], [4,5,6], [7,8,9]]
print(m1)
print(transpor_matriz(m1))
m2 = [[1,2,3,4,5,6,7,8,9]]
print(m2)
print(transpor_matriz(m2))

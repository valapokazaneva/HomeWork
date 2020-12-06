def matrix_diag_summ(matrix, main=True):
    l=len(matrix)
    for i in matrix:
        if len(i)!=l:
            raise ValueError
    diag_summ=0
    if main:
        for i, e in enumerate(matrix):
            diag_summ+=e[i]
    else:
        for i, e in enumerate(matrix):
            diag_summ+=e[-(i+1)]
    return diag_summ
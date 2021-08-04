def sao_multiplicaveis(m1, m2):
    if len(m1[0]) == len(m2):
       return True
    else:
        return False
    
if __name__ == "__main__":
    import sys
    sao_multiplicaveis(int(sys.argv[1]))
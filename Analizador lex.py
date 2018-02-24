


reservadas =['if','else', 'while', 'def', 'for', 'break', 'return', 'print', 'import','\tif', '\telse', '\twhile', '\tdef', '\tfor', '\tbreak', '\treturn', '\tprint', 'import']
operadores = ['+', '_', '>', '==', '!=', '*', '/']
delimitadores = [':', '(', ')', '\t', '\n']


arquivo = open('codigo.txt', 'r')
cod = arquivo.read()
linhas = cod.split('\n')
linhas_arq = len(linhas)
        
    



def verificaToken(codigo, linha):
    saida = open('saida.txt','w')
    for pl in codigo: 
        if(pl != '\n' or '\t'):
            if pl.isdigit():
                print('Numero: "'+pl + '" linha: '+ str(linha)+'\n')
                saida.write('Numero: '+pl + ' linha: '+ str(linha)+'\n')
                
            for res in reservadas:
                if pl == res:
                   print('Palavra reservada: "'+pl+'" linha: '+  str(linha)+'\n' )
                   saida.write('Palavra reservada: '+ pl+' linha: '+  str(linha)+'\n' )
            for op in operadores:
                if pl == op:
                   print('Operador: "'+pl+ '" linha: '+  str(linha)+ '\n')
                   saida.write('Operador: '+pl+ ' linha: '+  str(linha)+ '\n')
            for deli in delimitadores:
                if pl == deli:
                   print('Delimitador: "'+pl+ '" linha: '+  str(linha)+'\n')
                   saida.write('Delimitador: "'+pl+ '" linha: '+  str(linha)+'\n')
        
        else:
            linha_atual +=1

    return 
        

def contarLinha(linha_cod):
    num_linha =1
    for li in  linha_cod:
        #print(linha_cod)
        #print(num_linha)
        string = ''.join(li)
        palavra_codigo = string.split(' ')
        verificaToken(palavra_codigo, num_linha)
        num_linha +=1
    arquivo.close()

contarLinha(linhas)

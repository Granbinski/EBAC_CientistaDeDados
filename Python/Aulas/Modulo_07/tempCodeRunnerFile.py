from arquivo_csv import ArquivoCSV
arquivo_banco = ArquivoCSV(arquivo='./banco.csv')

education = arquivo_banco.extrair_coluna(indice_coluna=3)
print(education)

arquivo_banco = ArquivoCSV(arquivo='./banco.csv')
education = arquivo_banco.extrair_coluna(indice_coluna=3)
print(education)

arquivo_banco_modulo = ArquivoCSV(arquivo='./banco.csv')
education = arquivo_banco_modulo.extrair_coluna(indice_coluna=3)
print(education)
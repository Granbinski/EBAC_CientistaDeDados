from arquivo.arquivo_csv import ArquivoCSV
arquivo_banco = ArquivoCSV(arquivo='Python/Aulas/Modulo_07/banco.csv')

education = arquivo_banco.extrair_coluna(indice_coluna=3)
print(education)

arquivo_banco = ArquivoCSV(arquivo='Python/Aulas/Modulo_07/banco.csv')
education = arquivo_banco.extrair_coluna(indice_coluna=3)
print(education)

arquivo_banco_modulo = ArquivoCSV(arquivo='Python/Aulas/Modulo_07/banco.csv')
education = arquivo_banco_modulo.extrair_coluna(indice_coluna=3)
print(education)

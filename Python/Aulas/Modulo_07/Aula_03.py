from arquivo.arquivo_csv import ArquivoCSV
from arquivo.arquivo_txt import ArquivoTXT


arquivo_banco_pacote = ArquivoCSV(arquivo=r'Python\Aulas\Modulo_07\banco.csv')
arquivo_noticia_pacote = ArquivoTXT(
    arquivo=r'Python\Aulas\Modulo_07\noticia.csv')

education = arquivo_banco_pacote.extrair_coluna(indice_coluna=3)
print(education)

titulo = arquivo_noticia_pacote.extrair_linha(numero_linha=1)
print(titulo)

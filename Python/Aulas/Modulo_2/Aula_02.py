hashtags_seg = ['#tiago', '#joao', '#bbb']
hashtags_ter = ['#sarah', '#bbb', '#fiuk']
hashtags_qua = ['#gil', '#thelma', '#lourdes']
hashtags_qui = ['#rafa', '#fora', '#danilo']
hashtags_sex = ['#juliete', '#arthur', '#bbb']


hashtags_semana = hashtags_seg + \
    hashtags_ter + \
    hashtags_qua + \
    hashtags_qui + \
    hashtags_sex
print(hashtags_semana)

frutas = {'banana', 'maca', 'uva', 'uva'}
print(frutas)
print(type(frutas))

norte_europa = {'reino unido', 'suecia', 'russia', 'noruega', 'dinamarca'}
escandinavia = {'noruega', 'dinamarca', 'suecia'}


norte_europa_nao_escandivano = norte_europa - escandinavia
print(norte_europa_nao_escandivano)

escandivano_nao_norte_europa = escandinavia - norte_europa
print(escandivano_nao_norte_europa)

cursos = {'Exatas', 'Humanas', 'Biológicas'}
print(cursos)

# inserir um elemento no conjunto: set.add(val)
cursos.add('Saúde')
print(cursos)

# remover um elemento no conjunto: set.remove(val)
cursos.remove('Saúde')
print(cursos)

times_paulistas = {'São Paulo', 'Palmeiras', 'Corinthians', 'Santos'}
print(times_paulistas)
print(type(times_paulistas))

print(list(times_paulistas))
print(type(list(times_paulistas)))

print(hashtags_semana)
print(len(hashtags_semana))

hashtags_semana = list(
    set(
        hashtags_seg +
        hashtags_ter +
        hashtags_qua +
        hashtags_qui +
        hashtags_sex
    )
)
print(hashtags_semana)
print(len(hashtags_semana))

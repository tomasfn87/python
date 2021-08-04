def main():

    print('\t1) Format method: ')

    print('\n\t1.1)')
    print('\tdecimal case precision:')
    print('\n{0:.1f}'.format(50/3))
    print('{0:.2f}'.format(50/6))
    print('{0:.3f}'.format(50/7))
    print('{0:.4f}'.format(17/3))
    print('{0:.5f}'.format(50/420))

    print('\n\t1.2)')
    print('\tfill with underscores:')
    print('\n{0:_^66}'.format('J\'aime bien le {lingua}'.format(lingua='français')))
    print('{0:_^66}'.format('Jag tycker om {lingua}'.format(lingua='svenska')))
    print('{0:_^66}'.format('On apprend toujours des nouvelles choses'))
    print('{0:_^66}'.format('Vi lär oss alltid något annat'))

    print('\n{0:_^66}'.format('English is good for coding!'))
    print('{0:_^66}'.format('It\'s very useful. It\'s maybe even a condition for deep-learning.'))

    print('\n{0:_^66}'.format('Allez, {nome}!'.format(nome='mon frère')))
    print('{0:_^66}'.format('Je vous en prie, {tempo0}!'.format(tempo0='à bientôt')))
    print('{0:_^66}'.format('Nous nous verons {tempo1}.'.format(tempo1='la semaine prochaine')))

    print('\n\t1.3)')
    print('\tkey-word based:')
    print('\n{name} wrote {book}'.format(name='Albert Camus', book='The Plague'))

    print('\n\t2)')
    print('\tspecify end:')
    print("\nI want to print in the ", end='')
    print("same line, but the code has two lines. \'code filename.ext\'")

    print('\nCamila linda!!!! Je t\'aime!')
main()
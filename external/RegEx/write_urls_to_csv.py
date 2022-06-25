import sys

data = [
    "url.parse('alqaeda.ak47.gun.shop')",
    'a.aa',
    '1123.123',
    'bobmartin.com',
    '&~.ll',
    'a1.aa',
    '1a.11',
    'a1.11',
    'b2.b1',
    '1.123',
    'bobmartin.co.uk',
    'www.example.com',
    'example.com',
    'help.example.com',
    '-&.aa',
    '{subsite.site.com.br/produtos}',
    '"example.net"',
    'aa.aa',
    '(http:/www.example12.net)',
    'https:\contact.example55.net',
    'store.steampowered.com',
    'buy.some-thing.for.me',
    "'gmail.com'",
    'www.saopaulo.sp.gov.br',
    '[bit.ly/1asd7a6]',
    'https://stackoverflow.com/questions/47637545/domain-names-that-start-with-a-number',
    'https://auth.udacity.com/sign-in?next=https%3A%2F%2Fclassroom.udacity.com%2Fauthenticated',
    'https://www.postgresql.org/docs/9.1/sql-altertable.html',
    'Digita duckduckgo.com no Safari e procura o nome da loja.',
    'O endereço completo é https://www.mozilla.org', 
    'D:\photo.png',
    'Ou só mozilla.org já dá certo',
    r'C:\User\Documents\outlook.com',
    'A loja está aberta. Eu não sei o que tem pra vender hoje.',
    'google .com',
    'google ponto con',
    'Entra no gugol',
    'A promoção é válida até sexta-feira 14/02 até as 23h39.',
    'https://onlinegdb.com/5hoybMfGy',
    '/usr/local/google.com\\',
    'google.com/usr/local/',
    r'htp:\\\\onlinegdb.com\5hoybMfG/',
    'https://www.w3schools.com/python/trypython.asp?filename=demo_regex',
    'https://idpcafe.usp.br/idp/profile/SAML2/Redirect/SSO?execution=e1s1#inbox',
    'https://mail.google.com/mail/u/0/?zx=ley03zxch2dl#inbox',
    'https://www.mercadolivre.com.br/c/calcados-roupas-e-bolsas#DEAL_ID=MLB9079&S=landingHubfashion-trends-jun&V=0&T=MainSliderItem-normal&L=FT_20.06_TENDENCIAS_INVERNO&deal_print_id=bbf80ce0-f41c-11ec-a285-b5055f67c13a&c_id=mainslideritem-normal&c_element_order=1&c_campaign=FT_20.06_TENDENCIAS_INVERNO&c_uid=bbf80ce0-f41c-11ec-a285-b5055f67c13a',
]

if __name__ == '__main__':
    inputs = sys.argv
    if len(inputs) > 1:
        output_file = sys.argv[1]

        with open(output_file, 'w') as fh:
            for i in data:
                fh.write(f'{i}\n')

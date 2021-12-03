def parse_cookie(cookie: str) -> dict:
    cookie = cookie.strip(';')
    if cookie == '':
        return {}
    name_values_dict = dict(pair.split('=', maxsplit=1) for pair in cookie.split(';'))
    return name_values_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('devicePixelRatio=1;ident=exists;__utma=13103r6942.2918;') == \
           {'devicePixelRatio': '1', 'ident': 'exists', '__utma': '13103r6942.2918'}
    assert parse_cookie('__utmc=13103656942;__utmz=13105942.1.1.1;utmcsr=google') == \
           {'__utmc': '13103656942', '__utmz': '13105942.1.1.1', 'utmcsr': 'google'}
    assert parse_cookie('utmccn=(organic);utmctr=(not%20provided);mp=3cb27825a6612988r46d00tinct') == \
           {'utmccn': '(organic)', 'utmctr': '(not%20provided)', 'mp': '3cb27825a6612988r46d00tinct'}
    assert parse_cookie('name=bijaya;comment=Comment1;expires=Mon, 26-Jul-2021 06:34:02 GMT;') == \
           {'name': 'bijaya', 'comment': 'Comment1', 'expires': 'Mon, 26-Jul-2021 06:34:02 GMT'}
    assert parse_cookie('ckpf_ppid_safari=a271b829cc244d5c94faae14f73f34df;') == \
           {'ckpf_ppid_safari': 'a271b829cc244d5c94faae14f73f34df'}
    assert parse_cookie('_cb_ls=1;ckns_privacy=july2019') == {'_cb_ls': '1', 'ckns_privacy': 'july2019'}
    assert parse_cookie('ckns_sa_labels_persist={};ckpf_ppid=7b5b127c65d24d939298eb61b7b9a08f;') == \
           {'ckns_sa_labels_persist': '{}', 'ckpf_ppid': '7b5b127c65d24d939298eb61b7b9a08f'}
    assert parse_cookie('yummy_cookie=choco;tasty_cookie=strawberry') == \
           {'yummy_cookie': 'choco', 'tasty_cookie': 'strawberry'}
    assert parse_cookie('id=a3fWa;Expires=Wed, 21 Oct 2015 07:28:00 GMT;') == \
           {'id': 'a3fWa', 'Expires': 'Wed, 21 Oct 2015 07:28:00 GMT'}
    assert parse_cookie('name=Nicholas;domain=nczonline.net') == {'name': 'Nicholas', 'domain': 'nczonline.net'}


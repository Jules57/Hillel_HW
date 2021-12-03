def parse(url: str) -> dict:
    if '?' in url:
        page, query = url.split('?')
        query = query.strip('&')
        if query == '':
            return {}
        name_values_dict = dict(pair.split('=') for pair in query.split('&'))
        return name_values_dict
    else:
        return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('https://www.domain.com/?utm_source=newsletter&utm_medium=email') == {'utm_source': 'newsletter',
           'utm_medium': 'email'}
    assert parse('https://www.domain.com/?utm_source=twitter&utm_medium=tweet&utm_campaign=summer-sale') == \
           {'utm_source': 'twitter', 'utm_medium': 'tweet', 'utm_campaign': 'summer-sale'}
    assert parse('www.go.clickmeter.com/38w2?id=123') == {'id': '123'}
    assert parse('https://stackoverflow.com/search?q=urls&s=5b3f0605-db5b-4f98-b815-85283c748575') == \
           {'q': 'urls', 's': '5b3f0605-db5b-4f98-b815-85283c748575'}
    assert parse('https://stackoverflow.com/questions/tagged/python-3.10?tab=Active') == {'tab': 'Active'}
    assert parse('https://www.youtube.com/watch?v=WIUrrp5KkCo') == {'v': 'WIUrrp5KkCo'}
    assert parse('https://medium.com/about?autoplay=1') == {'autoplay': '1'}
    assert parse('https://www.facebook.com/groups/search/groups_home/?q=urls') == {'q': 'urls'}
    assert parse('www.mediawiki.org/w/index.php?title=Project:Sandbox&action=delete') == \
           {'title': 'Project:Sandbox', 'action': 'delete'}
    assert parse('https://www.youtube.com/results?search_query=cat+hiccups+and+then+farts') == \
           {'search_query': 'cat+hiccups+and+then+farts'}
    assert parse('https://www.google.com') == {}

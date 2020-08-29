from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.soundcloud.com/users/soundcloud:users:4691639/sounds.rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Podcasts71/v4/ab/af/fd/abaffd6e-a4d1-5922-967c-338c8e67cf62/mza_2397885571294571131.jpg/313x0w.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Podcasts71/v4/ab/af/fd/abaffd6e-a4d1-5922-967c-338c8e67cf62/mza_2397885571294571131.jpg/313x0w.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()

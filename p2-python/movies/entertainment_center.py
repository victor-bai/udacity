import media
import fresh_tomatoes

#create some movie instances
underworld = media.Movie('Underworld:Awakening',
                         'The war between vampire and werewolf',
                        'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1506679373789&di=5960c252044e6d7093244023634970e4&imgtype=0&src=http%3A%2F%2Fimg5.cache.netease.com%2Fent%2F2012%2F5%2F11%2F201205111137269e33f.jpg',
                        'https://www.youtube.com/watch?v=rzRQwjlecFE')

blade_trinity = media.Movie('Blade Trinity',
                     'A vampire hunter',
                     'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=930861679,3970273730&fm=27&gp=0.jpg',
                     'https://www.youtube.com/watch?v=6vpqAwYj2Ks')

van_helsing = media.Movie('Van Helsing',
                          'A vampire hunter',
                     'https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=884c6401cd1349546a13e0363727f93d/f9dcd100baa1cd11a418aea0bf12c8fcc2ce2d80.jpg',
                     'https://www.youtube.com/watch?v=7pBmXkyycWE')

x_man = media.Movie('X-Man',
                    'Power\'s war',
                     'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1506680665901&di=1c0868f1079ed4903dae864980d3f8ee&imgtype=0&src=http%3A%2F%2Fimg0.cache.hxsd.com%2Fnews%2F2011%2F08%2F24%2F250Q620JL.jpg',
                     'https://www.youtube.com/watch?v=nbNcULQFojc')

midnight_in_paris = media.Movie('Midnight in Paris',
                     'Going back is time to meet authors',
                     'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1506601186309&di=75ddb2a61d49b69fa0afc4a949d5a138&imgtype=0&src=http%3A%2F%2Fi-7.vcimg.com%2Fd8e61a3297f35da68423892ce41b7f8b223197%2Forigin.jpg',
                     'https://www.youtube.com/watch?v=FAfR8omt-CY')

hunger_games = media.Movie('Hunger Games',
                     'A really real reality show',
                     'http://img.eaymusic.com/forum/201411/14/151947pny4lltalvel20l8.jpg',
                     'https://www.youtube.com/watch?v=mfmrPu43DF8')

movies = [underworld, blade_trinity, van_helsing, x_man, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)# generate web pages

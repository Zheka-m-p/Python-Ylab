from heroes import ChuckNorris, Superman, SuperHero
from news import CreatorNews
from places import Place, Kostroma, Tokyo
from random import choice


def save_the_place(hero: SuperHero, place: Place):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()

    news = CreatorNews(hero, place)
    make_news = choice([news.create_newspaper, news.create_tv_news])
    make_news()


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo())

from django.core.management import BaseCommand

from reviews.models import Genre

from ._load_data import _load_data


def row_saver_func(row: dict) -> None:
    obj = Genre(**row)
    obj.save()


def _load_genres_data():
    _load_data(
        data_model=Genre,
        data_name='genre',
        row_saver_func=row_saver_func
    )


class Command(BaseCommand):
    help = 'Loads data from genre.csv'

    def handle(self, *args, **options):
        _load_genres_data()

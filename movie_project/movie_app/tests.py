from django.test import TestCase
from django.urls import reverse
from .models import Movie
# Create your tests here.


class MovieModelTestCase(TestCase):


    @staticmethod
    def print_info(message):
        count = Movie.objects.count()
        print(f"{message}: all_movies={count}")


    def setUp(self):
        print('-' * 20)
        self.print_info('Start setUp')
        self.movie = Movie.objects.create(name='Test Movie', rating=80, year=2022)
        Movie.objects.create(name='Test Matrix', rating=90, year=2021)
        Movie.objects.create(name='Mask', rating=50, year=1995)
        self.print_info('Finish setUp')


    def test_movie_creation(self):
        """Проверка создания класса Movie"""
        self.print_info('Start test_movie_creation')
        self.assertEqual(self.movie.name, 'Test Movie')
        self.assertEqual(self.movie.rating, 80)
        self.assertEqual(self.movie.year, 2022)
        self.assertEqual(self.movie.budget, 1000000)
        self.assertEqual(self.movie.slug, 'test-movie')
        self.print_info('Finish test_movie_creation')


    def test_movie_get_all_records(self):
        """Проверка получения всех записей из БД"""
        self.print_info('Start test_movie_creation')
        movies = Movie.objects.all()
        self.assertEqual(len(movies), 3)
        self.print_info('Finish test_movie_creation')



    def test_movie_get_url(self):
        """Проверка метода get_url()"""
        self.print_info('Start test_movie_creation')
        url = self.movie.get_url()
        expected_url = reverse('details-movie', args=['test-movie'])
        self.assertEqual(url, expected_url)
        self.print_info('Finish test_movie_creation')


    def test_movie_str(self):
        """Проверка метода __str__()"""
        self.print_info('Start test_movie_creation')
        expected_str = 'Test Movie - 80'
        self.assertEqual(str(self.movie), expected_str)
        self.print_info('Finish test_movie_creation')


    def test_movie_save_slug(self):
        """Проверка сохранение slug при сохранении объекта"""
        self.print_info('Start test_movie_creation')
        self.assertEqual(self.movie.slug, 'test-movie')
        self.print_info('Finish test_movie_creation')


    def test_movie_budget_default_value(self):
        """Проверка значения по умолчанию для budget"""
        self.print_info('Start test_movie_creation')
        self.assertEqual(self.movie.budget, 1000000)
        self.print_info('Finish test_movie_creation')


import pytest


@pytest.fixture(params=[
    ('Дюна', 'Фантастика'),
    ('Как приручить дракона', 'Мультфильмы'),
    ('Солярис', 'Фантастика'),
    ('Убийство на улице Морг', 'Детективы')
])
def book_and_genre(request):
    return request.param

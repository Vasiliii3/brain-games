install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

barin-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

build:
	poetry build
# сборка проекта
publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
# распаковка
uninstall:
	pip uninstall hexlet_code -y
# удаление
lint:
	poetry run flake8 brain_games
# проверка файлов на стандарт PEP8
selfcheck:
	poetry check

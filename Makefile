install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even


build:
	poetry build
# сборка проекта
publish:
	poetry publish --dry-run
# тестовая публикация в папку dist
package-install:
	python -m pip install dist/*.whl
# распаковка
uninstall:
	pip uninstall python-project-lvl1
# удаление
lint:
	poetry run flake8 brain_games
# проверка файлов на стандарт PEP8
selfcheck:
	poetry check

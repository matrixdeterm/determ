from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="determ",
    version="0.0.2",
    author="Karina",
    author_email="protasova_karina@mail.ru",
    description="Создание библиотеки matrixdeterm",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/matrixdeterm/determ/",
    packages=find_packages(),
    keywords=['sis'],
    install_requires=requirements
)
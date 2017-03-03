from distutils.core import setup

def get_readme_text():
    with open('README.rst') as f:
        return f.read()

setup(
    name = 'pyrogi',
    packages = find_packages(),
    install_requires = ['pygame'],
    version = '0.1.0',
    description = 'A feature-rich roguelike game engine focused on ease of development and beauty through text graphics.',
    long_description = get_readme_text(),
    license = 'GPLv3',
    author = 'Ben Weedon',
    author_email = 'ben.weedon@outlook.com',
    url = 'https://github.com/BenWeedon/pyrogi',
    download_url = 'https://github.com/BenWeedon/pyrogi/releases/download/v0.1.0/pyrogi-0.1.0.tar.gz',
    keywords = ['game', 'engine', 'game-engine', 'roguelike', 'ascii'],
    classifiers = [],
)

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='dubeolsik-automata',
    version='0.1.0',
    author='Jihoon Kim, Seongyeop Yi',
    author_email='kimjihoon6188@daum.net',
    description='Dubeolsik automata',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kjh618/dubeolsik-automata',
    download_url='https://github.com/kjh618/dubeolsik-automata/archive/v0.1.0.tar.gz',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

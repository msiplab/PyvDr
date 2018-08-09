from setuptools import setup
import os

def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(
            map(str, version_tuple[:-1])
        ) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))

init = os.path.join(
    os.path.dirname(__file__), 'src', 'saivdr', '__init__.py'
)

def strip_comments(l):
    return l.split('#', 1)[0].strip()

def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
            os.path.join(os.getcwd(), *f)).readlines()]))

version_line = list(
    filter(lambda l: l.startswith('VERSION'), open(init))
)[0]

try:
    from pypandoc import convert
    def read_md(f):
        return convert(f, 'rst')
except ImportError:
    convert = None
    print(
        'warning: pypandocモジュールが見つからないため、MarkdownからRSTに変換できません'
    )
    def read_md(f):
        return open(f, 'r').read()

README = os.path.join(os.path.dirname(__file__), 'README.md')
VERSION = get_version(eval(version_line.split('=')[-1]))
setup(
    name='saivdr',
    version=VERSION,
    description='SaivDr package for Python',
    long_description=read_md(README),
    install_requires=reqs('requirements.txt')
)

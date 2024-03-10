from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="rango-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    long_description=open('README.md').read(),
    author='Nimara0x',
    author_email='nimcrypto12@gmail.com',
    url='https://github.com/Nimara0x/rango-sdk',
    python_requires='>=3.9',
)
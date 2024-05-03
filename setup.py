from setuptools import setup, find_packages

setup(
    name='trade_utils',
    version='0.1.0',
    author='Sunny Saxena',
    author_email='saxenasunny@hotmail.com',
    description='This is my custom trade utility and db connection module',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10'
)


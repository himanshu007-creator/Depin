from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Python package to utilize olinda depin services'
LONG_DESCRIPTION = 'Depin works on packaging functionality offered by brazilian central bank\'s service. For more information visit here https://bit.ly/3FJPiqe'

setup(
    name="depin",
    version=VERSION,
    author="Himanshu, Frank, Maylon",
    author_email="<addyjeridiq@email.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'bcb', 'olinda'],
    classifiers=[
        "Development Status :: 3 - beta",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

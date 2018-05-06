import sys
from setuptools import setup
import io

if sys.version_info[0] > 2:
    exec(open('PageObjectLibrary/version.py').read())
else:
    execfile('PageObjectLibrary/version.py')

setup(
    name             = 'robotframework-pageobjectlibrary',
    version          = __version__,
    author           = 'Bryan Oakley',
    author_email     = 'bryan.oakley@gmail.com',
    url              = 'https://github.com/boakley/robotframework-pageobjectlibrary/',
    keywords         = 'robotframework',
    license          = 'Apache License 2.0',
    description      = 'RobotFramework library that implements the Page Object pattern',
    long_description = io.open('README.md', encoding="utf-8").read(),
    long_description_content_type = "text/markdown",
    zip_safe         = True,
    include_package_data = True,
    install_requires = ['robotframework', 'selenium', 'six'],
    classifiers      = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Framework :: Robot Framework",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        "Intended Audience :: Developers",
        ],
    packages         =[
        'PageObjectLibrary',
    ],
    scripts          =[],
)

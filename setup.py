import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.txt")) as f:
    README = f.read()

requires = [
    "pyramid",
    "pyramid_jinja2",
    "waitress",
]

setup(
    name="portfolio",
    version="0.0",
    description="Personal educational portfolio",
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
    ],
    author="",
    author_email="",
    url="",
    keywords="web pyramid portfolio",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        "paste.app_factory": ["main = portfolio:main"],
    },
)

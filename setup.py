from setuptools import setup

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(name="Presser",
    version="0.1.1",
    packages=["presser",],
    license="GNU GPL v3.0",
    description="Extracts data from vine, in lieu of an API",
    author="Gemma Hentsch",
    author_email="contact@halfapenguin.com",
    requires=[
        "beautifulsoup4(>=4.3.2)",
        "requests(>=2.4.0)", 
        "mock(>=1.0.1)", 
        "coverage(>=3.7.1)", 
        "nose(>=1.3.4)", 
        # "nose-cover3(>=0.1.0)",
    ],
    long_description=long_description,
    test_suite="nose.collector",
)
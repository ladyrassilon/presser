from distutils.core import setup

setup(name="Presser",
    version="0.1",
    packages=["presser",],
    license="GNU GPL v3.0",
    description="Extracts data from vine, in lieu of an API",
    author="Gemma Hentsch",
    author_email="contact@halfapenguin.com",
    requires=["beautifulsoup4(>=4.3.2)","requests(>=2.4.0)"],
    long_description=open("README.txt").read(),
)
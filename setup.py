from setuptools import setup, find_packages

with open("README.md", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="cristiano",
    author_email="crisosilva88@gmail.com",
    description="",
    long_description="",
    install_requires=requirements,
    python_requires=">=3.8",
)

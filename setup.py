import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Py_Keyboard",
    version="0.0.2",
    author="Danny Dasilva",
    author_email="dannydasilva.solutions@gmail.com",
    description="Python wrapper for hid device on the pi zero w",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Danny-Dasilva/Py_Keyboard",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: Linux",
    ],
)

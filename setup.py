import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="entro_py_min",
    version="0.0.1",
    author="Conrad Großer",
    author_email="grosserconrad@gmail.com",
    description="Small Information Entropy Calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/creyD/entro.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

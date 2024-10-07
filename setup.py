from setuptools import setup, find_packages

setup(
    name="dna-barcodes",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    author="Jasper August Tootsi",
    author_email="jasper.august.tootsi@ut.ee",
    description="A package for generating unique DNA barcodes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JasperAugust/dna-barcodes",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

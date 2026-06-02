from setuptools import setup, find_packages

setup(
    name="astralnet",
    version="1.0.0",
    author="Dr. Noor Fatima",
    author_name="noorf",
    description="Advanced predictive stroke modeling and clinical radiomics data pipelining.",
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    python_requires='>=3.8',
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
    ],
)

from setuptools import setup, find_packages

setup(
    name="rebound-compare",
    version="0.1.0",
    author="Muzaffer Mahi Can",
    description="Compare REBOUND simulations side-by-side",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "rebound"
    ],
    license="MIT", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy"
    ],
    python_requires=">=3.7",
)

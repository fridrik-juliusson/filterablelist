from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="filterablelist",
    version="0.1.1",
    description="A list with built in filtering syntax.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fridrik-juliusson/filterablelist",
    author="Fridrik Juliusson",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="list, filter, development, utility",
    package_dir={"": "filterablelist"},
    py_modules=["filterablelist"],
    # packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    project_urls={
        'Documentation': 'https://github.com/fridrik-juliusson/filterablelist/',
        "Bug Reports": "https://github.com/fridrik-juliusson/filterablelist/issues",
        "Say Thanks!": "https://fridrikjuliusson.com/",
        "Source": "https://github.com/fridrik-juliusson/filterablelist/",
    },
)

from setuptools import setup, find_packages
from pathlib    import Path

base_dir     = Path(__file__).parent.resolve()
version_file = base_dir / "lib/lisless/__version__.py"
readme_file  = base_dir / "README.md"

# Eval the version file to get __version__; avoids importing our own package
with version_file.open() as f:
    exec(f.read())

# Get the long description from the README file
with readme_file.open(encoding = "utf-8") as f:
    long_description = f.read()

setup(
    name = "lisless",
    version = __version__,

    packages = find_packages("lib"),
    package_dir = {"": "lib"},

    description = "A LIS that does less, for the LIS-less.",
    long_description = long_description,
    long_description_content_type = "text/markdown",

    url = "https://github.com/seattleflu/lisless",
    project_urls = {
        "Bug Reports": "https://github.com/seattleflu/lisless/issues",
        "Source":      "https://github.com/seattleflu/lisless",
    },

    classifiers = [
        "Development Status :: 2 - Pre-Alpha",

        # This is a CLI
        "Environment :: Console",
        "Environment :: Web Environment",

        # This is for bioinformatic software devs and researchers
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps",

        # Python ≥ 3.8 only
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],

    python_requires = ">=3.8",

    install_requires = [
        "astm",
    ],

    entry_points = {
        "console_scripts": [
            "lisless = lisless.__main__:main",
        ],
    },
)

from setuptools import setup, find_packages


def get_description():
    return "Deep Learning library for colorizing and restoring old images and video"


# def get_long_description():
#     with open("README.md") as f:
#         return f.read()


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="BlushUp",
    version="0.0.1",
    packages=find_packages(exclude=["tests"]),
    license="MIT License",
    description=get_description(),
    # long_description=get_long_description(),
    # long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Jupyter",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=get_requirements(),
    python_requires=">=3.6",
)

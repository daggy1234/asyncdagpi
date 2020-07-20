from setuptools import find_packages, setup

setup(
    name="asyncdagpi",
    version="2.5.0",
    license="MIT",
    description="Asynchronous API wrapper for the Dagbot API (https://dagpi.tk)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Daggy1234/asyncdagpi",
    author="Daggy1234",
    packages=find_packages(),
    install_requires=["aiohttp"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

from setuptools import find_packages, setup
with open("README.md", "r") as f:
    long_description = f.read()
setup(
    name="asyncdagpi",
    packages=["asyncdagpi"],
    version="1.0.0",
    pacakges=find_packages(),
    license="MIT",
    description="Asynchronous API wrapper for the Dagbot API (http://dagpi.tk)",
    url="https://github.com/Daggy1234/asyncdagpi",
    download_url="https://github.com/Daggy1234/asyncdagpi/archive/1.1.0.tar.gz",
    author="Daggy1234",
    install_requires=["aiohttp"],
    long_description=long_description,
    long_description_content_type="text/markdown",
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

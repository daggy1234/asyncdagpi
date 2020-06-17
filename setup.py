from setuptools import find_packages, setup

setup(
    name="asyncdagpi",
    packages=["asyncdagpi"],
    version="1.0.0",
    pacakges=find_packages(),
    license="MIT",
    description="Asynchronous API wrapper for the Dagbot API (http://dagpi.tk)",
    url="https://github.com/Daggy1234/asyncdagpi",
    author="Daggy1234",
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

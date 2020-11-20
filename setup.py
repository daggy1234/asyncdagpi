from setuptools import find_packages, setup
import re

with open('asyncdagpi/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(
    name="asyncdagpi",
    version=version,
    license="MIT",
    description="Asynchronous API wrapper for the Dagpi https://dagpi.xyz",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/Daggy1234/asyncdagpi",
    project_urls={
        "Documentation": "https://asyncdagpi.rtfd.io",
        "Issue tracker": "https://github.com/Daggy1234/asyncdagpi/issues",
        "Website": "https://dagpi.xyz"
      },
    author="Daggy1234",
    packages=find_packages(),
    install_requires=["aiohttp"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Natural Language :: English',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
        ],
)
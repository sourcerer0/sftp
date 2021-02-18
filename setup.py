import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sftp",
    version="1.0.0-a.1",
    author="Lo Han",
    author_email="lohan.uchsa@protonmail.com",
    description="SFTP Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sourcerer0/sftp",
    packages=setuptools.find_packages(),
    keywords="sftp file network ssh",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.8',
    install_requires=[]
)
import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="qstat",
    version="0.0.5",
    description="Parse qstat xml to python dict",
    long_description=long_description,
    url="https://github.com/relleums/qstat/archive/0.0.5.tar.gz",
    author="Sebastian Achim Mueller",
    author_email="sebastian-achim.mueller@mpi-hd.mpg.de",
    license="GPLv3",
    packages=["qstat",],
    package_data={"qstat": ["tests/resources/*",]},
    install_requires=["xmltodict"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Clustering",
    ],
)

from setuptools import setup
setup(
    name='qstat',
    version='0.0.4',
    description='Parse qstat xml to python dict',
    url='https://github.com/relleums/qstat/archive/0.0.4.tar.gz',
    author='Sebastian Achim Mueller',
    author_email='sebmuell@phys.ethz.ch',
    license='GPLv3',
    packages=[
        'qstat',
    ],
    package_data={
        'qstat': [
            'tests/resources/*',
        ]
    },
    install_requires=[
        'xmltodict'
    ],
    keywords = ['qsub', 'qstat', 'grid engine', 'SGE', 'queue']
)

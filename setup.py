from distutils.core import setup

setup(
    name='qstat',
    version='0.0.0',
    description='Parse qstat xml to python dict',
    url='https://github.com/relleums/qstat',
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
    zip_safe=False,
)

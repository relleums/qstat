qstat for python |TravisBuildStatus| |PyPIStatus| |BlackStyle|
==============================================================

A python API for qstat
----------------------
The sungrid job submission framework known as ```qsub``` is a powerful tool to distribute your workload over many machines in parallel. To check the status of the jobs in the queue there is ```qstat``` which can print a human readable status table on the command line. Such status can be useful to keep track of your submitted compute jobs to e.g. prevent duplicate submission.

This python qstat wrapper parses the jobs listed in ```qstat -xml``` into a list of dictionaries.

Install with

.. code::

     $ pip install qstat

Usage
~~~~~
Get python dictionaries descibing your ```qsub``` jobs.

.. code:: python

    from qstat import qstat

    queue_info, job_info = qstat()

    queue_info[13]

.. code:: python

    {'@state': 'running',
     'JAT_prio': '0.55008',
     'JAT_start_time': '2017-09-04T16:22:50',
     'JB_job_number': '6384796',
     'JB_name': 'phs_obs_20120102_001',
     'JB_owner': 'relleums',
     'queue_name': 'test@isdc-cn11.astro.unige.ch',
     'slots': '1',
     'state': 'r'}

Add both ```queue_info``` and ```job_info``` to have one list of both running and waiting jobs:

.. code:: python

    from qstat import qstat

    queue_info, job_info = qstat()

    all_jobs = queue_info + job_info

    for job in all_jobs:
        print(job['JB_name'], 'is', job['@state'])

::

    my_job_001 is running
    my_job_002 is running
    my_job_003 is running


or combine with e.g. with pandas DataFrame

.. code:: python

    from qstat import qstat
    q, j = qstat()

    import pandas as pd
    df = pd.DataFrame(q + j)

    df.tail()

::

          @state JAT_prio JAT_start_time JB_job_number               JB_name  \
    190  pending  0.00000            NaN       6384973  phs_obs_20160102_002
    191  pending  0.00000            NaN       6384974  phs_obs_20160201_001
    192  pending  0.00000            NaN       6384975  phs_obs_20160201_002
    193  pending  0.00000            NaN       6384976  phs_obs_20160202_001
    194  pending  0.00000            NaN       6384977  phs_obs_20160202_002

         JB_owner   JB_submission_time queue_name slots state
    190  relleums  2017-09-04T16:22:51       None     1    qw
    191  relleums  2017-09-04T16:22:51       None     1    qw
    192  relleums  2017-09-04T16:22:51       None     1    qw
    193  relleums  2017-09-04T16:22:51       None     1    qw
    194  relleums  2017-09-04T16:22:51       None     1    qw


.. |TravisBuildStatus| image:: https://travis-ci.org/relleums/qstat.svg?branch=master
   :target: https://travis-ci.org/relleums/qstat

.. |PyPIStatus| image:: https://badge.fury.io/py/qstat.svg
   :target: https://pypi.python.org/pypi/qstat

.. |BlackStyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

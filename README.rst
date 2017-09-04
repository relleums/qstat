qstat for python |TravisBuildStatus| |PyPIStatus|
=================================================

A python API for qstat 
----------------------
The sungrid job submission framework known as ```qsub``` is a powerful tool to spread the workload of a task over many machines in parallel. To check the status of the jobs in the queue there is ```qstat``` which can print a human readable status table which can be useful to keep track of once submitted compute jobs. There is also a machine readable flavor exporting to ```xml```.

This python qstat package parses the jobs listed in ```qstat -xml``` into a list of dictionaries. 

Install with

.. code:: 

     $ pip install qstat

Usage
~~~~~

.. code:: python

    from qstat import qstat

    queue_info, job_info = qstat()
    

.. |TravisBuildStatus| image:: https://travis-ci.org/relleums/qstat.svg?branch=master
   :target: https://travis-ci.org/relleums/qstat
   
.. |PyPIStatus| image:: https://badge.fury.io/py/qstat.svg
   :target: https://pypi.python.org/pypi/qstat

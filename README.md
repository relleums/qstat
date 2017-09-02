# qstat 2 python dict [![Build Status](https://travis-ci.org/relleums/qstat2pydict.svg?branch=master)](https://travis-ci.org/relleums/qstat2pydict)

The sungrid job submission framework known as ```qsub``` is a powerful tool to spread the workload of a task over many machines in parallel. To check the status of the jobs in the queue there is ```qstat``` which can print a human readable status table which can be useful to keep track of once submitted compute jobs. There is also a machine readable flavor exporting to ```xml```.

This python qstat package parses the jobs listed in ```qstat -xml``` into a list of dictionaries. 

## Usage
```python
from qstat import qstat 

job_list = qstat()

job_list[13]
{'@state': 'running',
 'JAT_prio': 0.56,
 'JAT_start_time': '2017-09-02T02:06:19',
 'JB_job_number': 6177275,
 'JB_name': 'phs_obs_20120102_001',
 'JB_owner': 'relleums',
 'queue_name': 'test@isdc-cn23.astro.unige.ch',
 'slots': '1',
 'state': 'r'}

for job in job_list:
    if job['@state'] == 'running':
        print('Job '+str(job['JB_job_number'])+' is running for its life!')
Job 6177303 is running for its life!
Job 6177304 is running for its life!
Job 6177305 is running for its life!
Job 6177306 is running for its life!
Job 6177307 is running for its life!
Job 6177308 is running for its life!
Job 6177309 is running for its life!
Job 6177310 is running for its life!
...
```

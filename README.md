# qstat 2 python dict [![Build Status](https://travis-ci.org/relleums/qstat2pydict.svg?branch=master)](https://travis-ci.org/relleums/qstat2pydict)

The sungrid job submission framework known as ```qsub``` is a powerful tool to spread the workload of a task over many machines in parallel. To check the status of the jobs in the queue there is ```qstat``` which can print a human readable status table which can be useful to keep track of once submitted compute jobs. There is also a machine readable flavor exporting to ```xml```.

This python qstat package parses the jobs listed in ```qstat -xml``` into a list of dictionaries. 

## Usage
Get a list of qstat job info dicts:
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
```

Iterate thorugh job info list:
```python
from qstat import qstat 

job_list = qstat()

for job in job_list:
    if job['@state'] == 'running':
        print('Job '+str(job['JB_job_number'])+' is running for its life!')
"""
Job 6177303 is running for its life!
Job 6177304 is running for its life!
Job 6177305 is running for its life!
Job 6177306 is running for its life!
Job 6177307 is running for its life!
Job 6177308 is running for its life!
Job 6177309 is running for its life!
Job 6177310 is running for its life!
...
"""
```

Use a pandas DataFrame:
```python
from qstat import qstat
import pandas as pd

df = pd.DataFrame(qstat())

df.head()

"""
    @state  JAT_prio       JAT_start_time  JB_job_number  \
0  running      0.56  2017-09-02T02:03:12        5074985   
1  running      0.56  2017-09-02T02:03:45        5074992   
2  running      0.56  2017-09-02T02:02:13        5075009   
3  running      0.56  2017-09-02T02:06:19        6177265   
4  running      0.56  2017-09-02T02:06:19        6177266   

                         JB_name  JB_owner  \
0  fact_phs_muon_20150422_148.sh  relleums   
1  fact_phs_muon_20150422_160.sh  relleums   
2  fact_phs_muon_20150409_192.sh  relleums   
3           phs_obs_20110101_001  relleums   
4           phs_obs_20110101_002  relleums   

                           queue_name slots state  
0  fact_long@isdc-cn23.astro.unige.ch     1    dt  
1  fact_long@isdc-cn23.astro.unige.ch     1    dt  
2  fact_long@isdc-cn22.astro.unige.ch     1    dt  
3       test@isdc-cn23.astro.unige.ch     1     r  
4       test@isdc-cn23.astro.unige.ch     1     r 
"""

df.state == 'r'
"""
0     False
1     False
2     False
3      True
4      True
5      True
6      True
7      True
8      True
9      True
...
"""

# qstat 2 python dict [![Build Status](https://travis-ci.org/relleums/qstat2pydict.svg?branch=master)](https://travis-ci.org/relleums/qstat2pydict)

The sungrid job submission framework known as ```qsub``` is a powerful tool to spread the workload of a task over many machines in parallel. To check the status of the jobs in the queue there is ```qstat``` which can print a human readable status table which can be useful to keep track of once submitted compute jobs. There is also a machine readable flavor exporting to ```xml```.

This python qstat package parses the jobs listed in ```qstat -xml``` into a list of dictionaries. 

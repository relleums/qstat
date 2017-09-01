import subprocess as sp
import xmltodict
from datetime import datetime


def qstat(qstat_path='qstat', typed=True):
    xml = qstat2xml(qstat_path=qstat_path)
    if typed:
        return typed_job_infos(xml2job_infos(xml))
    else:
        return xml2job_infos(xml)


def qstat2xml(qstat_path='qstat'):
    """
    Returns a qstat xml string
    """
    try:
        out = sp.check_output([qstat_path, '-xml'], stderr=sp.STDOUT)
    except sp.CalledProcessError as e:
        print('qstat returncode:', e.returncode)
        print('qstat std output:', e.output)
        raise
    except FileNotFoundError as e:
        e.message = 'Maybe qstat is not installed.'
        raise
    return out


def xml2job_infos(qstatxml):
    """
    Takes qstat xml string and returns a list of dicts of 
    qsub job name and qsub job state 
    """
    x = xmltodict.parse(qstatxml)
    job_infos = []
    if x['job_info']['queue_info'] is not None:
        for job in x['job_info']['queue_info']['job_list']:
            job_infos.append(dict(job))
    if x['job_info']['job_info'] is not None:
        for job in x['job_info']['job_info']['job_list']:
            job_infos.append(dict(job))
    return job_infos


def typed_job_infos(job_infos):
    j = job_infos
    for i in range(len(j)):
        if 'JB_job_number' in j[i]:
            j[i]['JB_job_number'] = int(j[i]['JB_job_number'])
        if 'JAT_prio' in j[i]:
            j[i]['JAT_prio'] = float(j[i]['JAT_prio'])
        if 'JB_submission_time' in j[i]:
            j[i]['JB_submission_time'] = datetime.strptime(
                j[i]['JB_submission_time'], 
                '%Y-%m-%dT%H:%M:%S'
            )
    return j
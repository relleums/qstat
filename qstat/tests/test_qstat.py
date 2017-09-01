import qstat
import os
import pkg_resources
from datetime import datetime


qstat_example_xml_path = pkg_resources.resource_filename(
    'qstat', 
    os.path.join('tests','resources','qstat_example.xml')
)

qstat_xml_empty_queue_path = pkg_resources.resource_filename(
    'qstat', 
    os.path.join('tests','resources','qstat_empty_queue.xml')
)


def test_read_empty_qstat():
    with open(qstat_xml_empty_queue_path, 'rt') as fin:
        qstat_xml_empty_queue = fin.read()
    jobs = qstat._tools.xml2job_infos(qstat_xml_empty_queue)
    assert len(jobs) == 0


def test_read_empty_qstat_suitable_types():
    with open(qstat_xml_empty_queue_path, 'rt') as fin:
        qstat_xml_empty_queue = fin.read()
    jobs = qstat._tools.xml2job_infos(qstat_xml_empty_queue)
    sjobs = qstat._tools.typed_job_infos(jobs)
    assert len(sjobs) == 0


def test_jobs_in_qstatxml():
    with open(qstat_example_xml_path, 'rt') as fin:
        qstat_xml = fin.read()
    jobs = qstat._tools.xml2job_infos(qstat_xml)
    assert len(jobs) == 51


def test_jobs_in_qstatxml_suitable_types():
    with open(qstat_example_xml_path, 'rt') as fin:
        qstat_example_xml = fin.read()
    jobs = qstat._tools.xml2job_infos(qstat_example_xml)
    sjobs = qstat._tools.typed_job_infos(jobs)
    assert len(sjobs) == 51
    for job in sjobs:
        assert type(job['JB_job_number']) is int
        assert type(job['JAT_prio']) is float
        if 'JB_submission_time' in job:
            assert type(job['JB_submission_time']) is datetime


def test_qsat_not_installed_exception():
    path_which_most_certainly_does_not_exist = os.path.join(
        'dev','unicorn','rainbow','barf','minus-null'
    )
    try:
        qstat._tools.qstat2xml(
            qstat_path=path_which_most_certainly_does_not_exist
        )
    except FileNotFoundError as e:
        assert 'qstat is not installed' in e.message
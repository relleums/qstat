import qstat
import os
import pkg_resources
from datetime import datetime
import tempfile

qstat_example_xml_path = pkg_resources.resource_filename(
    'qstat', 
    os.path.join('tests','resources','qstat_example.xml')
)

qstat_xml_empty_queue_path = pkg_resources.resource_filename(
    'qstat', 
    os.path.join('tests','resources','qstat_empty_queue.xml')
)

qstat_length_one_xml_path = pkg_resources.resource_filename(
    'qstat', 
    os.path.join('tests','resources','qstat_length_one.xml')
)

def test_read_empty_qstat():
    with open(qstat_xml_empty_queue_path, 'rt') as fin:
        qstat_xml_empty_queue = fin.read()
    queue_info, job_info = qstat._tools.xml2queue_and_job_info(qstat_xml_empty_queue)
    assert len(queue_info) == 0
    assert len(job_info) == 0


def test_queue_and_job_info_in_qstatxml():
    with open(qstat_example_xml_path, 'rt') as fin:
        qstat_xml = fin.read()
    queue_info, job_info = qstat._tools.xml2queue_and_job_info(qstat_xml)
    assert len(queue_info + job_info) == 51
    assert len(queue_info) == 24
    assert len(job_info) == 27


def test_qsat_not_installed_exception():
    with tempfile.TemporaryDirectory(prefix='qstat_') as tmp:
        nap = os.path.join(tmp,'unicorn.barf')
        try:
            qstat._tools.qstat2xml(
                qstat_path=nap
            )
        except FileNotFoundError as e:
            assert 'Maybe "'+nap+' -xml" is not installed.' in e.message


def test_qsat_xml_oprion():
    with tempfile.TemporaryDirectory(prefix='qstat_') as tmp:
        nap = os.path.join(tmp,'unicorn.barf')
        xml_option = '-probably_not'
        try:
            qstat._tools.qstat2xml(
                qstat_path=nap,
                xml_option=xml_option
            )
        except FileNotFoundError as e:
            assert 'Maybe "'+nap+' '+xml_option+'" is not installed.' in e.message


def test_read_qstat_with_length_one():
    with open(qstat_length_one_xml_path, 'rt') as fin:
        qstat_xml = fin.read()
    queue_info, job_info = qstat._tools.xml2queue_and_job_info(qstat_xml)
    assert len(queue_info) == 0
    assert len(job_info) == 1

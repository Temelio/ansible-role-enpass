"""
Role tests
"""

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('name', [
    ('enpass'),
    ('libxss1'),
    ('lsof'),
])
def test_packages(host, name):
    """
    Test packages installed
    """

    assert host.package(name).is_installed


def test_repository_file(host):
    """
    Test repository file
    """

    repo_file = host.file('/etc/apt/sources.list.d/enpass.list')

    assert repo_file.exists
    assert repo_file.is_file
    assert repo_file.user == 'root'
    assert repo_file.group == 'root'
    assert repo_file.mode == 0o644

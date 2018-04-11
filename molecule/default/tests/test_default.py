"""
Runs Default tests
Available Modules: http://testinfra.readthedocs.io/en/latest/modules.html

"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sudoers_file(host):
    """
    Tests that the sudoers file was configured correctly
    """
    file = host.file('/etc/sudoers.d/ansible')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o440
    assert file.contains('Defaults:foo requiretty')
    assert file.contains('foo ALL=(ALL:ALL) NOPASSWD: /bin/ls')


def test_sudo_is_installed(host):
    """
    Tests that sudo is installed
    """
    sudo = host.package("sudo")
    assert sudo.is_installed

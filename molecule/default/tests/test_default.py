import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_service_running_and_enabled(host):
    assert not host.ansible(
            "service",
            "name=grafana-server enabled=true state=started")['changed']

def test_service_listens_on_ports(host):
    assert host.socket("tcp://0.0.0.0:3000").is_listening

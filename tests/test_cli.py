# -*- coding: utf-8 -*-
import subprocess

from shutil import rmtree


def run(command):
    return subprocess.run(command, capture_output=True, shell=True, text=True)


def test_generate():
    out = run('python logya/main.py gen --dir-site logya/sites/docs')
    assert 0 == out.returncode
    assert 'write pages' in out.stdout.lower()


def test_generate_wrong_dir():
    out = run('python logya/main.py gen --dir-site .')
    assert 1 == out.returncode
    assert 'error' in out.stderr.lower()


def test_create():
    out = run('python logya/main.py create test_create_site --dir-site tests/fixtures/')
    assert 0 == out.returncode
    assert 'site created' in out.stdout.lower()

    # Second time must fail
    out2 = run('python logya/main.py create test_create_site --dir-site tests/fixtures/')
    assert 1 == out2.returncode
    assert 'already exists' in out2.stderr.lower()

    # Cleanup
    rmtree('tests/fixtures/test_create_site')
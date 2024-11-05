import subprocess
from shutil import rmtree


def run(command):
    return subprocess.run(command, capture_output=True, shell=True, text=True, check=False)


def test_generate():
    out = run('python logya/main.py gen --dir-site logya/sites/docs')
    assert out.returncode == 0
    assert 'write pages' in out.stdout.lower()


def test_generate_wrong_dir():
    out = run('python logya/main.py gen --dir-site .')
    assert out.returncode == 1
    assert 'error' in out.stderr.lower()


def test_create():
    out = run('python logya/main.py create test_create_site --dir-site tests/fixtures/')
    assert out.returncode == 0
    assert 'site created' in out.stdout.lower()

    # Second time must fail
    out2 = run('python logya/main.py create test_create_site --dir-site tests/fixtures/')
    assert out2.returncode == 1
    assert 'already exists' in out2.stderr.lower()

    # Cleanup
    rmtree('tests/fixtures/test_create_site')

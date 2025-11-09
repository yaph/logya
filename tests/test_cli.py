import subprocess
from pathlib import Path
from shutil import rmtree


def run(command):
    return subprocess.run(command, capture_output=True, shell=True, text=True, check=False)


def test_clean():
    dir_site = 'logya/sites/docs'
    dir_test = Path(dir_site).joinpath('public', '_test_clean')
    dir_test.mkdir(exist_ok=True, parents=True)
    file_test = dir_test.joinpath('test.txt')
    file_test.write_text('TEST')
    out = run(f'logya clean --dir-site {dir_site} --verbose')
    assert dir_test.name in out.stdout.lower()
    assert file_test.name in out.stdout.lower()
    assert not dir_test.exists()
    assert not file_test.exists()


def test_generate():
    out = run('logya gen --dir-site logya/sites/docs')
    assert out.returncode == 0
    assert 'write pages' in out.stdout.lower()


def test_generate_wrong_dir():
    out = run('logya gen --dir-site .')
    assert out.returncode == 1
    assert 'error' in out.stderr.lower()


def test_create():
    out = run('logya create test_create_site --dir-site tests/fixtures/')
    assert out.returncode == 0
    assert 'site created' in out.stdout.lower()

    # Second time must fail
    out2 = run('logya create test_create_site --dir-site tests/fixtures/')
    assert out2.returncode == 1
    assert 'already exists' in out2.stderr.lower()

    # Cleanup
    rmtree('tests/fixtures/test_create_site')

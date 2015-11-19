from invoke import task, run


@task
def clean():
    run("rm -rf build")


@task(clean)
def install():
    run("pip install -r requirements.pip")
    run("python setup.py install")


@task(install)
def test():
    run("py.test")



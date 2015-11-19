from invoke import task, run


@task
def clean():
    run("rm -rf build")


@task
def lint():
    run("flake8 dotbot test")


@task(clean)
def install():
    run("pip install -r requirements.pip")
    run("python setup.py install")


@task(install, lint)
def test():
    run("py.test")



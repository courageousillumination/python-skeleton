"""This includes all of the tasks for the decks project."""

from invoke import Collection, run, task

PYTHON_PACKAGES = ['example']
PYTHON_FILES = ['tasks.py'] + PYTHON_PACKAGES


# Context is required by tasks even if it's not used.
# pylint: disable=unused-argument
@task
def fix(context):
    """Run autoformating programs."""
    run('yapf --style=config/python_style --in-place -r --exclude="*env*" .',
        warn=True)


@task
def lint(context):
    """Run linters."""
    files = ' '.join(PYTHON_FILES)
    # Suppres reports since they'll just clutter things up.
    run('pylint --rcfile=config/pylintrc --reports=n {}'.format(files),
        warn=True)

@task
def build_docs(context):
    """Build docs."""
    run('sphinx-build -c docs -b html docs docs/_build')

@task
def everything(context):
    """Run all tests."""
    run('nosetests -c config/noserc')


@task
def unit(context):
    """Run all unittests."""
    run('nosetests -c config/noserc -a "!integration,!end_to_end"')


@task
def integration(context):
    """Run integration tests."""
    run('nosetests -c config/noserc -a "integration"')


@task
def end_to_end(context):
    """Run end to end tests."""
    run('nosetests -c config/noserc -a "end_to_end"')


@task
def wip(context):
    """Run any work in progress tests."""
    run('nosetests -c config/noserc -a "wip"')


@task
def coverage(context):
    """Run all tests with coverage options."""
    packages = ','.join(PYTHON_PACKAGES)
    run('nosetests -c config/noserc --with-coverage --cover-branches '
        '--cover-package={}'.format(packages))

# pylint: disable=invalid-name
test = Collection(everything, unit, integration, end_to_end, wip, coverage)
ns = Collection(lint, fix, build_docs, test=test)

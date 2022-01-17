"""This begins a basic cli. In its current state, bem calls these commands if pyvue.repo/tests is True"""

import os
import click
import pytest
from pyvue import core
from pyvue import local
from pyvue.local import PROJ_NAME, PROJ_DIR, PROJ_VERSION, COV_CONFIG
from pprint import pprint


PROJECT_NAME = PROJ_NAME

context_settings = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=context_settings)
@click.version_option(prog_name=PROJECT_NAME.capitalize(), version=PROJ_VERSION)
@click.pass_context
def cli(ctx):
    pass


@click.group(name="system")
def system_group():
    pass


@system_group.command(name="settings")
def settings_cli():
    pprint(local.list_settings(local))


@system_group.command(name="version")
def version_cli():
    print(local.PROJ_VERSION)


@system_group.command(name="selftest")
def selftest_cli():
    pytest.main([str(PROJ_DIR)])


@system_group.command(name="selfcoverage")
def selfcoverage_cli():
    os.chdir(PROJ_DIR)
    cov_config = ""
    if COV_CONFIG:
        cov_config = f"--cov-config={COV_CONFIG}"
    pytest.main([cov_config, f"--cov={PROJ_NAME}", "--cov-report", "term-missing", str(PROJ_DIR)])


@click.command(name="core")
def core_cli():
    core.main()

@click.command(name="pyv")
def core_pyv():
    app = core.Vue("/home/benjamin/predicatestudio/pyvue/SwitchPanel/App.vue")
    print(app)
    print(app.raw_template)

cli.add_command(core_pyv)
cli.add_command(core_cli)
cli.add_command(system_group)
main = cli

if __name__ == "__main__":
    main()

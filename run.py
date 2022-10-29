#!/usr/bin/env python
import click
from sarge import run


def run_compose_cmd(name, command):
    cmd = f'docker compose run --rm {name} {command}'
    result = run(cmd.split())
    if result.returncode != 0:
        print(result.stderr)  # noqa: T201
    exit(result.returncode)


def generate_manage_cmd(*args):
    return f'python manage.py {" ".join(args)}'


@click.command()
@click.argument('name')
@click.argument('command')
def process(name, command):
    manage_py_cmd = generate_manage_cmd(command)
    run_compose_cmd(name, manage_py_cmd)


if __name__ == '__main__':
    process()

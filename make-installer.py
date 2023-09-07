#!/usr/bin/env python3
# adapted from https://stackoverflow.com/questions/63468006

import pathlib
import string
import subprocess
import tempfile
import venv


makensis_exe = "c:/progra~2/NSIS/Bin/makensis.exe"


class EnvBuilder(venv.EnvBuilder):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.context = None

    def post_setup(self, context):
        self.context = context


def main():
    with tempfile.TemporaryDirectory() as target_dir_path:
        print(f" *** Creating virtual env at '{target_dir_path}'.")

        venv_builder = EnvBuilder(with_pip=True)
        venv_builder.create(str(target_dir_path))
        venv_context = venv_builder.context

        pip_install_command = [
            venv_context.env_exe,
            '-m',
            'pip',
            'install',
            'ncrar-abr',
            'pyinstaller',
        ]
        subprocess.check_call(pip_install_command)

        version_command = [
            'python',
            '-c',
            'import ncrar_abr; print(ncrar_abr.__version__)'
        ]
        process = subprocess.Popen(version_command, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        out, err = process.communicate()
        version = out.decode().strip()

        pyinstaller_command = [
            venv_context.env_exe,
            '-m',
            'PyInstaller',
            '-y',
            'ncrar-abr.spec',
        ]
        subprocess.check_call(pyinstaller_command)

        makensis_command = [
            makensis_exe,
            f'/Dversion={version}',
            'ncrar-abr.nsi',
        ]
        subprocess.check_call(makensis_command)


if __name__ == '__main__':
    main()

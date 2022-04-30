import os
import subprocess
from pathlib import Path
import sys
import shutil


def main():
    path: str = input(r"Enter the desired path of the Flutter project: ")
    firebase_proj = input("Is it a firebase project? (y/n) ")

    current_script: str = os.path.dirname(os.path.abspath(__file__))
    lib_dir: Path = Path(f'{path}\lib')
    pubspec_file: Path = Path(f'{path}\pubspec.yaml')
    folders: list[str] = ['models', 'screens', 'services', 'state', 'utils', 'constants']

    os.chdir(f'{path}')

    if pubspec_file.exists() and lib_dir.is_dir():
        print("Valid Flutter project. Executing... ")

        subprocess.run('flutter pub add provider', shell=True)
        subprocess.run('flutter pub add shared_preferences', shell=True)
        subprocess.run('flutter pub add go_router', shell=True)
        # subprocess.run('flutter pub add dio', shell=True)
        # subprocess.run('flutter pub add http', shell=True)
        # subprocess.run('flutter pub add flutter_form_builder', shell=True)
        subprocess.run('flutter pub add path', shell=True)
        subprocess.run('flutter pub add path_provider', shell=True)
        subprocess.run('flutter pub add device_preview --dev', shell=True)
        subprocess.run('flutter pub add responsive_builder', shell=True)
        # subprocess.run('flutter pub add fluttertoast', shell=True)
        # subprocess.run('flutter pub add connectivity_plus', shell=True)
        subprocess.run('flutter pub add change_app_package_name --dev', shell=True)

        if firebase_proj == 'y'.lower():
            subprocess.run('flutter pub add firebase_core', shell=True)
            subprocess.run('flutter pub add firebase_auth', shell=True)
            subprocess.run('flutter pub add google_sign_in', shell=True)
            subprocess.run('flutter pub add cloud_firestore', shell=True)
            # subprocess.run('flutter pub add firebase_storage', shell=True)
            # subprocess.run('flutter pub add firebase_messaging', shell=True)

        print("All packages added!")
        print("Creating necessary folder structure... ")

        os.chdir(f'{path}\lib')

        for folder in folders:
            os.makedirs(folder, exist_ok=True)

        os.chdir(f'{path}\lib\screens')
        os.makedirs('home', exist_ok=True)
        os.chdir(f'{path}\lib\screens\home')
        os.makedirs('widgets', exist_ok=True)

        print("All folders created!")
        print("Copying responsive_helper + providers to their specified locations...")

        os.chdir(f'{current_script}\data')

        shutil.copyfile(r"utils\app_routes.dart",
                        f'{path}' + r'\lib\utils\app_routes.dart')
        shutil.copyfile(r"constants\constants.dart",
                        f'{path}' + r'\lib\constants\constants.dart')
        # shutil.copyfile(r"utils\responsive_helper.dart",
        #                 f'{path}' + r'\lib\utils\responsive_helper.dart')
        shutil.copyfile(r"state\root_state.dart",
                        f'{path}' + r'\lib\state\root_state.dart')
        shutil.copyfile(r"state\theme_state.dart",
                        f'{path}' + r'\lib\state\theme_state.dart')

        shutil.copyfile(r'main.dart', f'{path}' + r'\lib\main.dart')

        os.chdir(f'{current_script}\data\screens\home')

        shutil.copyfile(r"home_screen.dart", f'{path}' + r'\lib\screens\home\home_screen.dart')

        print("Files copied successfully!")

    else:
        print("File does not exist, please enter the correct path!")
        sys.exit()


if __name__ == "__main__":
    main()

from setuptools import setup
import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


extra_files = package_files("./fcreplay/data")

setup(
    name="fcreplay",
    version="0.9",
    description="Fcreplay python code",
    url="http://github.com/glisignoli/fcreplay",
    author="Gino Lisignoli",
    author_email="glisignoli@gmail.com",
    license="GPL3",
    packages=["fcreplay"],
    package_data={"": extra_files},
    entry_points={
        "console_scripts": [
            "fcreplayget=fcreplay.getreplay:console",
            "fcreplayloop=fcreplay.loop:console",
            "fcreplaytasker=fcreplay.tasker:console",
            "fcreplayvalidate=fcreplay.config:console",
        ]
    },
    install_requires=[
        "appdirs==1.4.4",
        "argparse==1.4.0",
        "backports.csv==1.0.7",
        "beautifulsoup4==4.9.3",
        "bootstrap-flask==1.5.1",
        "cachetools==4.2.0; python_version ~= '3.5'",
        "cerberus==1.3.2",
        "certifi==2020.12.5",
        "chardet==3.0.4",
        "click==7.1.2",
        "contextlib2==0.6.0.post1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "debugpy==1.2.0",
        "docker==4.4.0",
        "docopt==0.6.2",
        "dominate==2.6.0",
        "easyprocess==0.3",
        "entrypoint2==0.2.3",
        "flask==1.1.2",
        "flask-cors==3.0.9",
        "flask-sqlalchemy==2.4.4",
        "flask-wtf==0.14.3",
        "google-api-core==1.23.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "google-api-python-client==1.12.8",
        "google-auth==1.24.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
        "google-auth-httplib2==0.0.4",
        "googleapis-common-protos==1.52.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "gunicorn==20.0.4",
        "httplib2==0.18.1",
        "i3ipc==2.2.1",
        "idna==2.10",
        "internetarchive==1.9.6",
        "itsdangerous==1.1.0",
        "jeepney==0.6.0; python_version >= '3.5' and platform_system == 'Linux'",
        "jinja2==2.11.2",
        "jsonpatch==1.28; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "jsonpointer==2.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "lxml==4.6.2",
        "markupsafe==1.1.1",
        "mouseinfo==0.1.3",
        "mss==6.1.0; python_version >= '3.5'",
        "numpy==1.19.4",
        "pillow==8.0.1; python_version >= '3.6'",
        "protobuf==3.14.0",
        "psycopg2==2.8.6",
        "pyasn1==0.4.8",
        "pyasn1-modules==0.2.8",
        "pyautogui==0.9.52",
        "pygetwindow==0.0.9",
        "pymsgbox==1.0.9",
        "pyperclip==1.8.1",
        "pyrect==0.1.4",
        "pyscreenshot==2.2",
        "pyscreeze==0.1.26",
        "python-xlib==0.29",
        "python3-xlib==0.15",
        "pytweening==1.0.3",
        "pytz==2020.4",
        "pyyaml==5.3.1",
        "requests==2.25.0",
        "retrying==1.3.3",
        "rsa==4.6; python_version >= '3.6'",
        "schema==0.7.2",
        "six==1.15.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "soupsieve==2.1; python_version >= '3.0'",
        "sqlalchemy==1.3.20",
        "sqlalchemy-utils==0.36.8",
        "tqdm==4.54.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "uritemplate==3.0.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "urllib3==1.26.2",
        "visitor==0.1.3",
        "websocket-client==0.57.0",
        "werkzeug==1.0.1",
        "wtforms==2.3.3",
    ],
    dependency_links=[],
    zip_safe=False,
)

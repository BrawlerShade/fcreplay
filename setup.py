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
    entry_points={"console_scripts": ["fcreplay=fcreplay.__main__:main"]},
    install_requires=[
        "attrs==21.2.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "backports.csv==1.0.7",
        "bootstrap-flask==1.8.0",
        "cachetools==4.2.4; python_version ~= '3.5'",
        "cerberus==1.3.4",
        "certifi==2021.10.8",
        "charset-normalizer==2.0.7; python_version >= '3'",
        "click==7.1.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "cmd2==1.5.0",
        "colorama==0.4.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "contextlib2==21.6.0; python_version >= '3.6'",
        "debugpy==1.5.1",
        "docker==4.4.4",
        "docopt==0.6.2",
        "feedgen==0.9.0",
        "flask==1.1.4",
        "flask-cors==3.0.10",
        "flask-sqlalchemy==2.5.1",
        "flask-wtf==0.15.1",
        "google-api-core==1.31.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
        "google-api-python-client==1.12.8",
        "google-auth==1.35.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
        "google-auth-httplib2==0.1.0",
        "google-auth-oauthlib==0.4.6",
        "googleapis-common-protos==1.53.0; python_version >= '3.6'",
        "greenlet==1.1.2; python_version >= '3' and platform_machine == 'aarch64' or (platform_machine == 'ppc64le' or (platform_machine == 'x86_64' or (platform_machine == 'amd64' or (platform_machine == 'AMD64' or (platform_machine == 'win32' or platform_machine == 'WIN32')))))",
        "gunicorn==20.1.0",
        "httplib2==0.20.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "i3ipc==2.2.1",
        "idna==3.3; python_version >= '3'",
        "internetarchive==1.9.9",
        "itsdangerous==1.1.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "jinja2==2.11.3",
        "jsonpatch==1.32; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "jsonpointer==2.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "lxml==4.6.4",
        "markupsafe==2.0.1; python_version >= '3.6'",
        "mouseinfo==0.1.3",
        "oauth2client==4.1.3",
        "oauthlib==3.1.1; python_version >= '3.6'",
        "packaging==21.2; python_version >= '3.6'",
        "pillow==8.4.0",
        "progressbar2==3.55.0",
        "protobuf==3.17.3",
        "psycopg2==2.9.1",
        "pyasn1==0.4.8",
        "pyasn1-modules==0.2.8",
        "pyautogui==0.9.53",
        "pygetwindow==0.0.9",
        "pymsgbox==1.0.9",
        "pyparsing==2.4.7; python_version >= '3.1'",
        "pyperclip==1.8.2",
        "pyrect==0.1.4",
        "pyscreeze==0.1.28",
        "python-dateutil==2.8.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "python-logging-loki==0.3.1",
        "python-utils==2.5.6",
        "python-xlib==0.31",
        "python3-xlib==0.15",
        "pytweening==1.0.4",
        "pytz==2021.3",
        "requests==2.26.0",
        "requests-oauthlib==1.3.0",
        "retrying==1.3.3",
        "rfc3339==6.2",
        "rsa==4.7.2; python_version >= '3.6'",
        "schedule==1.1.0",
        "schema==0.7.4",
        "six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "sqlalchemy==1.4.26",
        "sqlalchemy-utils==0.37.9",
        "tqdm==4.62.3; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "uritemplate==3.0.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "urllib3==1.26.7",
        "wcwidth==0.2.5",
        "websocket-client==1.2.1; python_version >= '3.6'",
        "werkzeug==1.0.1",
        "wtforms==2.3.3",
    ],
    dependency_links=[
        "git+https://github.com/tokland/youtube-upload.git@6a30b55d0fd4976571a5b9b34c01fd41cec49c7a#egg=youtube-upload"
    ],
    zip_safe=False,
)

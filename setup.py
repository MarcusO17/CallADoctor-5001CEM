from setuptools import setup

setup(
    name="Call_A_Doctor",
    version='1.0.0',
    description='5001-CEM, Project',
    packages = ['src','api','src.model'],
    install_requires=[
        'blinker==1.6.2',
        'certifi==2023.7.22',
        'charset-normalizer==3.3.0',
        'click==8.1.7',
        'colorama==0.4.6',
        'Flask==2.3.3',
        'idna==3.4',
        'iniconfig==2.0.0',
        'PyQt5 ==5.15.2',
        'itsdangerous==2.1.2',
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.3',
        'packaging==23.2',
        'pluggy==1.3.0',
        'PyMySQL==1.1.0',
        'pytest==7.4.2',
        'pytest-mock==3.11.1',
        'python-dotenv==1.0.0',
        'requests==2.31.0',
        'six==1.16.0',
        'urllib3==2.0.5',
        'Werkzeug==2.3.7',
        'geopy'
        'folium'
        'kaleido'
        'plotly-express'
        'pandas'
    ]
)
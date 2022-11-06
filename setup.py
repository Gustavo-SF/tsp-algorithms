# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tsp_algorithms']

package_data = \
{'': ['*'], 'tsp_algorithms': ['lib/*', 'lib/include/*']}

setup_kwargs = {
    'name': 'tsp-algorithms',
    'version': '0.1.3',
    'description': 'TSP Algorithms developed as C extension for Python',
    'long_description': '# TSP Algorithms developed as C extensions for Python\n\n## Introduction\n\nIn a VRP problem, the objective is to find the best route for a fleet of vehicles to visit a set of customers. The best route is the one that minimizes the total distance traveled by the fleet. The problem is NP-hard, and there are many heuristics to solve it. \n\n## Install\n\nFor now, I am still testing the package, but you can install via pip:\n```bash\npip install --index-url https://test.pypi.org/simple/ tsp-algorithms\n```\n\n## Usage\n\nJust import the package and use one of the methods available:\n\n```python\nimport tsp_algorithms as tsp\n\ntsp.nn([[0., 1.], [2., 3.]])\n```\n\n## Available methods\n\n- [Nearest Neighbour](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm) (`.nn`)\n',
    'author': 'Gustavo-SF',
    'author_email': 'gustavo.fonseca@outlook.pt',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.github.com/gustavo-sf/tsp-algorithms',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>3.8',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)

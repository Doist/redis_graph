#!/usr/bin/env python
# Copyright (c) 2007 Qtrac Ltd. All rights reserved.
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

import os
from setuptools import setup

setup(name='redis_graph',
      version = '1.0',
      author="amix",
      author_email="amix@amix.dk",
      url="http://www.amix.dk/",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      packages=['redis_graph', 'test'],
      platforms=["Any"],
      license="BSD",
      keywords='redis graph database',
      description="Python graph database implemented on top of Redis.",
      long_description="""\
redis_graph
---------------

redis_graph implements a graph database on top of Redis.

Requires:

* Redis 2.0+
* Newest version of redis-py http://github.com/andymccurdy/redis-py
* redis_wrap http://pypi.python.org/pypi/redis_wrap

Related:

* Blog post about redis_graph: http://amix.dk/blog/post/19592#redis-graph-Graph-database-for-Python

Examples
----------

Example of creating edges between nodes::

    from redis_graph import *

    add_edge(from_node='frodo', to_node='gandalf')

    assert has_edge(from_node='frodo',
                    to_node='gandalf') == True

    assert list(neighbors('frodo')) == ['gandalf']

    delete_edge(from_node='frodo',
                to_node='gandalf')

    assert has_edge(from_node='frodo',
                    to_node='gandalf') == False


Example of node and edge values::

    from redis_graph import *

    set_node_value('frodo', '1')
    assert get_node_value('frodo') == '1'

    set_edge_value('frodo_baggins', '2')
    assert get_edge_value('frodo_baggins') == '2'

Copyright: 2010 by amix
License: BSD.""")

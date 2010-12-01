Python graph database implemented on top of Redis
===========================================

Requires:

* Redis 2.0+
* Newest version of [redis-py](http://github.com/andymccurdy/redis-py)
* [redis_wrap](http://pypi.python.org/pypi/redis_wrap)

You can also quick install it from [PyPi](http://pypi.python.org/pypi/redis_graph):
    
* $ sudo easy_install redis_wrap
* $ sudo easy_install redis_graph

Related:

* [Blog post about redis_graph](http://amix.dk/blog/post/19592#redis-graph-Graph-database-for-Python)


Examples
========

Example of creating edges between nodes:

    from redis_graph import *

    add_edge(from_node='frodo', to_node='gandalf')

    assert has_edge(from_node='frodo',
                    to_node='gandalf') == True

    assert list(neighbors('frodo')) == ['gandalf']

    delete_edge(from_node='frodo',
                to_node='gandalf')

    assert has_edge(from_node='frodo',
                    to_node='gandalf') == False


Example of node and edge values:

    from redis_graph import *

    set_node_value('frodo', '1')
    assert get_node_value('frodo') == '1'

    set_edge_value('frodo_baggins', '2')
    assert get_edge_value('frodo_baggins') == '2'

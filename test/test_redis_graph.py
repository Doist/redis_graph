from redis_graph import *


def test_edges():
    #Test adding edge
    add_edge(from_node='frodo',
             to_node='gandalf')

    assert has_edge(from_node='frodo',
                    to_node='gandalf') == True

    assert has_edge(from_node='gandalf',
                    to_node='frodo') == False

    #Test neighbors
    assert list(neighbors('frodo')) == ['gandalf']
    assert len(neighbors('frodo')) == 1

    #Test deleting edge
    delete_edge(from_node='frodo',
                to_node='gandalf')

    assert has_edge(from_node='frodo',
                    to_node='gandalf') == False

    assert len(neighbors('frodo')) == 0


def test_node_values():
    set_node_value('frodo', '1')
    assert get_node_value('frodo') == '1'


def test_edge_values():
    set_edge_value('frodo_baggins', '2')
    assert get_edge_value('frodo_baggins') == '2'


if __name__ == '__main__':
    test_edges()
    test_node_values()
    test_edge_values()

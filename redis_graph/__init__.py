from redis_wrap import *

#--- Edges ----------------------------------------------
def add_edge(from_node, to_node, system='default'):
    edges = get_set( from_node, system=system )
    edges.add( to_node )

def delete_edge(from_node, to_node, system='default'):
    edges = get_set( from_node, system=system )

    key_node_y = to_node
    if key_node_y in edges:
        edges.remove( key_node_y )

def has_edge(from_node, to_node, system='default'):
    edges = get_set( from_node, system=system )
    return to_node in edges

def neighbors(node_x, system='default'):
    return get_set( node_x, system=system )

#--- Node values ----------------------------------------------
def get_node_value(node_x, system='default'):
    node_key = 'nv:%s' % node_x
    return get_redis(system).get( node_key )

def set_node_value(node_x, value, system='default'):
    node_key = 'nv:%s' % node_x
    return get_redis(system).set( node_key, value )

#--- Edge values ----------------------------------------------
def get_edge_value(edge_x, system='default'):
    edge_key = 'ev:%s' % edge_x
    return get_redis(system).get( edge_key )

def set_edge_value(edge_x, value, system='default'):
    edge_key = 'ev:%s' % edge_x
    return get_redis(system).set( edge_key, value )

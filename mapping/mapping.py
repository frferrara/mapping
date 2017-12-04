"""
This file contains a class that is responsible for the mapping between ROS
messages and protobufs.
"""

# Import modules
from ruamel.ordereddict import ordereddict
from libreflection      import reflection as r
# &FEF TBD


class Mapping(object):
    """
    This class is responsible for the mapping between ROS messages and
    protobufs.
    """

    def __init__(self, map_def):
        """
        Constructor. Initialize the class with the mapping definition.
        inputs:
        - map_def: mapping definition
        outputs:
        - Mapping object
        """
        # Set the class attributes
        self.map_def = map_def

    def map_list(self, obj_map, obj_from, obj_to):
        """
        Map an object in form of a list to another object of the same form.
        inputs:
        - obj_map:  object definition in the map
        - obj_from: object that will be mapped
        - obj_to:   destination of the mapping
        outputs:
        - obj_to: destination of the mapping
        """
        # Loop through the list
        for element in obj_map:
            # Get the object (in case it is a key)
            obj = obj_map[element]
            # Check the type
            if isinstance(obj, ordereddict):
                # &FEF TBI
                print "bla"
            elif isinstance(obj, list):
                # &FEF TBI
                print "bla"
            else:
                # Map the elements in the list
                value = r.get_attr(element, obj_from)
                r.set_attr(element, obj_to, value)

        return obj_to

    def map_od(self, obj_map, obj_from, obj_to):
        """
        Map an object in form of a ordereddict to another object of the same
        form.
        inputs:
        - obj_map:  object definition in the map
        - obj_from: object that will be mapped
        - obj_to:   destination of the mapping
        outputs:
        - obj_to: destination of the mapping
        """
        # Loop through the ordereddict
        for element in obj_map:
            # Get the object (in case it is a key)
            obj = obj_map[element]
            # Check the type
            if isinstance(obj, ordereddict):
                # &FEF TBI
                print "bla"
            elif isinstance(obj, list):
                # &FEF TBI
                print "bla"
            else:
                # &FEF TBI
                print "bla"

        return obj_to

    def msg_from_proto(self, msg, proto):
        """
        Map a protobuf to a ROS message.
        inputs:
        - msg:   ROS message object (empty)
        - proto: protobuf object (with data)
        outputs:
        - ret: ROS message object (with data from protobuf object)
        """
        # &FEF TBI
        ret = None
        return ret

    def proto_from_msg(self, proto, msg):
        """
        Map a protobuf to a ROS message.
        inputs:
        - proto: protobuf object (empty)
        - msg:   ROS message object (with data)
        outputs:
        - ret: protobuf object (with data from ROS message object)
        """
        # &FEF TBI
        ret = None
        return ret

    def perform_mapping(self, sub_mapping, obj1, obj2):
        """
        &FEF TBD
        """
        # &FEF TBI
        ret = None
        return ret

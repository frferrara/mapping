"""
This file contains a class that is responsible for the mapping between ROS
messages and protobufs.
"""

# Import modules
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
        self.map_def = map_def

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

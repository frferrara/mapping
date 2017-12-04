"""
This python script is responsible for the testing of the mapping class.

PyLint warnings because of duckietown python environment
W:  7, 0: Relative import 'mapping.mapping', should be 'mapping.mapping.mapping' (relative-import)
W: 10, 0: Relative import 'protobuf._Pose_pb2', should be 'mapping.protobuf._Pose_pb2' (relative-import)
C: 10, 0: Imports from package mapping are not grouped (ungrouped-imports)
"""

# Imports
import sys
from mapping.mapping    import Mapping
from ruamel.yaml        import YAML
from geometry_msgs.msg  import Pose as RPose
from protobuf._Pose_pb2 import Pose as PPose
from ruamel.ordereddict import ordereddict
from protobuf._list_pb2 import List as PList
from dummy_ros.ros_list import List as RList
from libreflection      import reflection as r

"""
Iterating through YAML --> base library on this
-----------------------------------------------
"""
def print_ordereddict(dict_in):
    for value in dict_in:
        print "element: %s" %value
        obj = dict_in[value]
        if isinstance(obj, ordereddict):
            print_ordereddict(obj)
        if isinstance(obj, list):
            print_list(obj)

def print_list(list_in):
    for value in list_in:
        print value
"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

# Load the configuration file
FILE_OBJ = open("config.yaml")
YAML_OBJ = YAML()
CONFIG = YAML_OBJ.load(FILE_OBJ)
print "Yaml dump:"
YAML_OBJ.dump(CONFIG, sys.stdout)
print CONFIG
print_ordereddict(CONFIG["mapping"])

# Create the ROS message
POSE_MSG = RPose()
POSE_MSG.position.x = 1.0
POSE_MSG.position.y = 2.0
POSE_MSG.position.z = 3.0
POSE_MSG.orientation.x = 4.0
POSE_MSG.orientation.y = 5.0
POSE_MSG.orientation.z = 6.0
POSE_MSG.orientation.w = 7.0
print "ROS Pose message:"
print POSE_MSG

# Create the protobuf
POSE_PROTO = PPose()
POSE_PROTO.position.x = 7.0
POSE_PROTO.position.y = 6.0
POSE_PROTO.position.z = 5.0
POSE_PROTO.orientation.x = 4.0
POSE_PROTO.orientation.y = 3.0
POSE_PROTO.orientation.z = 2.0
POSE_PROTO.orientation.w = 1.0

# Instantiate the mapping class
MAPPING = Mapping(CONFIG)

# Set the proto list
p_list = PList()
p_list.x = 4.0
p_list.y = 5.0
p_list.z = 6.0

# Set the ROS list
r_list = RList()
print "r_list.x: {}".format(r_list.x)
print "r_list.y: {}".format(r_list.y)
print "r_list.z: {}".format(r_list.z)

# Read the map file
FILE_OBJ = open("list.yaml")
YAML_OBJ = YAML()
OBJ_MAP = YAML_OBJ.load(FILE_OBJ)

# Map the proto to the ROS list
print OBJ_MAP
MAPPING.map_list(OBJ_MAP["list"], p_list, r_list)
print "r_list.x: {}".format(r_list.x)
print "r_list.y: {}".format(r_list.y)
print "r_list.z: {}".format(r_list.z)
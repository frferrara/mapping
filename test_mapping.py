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

# Load the configuration file
FILE_OBJ = open("config.yaml")
YAML_OBJ = YAML()
CONFIG = YAML_OBJ.load(FILE_OBJ)
print "Yaml dump:"
YAML_OBJ.dump(CONFIG, sys.stdout)

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

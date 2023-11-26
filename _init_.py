import os
import subprocess
import importlib.util
import sys

python = sys.executable

# call classes used
from .SampleDiffusion import EXT_AudioManipulation
from .SampleDiffusion import EXT_PedalBoard
from .SampleDiffusion import EXT_SampleDiffusion
from .SampleDiffusion import EXT_Spectrology
from .SampleDiffusion import EXT_VariationUtils
from .SampleDiffusion import EXT_WaveGen

# Node Names from the beginning
# Note: Name: Unique to all node classes
NODE_CLASS_MAPPINGS = {
    "EXT_AudioManipulation":AudioManipulation,
    "EXT_PedalBoard":PedalBoard
    
}

#Main titles
NODE_DISPLAY_NAME_MAPPINGS = {
    "AudioManipulation": "AudioManipulation #Example Node"
    
}

for node in os.listdir(os.path.dirname(__file__)):
    if node.startswith('EXT_'):
        node = node.split('.')[0]
        node_import = importlib.import_module('custom_nodes.SampleDiffusion.' + node)
        # get class node mappings from py file
        NODE_CLASS_MAPPINGS.update(node_import.NODE_CLASS_MAPPINGS)
# web ui feature
WEB_DIRECTORY = "./web"

#print confirmation

print('--------------')
print('\ComfyUI_SampleAudio_diffusion nodes_loaded')
print('--------------')

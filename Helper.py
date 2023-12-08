import tensorflow as tf

import os

filemega = lambda filepath : os.path.getsize(filepath) / float(2**20)
from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import numpy as np
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame

def h2o_H2OFrameAtan():
    """
    Python API test: h2o.frame.H2OFrame.atan()
    """
    python_lists = np.random.uniform(-1,1, (3,4))
    h2oframe = h2o.H2OFrame(python_obj=python_lists)
    newframe = h2oframe.atan()
    assert_is_type(newframe, H2OFrame)
    pyunit_utils.assert_correct_frame_operation(h2oframe, newframe, "atan")

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrameAtan())
else:
    h2o_H2OFrameAtan()
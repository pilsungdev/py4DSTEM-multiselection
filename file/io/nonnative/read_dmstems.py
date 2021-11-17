import numpy as np
from PyQt5.QtWidgets import QInputDialog, QFileDialog
import hyperspy.api as hs
from ...datastructure import DataCube

def read_dmstems(fp, mem="RAM", binfactor=1, **kwargs):
    fp, _ = QFileDialog.getOpenFileName()
    file = hs.load(fp)
    text, ok = QInputDialog.getText(None, "Input dimension size","example:50x20")
    left_dim = int(str(text)[:str(text).find('x')])
    right_dim = int(str(text)[str(text).find('x')+1:])
    if ok:
        return DataCube(np.reshape(file.data,(left_dim,right_dim,file.data.shape[1],file.data.shape[2]))), None

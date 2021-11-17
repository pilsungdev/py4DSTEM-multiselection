#!/usr/bin/env python

from gui import DataViewer
import sys

def launch():
    app = DataViewer(sys.argv)

    sys.exit(app.exec_())

if __name__ == '__main__':
    app = DataViewer(sys.argv)

    sys.exit(app.exec_())

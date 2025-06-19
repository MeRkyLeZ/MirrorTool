import os

from mirrortool import installation

if installation.TYPE == installation.TYPES.SYSTEM:
    MIRRORTOOL_BASE_PATH = """@MIRRORTOOL_BASE_PATH@"""
elif installation.TYPE == installation.TYPES.MODULE:
    MIRRORTOOL_BASE_PATH = os.path.join(
        os.path.realpath(__import__("sys").prefix), "lib/mirrortool"
    )
else:
    MIRRORTOOL_BASE_PATH = os.path.join(
        os.sep, *os.path.realpath(__file__).split(os.sep)[:-3]
    )

if installation.TYPE == installation.TYPES.SYSTEM:
    MIRRORTOOL_BIN_PATH = """@MIRRORTOOL_BIN_PATH@"""
else:
    MIRRORTOOL_BIN_PATH = f"{MIRRORTOOL_BASE_PATH}/bin"
__all__ = ["bin_entry_point"]

import sys

from mirrortool.const import MIRRORTOOL_BIN_PATH
from portage import os


def bin_entry_point():
    """
    Adjust sys.argv[0] to point to a script in PORTAGE_BIN_PATH, and
    then execute the script, in order to implement entry_points when
    portage has been installed by pip.
    """
    script_path = os.path.join(MIRRORTOOL_BIN_PATH, os.path.basename(sys.argv[0]))
    if os.access(script_path, os.X_OK):
        sys.argv = [
            sys.executable,
            script_path,
        ] + sys.argv[1:]
        os.execvp(sys.argv[0], sys.argv)
    else:
        print("File not found:", script_path, file=sys.stderr)
        return 127

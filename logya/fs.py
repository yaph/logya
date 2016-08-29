import os
import shutil


def copytree(src, dst):
    """Copy a directory tree.

    Existing directories in the destination (dst) are ok.
    Source files (src) are only copied if newer than destination or destination
    does not exist.
    """

    os.makedirs(dst, exist_ok=True)
    for root, dirs, files in os.walk(src):
        relative_root = root[len(src):].strip('/')

        for d in dirs:
            dir_dst = os.path.join(dst, relative_root, d)
            if not os.path.exists(dir_dst):
                os.makedirs(dir_dst)

        for f in files:
            file_src = os.path.join(root, f)
            file_dst = os.path.join(dst, relative_root, f)
            if not os.path.exists(file_dst) or os.path.getmtime(file_src) > os.path.getmtime(file_dst):
                shutil.copyfile(file_src, file_dst)

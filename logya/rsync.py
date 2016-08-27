import os


def sync_dirs(src, dst):
    if not os.path.exists(dst):
        #os.makedirs(dst, exist_ok=True)
        print('make new dir: {}'.format(dst))


def sync_files(src, dst):
    print('{} -> {}'.format(src, dst))


def rsync(src, dst):
    os.makedirs(dst, exist_ok=True)
    for root, dirs, files in os.walk(src):
        relative_root = root[len(src):].strip('/')
        if (dirs):
            print('DIRECTORIES')
            for d in dirs:
                dir_src = os.path.join(root, d)
                dir_dst = os.path.join(dst, relative_root, d)
                sync_dirs(dir_src, dir_dst)
        if (files):
            print('FILES')
            for f in files:
                file_src = os.path.join(root, f)
                file_dst = os.path.join(dst, relative_root, f)
                sync_files(file_src, file_dst)
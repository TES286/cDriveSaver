import os
import shutil


def move(f_from, f_to):
    if is_dir(f_from):
        move_dir(f_from, f_to)
    else:
        move_file(f_from, f_to)


def is_dir(path):
    if os.path.exists(path):
        return os.path.isdir(path)
    else:
        error('File % is not exists, please click.' % path)


def move_file(f_from, f_to):
    if os.path.exists(f_from):
        shutil.copyfile(f_from, f_to)
        os.remove(f_from)
        make_link(f_from, f_to)
    else:
        error('File % is not exists, please click' % f_from)


def move_dir(f_from, f_to):
    if os.path.exists(f_from):
        if os.path.isdir(f_from):
            shutil.copytree(f_from, f_to)
            shutil.rmtree(f_from)
            make_link(f_from, f_to)
    else:
        error('File % is not exists, please click' % f_from)


def make_link(f_from, f_to):
    # os.symlink(f_from, f_to)
    os.symlink(f_to, f_from)


def error(string):
    print('Error: ' + string)
    exit(1)


def show():
    file_from = input('Please enter a file or a dir you want to move from: ')
    file_to = input('Please enter a file or a dir you want to move to: ')
    move(file_from, file_to)


if __name__ == '__main__':
    show()

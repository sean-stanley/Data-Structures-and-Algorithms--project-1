import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    forbidden_paths = [
        '',
        '~',
        'C:/',
        '/',
    ]

    if path in forbidden_paths:
        return Exception('please do not search the entire device.')

    dir = os.listdir(path)
    matches = []
    for i in dir:
        full_path = path + '/' + i
        if os.path.isdir(full_path):
            matches += find_files(suffix, full_path)
        elif os.path.isfile(full_path) and i.endswith(suffix):
            matches.append(full_path)

    return matches

print(find_files('.c', '.'))

# edge case with empty path
print(find_files('.c', ''))

# edge case with forbidden path
print(find_files('.c', '/'))

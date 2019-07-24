class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

SUB_CHILD_USER = "sub_child_user"
sub_child.add_user(SUB_CHILD_USER)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if not isinstance(group, Group):
        return Exception('Group must be a group')

    users = group.get_users()
    if user in users:
        return True

    groups = group.get_groups()

    if groups:
        for g in groups:
            found = is_user_in_group(user, g)
            if found:
                return True

    return False

print(is_user_in_group(SUB_CHILD_USER, parent))
# returns True

print(is_user_in_group('foo', parent))
# returns False

print(is_user_in_group('foo', ''))
# returns Exception(Group must be a group)

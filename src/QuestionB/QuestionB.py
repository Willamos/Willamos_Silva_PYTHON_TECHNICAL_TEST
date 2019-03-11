# Question B

# The goal of this question is to write a software library that accepts 2 version
# string as input and returns whether one is greater than, equal, or less than the other.
# As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

def check_version(version1: str, version2: str):
    assert(type(version1) == str), 'version1 should be a string'
    assert(type(version2) == str), 'version2 should be a string'
    version1 = version1.split('.')
    version2 = version2.split('.')
    (longer, shorter) = (version1, version2) if len(version1) > len(version2) else (version2, version1)
    for i in range(len(shorter)):
        val_larger = int(longer[i])
        val_smaller = int(shorter[i])
        if val_larger > val_smaller:
            return '.'.join(shorter) +' is older than ' + '.'.join(longer)
        elif val_larger < val_smaller:
            return '.'.join(longer) +' is older than ' + '.'.join(shorter)
        elif i == (len(shorter)-1):
            if len(longer) != len(shorter):
                for j in range(i+1, len(longer)):
                    val = int(longer[j])
                    if val != 0:
                        return '.'.join(shorter) + ' is older than ' + '.'.join(longer)
    return 'both ' + '.'.join(longer) + ' and ' + '.'.join(shorter) + ' are the same version'

# my idea for this question was to split the versions based on dots ('.') to compare
# the values of each one of the items in the list as int values. I'm ordering the lists by their size
# (shorter and longer versions).  04 should be newer than 3, even if char 0 is smaller than char 3.
# Therefore, I've converted every item into int. if the versions are the same until the last item from
# the smaller version, it is mandatory to check if the remaining items from the larger version are
# greater than zero. if at least one of them is not zero, the shorter version is older than the larger one



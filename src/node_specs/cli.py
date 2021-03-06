spec = {
    "title": "cli",
    "id": "pyflow.source.cli",
}


def func(command):
    """
    :params: command
    :ptypes: String
    :returns: out
    :rtype: String
    """

    import shlex
    import subprocess
    # This cli cannot hand code that refresh the screen like top
    args = shlex.split(command)
    p = subprocess.Popen(
        args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outdata, errdata = p.communicate()
    if len(errdata) != 0:
        raise Exception(
            'Failed to execut command % , error is {}'.format(command, errdata))
    return outdata

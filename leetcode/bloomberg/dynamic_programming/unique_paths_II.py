class PathsUitls(object):
    """
    bfs and for every hit to finish point, we increase
    res count
    """
    def unique_paths_II(self, mat):
        """
        if paths[r][c] == 1:
            paths[r][c] = 0
        else:
            paths[r][c] = paths[r-1][c] + paths[r][c-1]
        :param mat:
        :return:
        """
        if not mat:
            return None


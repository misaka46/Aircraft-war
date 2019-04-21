import abc


class Award(object):
    """奖励"""
    LIFE = 0
    FIRE_RED = 1
    FIRE_PURPLE = 2


    @abc.abstractmethod
    def getType(self):
        """获得奖励类型"""
        pass


if __name__ == '__main__':

    print(Award.DOUBLE_FIRE)

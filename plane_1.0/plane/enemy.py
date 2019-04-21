import abc

class Enemy(object):
    """敌人，敌人有分数"""
    @abc.abstractmethod
    def getScore(self):
        """获得分数"""
        pass
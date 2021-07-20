# 建立一個"步驟"檔案，作為母函式，讓其他子函式繼承，統一規範。
from abc import ABC
from abc import abstractmethod


class Step(ABC):  # 基底Class
    def __init__(self):
        pass

    @abstractmethod  # 抽象類別
    def process(self, date, inputs):  # 核心函數"處理"
        pass


class StepException(Exception):  # 捕捉例外
    pass

# pipeline 導管，負責執行各項流程。

from .steps.setp import StepException


class Pipeline():
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        date = None
        for step in self.steps:
            try:
                date = step.process(date, inputs)
            except StepException as e:
                print('Exception happened in steps', e)
                break

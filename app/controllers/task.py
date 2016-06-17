"""
    Simple task skeleton
"""


class Task(object):
    """
        Abstract class to define a task to execute.
    """
    execution_level = 0     # execution level: 0 is the higher, 32 is the
    # lower: level0 tasks will run before level1,
    # which will run before level32 tasks. Use
    # this to run after tasks you depend on.

    is_interrested = True   # setting this value to False will make the
    # scheduler not call your task's methods.
    tmessage = ""

    def __init__(self, sample=None):
        """
            @sample: the sample's object.
            Here you can copy any of the sample data. You should not copy
            the sample object itself as desynchronization issues may occur.

                self.storage_file = sample.storage_file
                self.sample_id = sample.id
                [...]

            You should also determine here if your task will run on the
            provided file by modifying the self.is_interrested value.

            Finally, you can also set your execution_level here, if it must
            be elevated.
        """
        self.tmessage = "BaseTask"
        pass

    def __repr__(self):
        return "Task %s" % (self.tmessage)

    def execute(self):
        """
            Do the main work from the sample.
            Return: True or False
        """
        raise ValueError

    def will_run(self):
        """
            This method is called before the execute() method. Actually
            the method will just return the is_interrested value, but you
            can superseede it if you want.
        """
        return self.is_interrested

    def apply_result(self):
        """
            This gets called when the task is finished, you can commit your
            results here.
            Return: True or False
        """
        raise ValueError

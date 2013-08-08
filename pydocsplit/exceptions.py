#!/usr/bin/env python
# encoding: utf-8


class ExtractionError(Exception):

    def __init__(self, cmd, msg):
        self.cmd = cmd
        self.msg = msg
        super(ExtractionError, self).__init__(cmd, msg)

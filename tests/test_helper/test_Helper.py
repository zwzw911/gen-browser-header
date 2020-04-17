import sys
import os
a=os.path.dirname(os.path.dirname(os.getcwd()))
# print(a)
sys.path.append(a)
# print(sys.path)
import pytest
import self.SelfEnum as self_enum

import helper.Helper as helper


@pytest.mark.all_values_preDefined
class Test_all_values_preDefined(object):
    # test_func = helper.all_values_preDefined
    # def setup_class(self):
    #     self.test_func = helper.all_values_preDefined

    def test_empty_values(self):
        assert helper.all_values_preDefined(values=set(), defined_enum=self_enum.OsType) == \
               True

    def test_all_valid_values(self):
        assert helper.all_values_preDefined(values=set({self_enum.OsType.Win64}),
                                            defined_enum=self_enum.OsType) == \
               True

    def test_invalid_values(self):
        assert helper.all_values_preDefined(values=set({'invalid'}),
                                            defined_enum=self_enum.OsType) == \
               False

if __name__ == '__main__':
    pass
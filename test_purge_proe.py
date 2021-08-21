from unittest import TestCase
from purge_proe import *

# backup
def file_list_get_proe_files(file_list=[]):
    if file_list == []: return []
    new_list = []
    from re import search
    for file in file_list:
        if search(r'(.*)\.(\w*)\.(\d*)$', file):
            new_list.append(file)
    return new_list

#================================================================

import random, string
class RandomFileGeneration():
    lastest_file_list = []
    def generation_string(self,digit_num):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(digit_num))
    def generation_normal_file(self):
        n = random.randint(2,8)
        return '.'.join([self.generation_string(n),self.generation_string(3)])
    def generation_proe_files(self):
        files_count = random.choices(range(1, 5), [5, 2, 3, 1])[0]
        files_SN = random.sample(range(120), files_count)
        file_name = self.generation_normal_file()
        file_list = []
        self.lastest_file_list.append('.'.join([file_name, str(max(files_SN,key=int))]))
        for sn in files_SN:
            file_list.append('.'.join([file_name,str(sn)]))
        return file_list
    def lastest_proe_file_list(self):
        return self.lastest_file_list
    def generation_test_file_list(self):
        files_list = []
        for _ in range(4):
            files_list.extend(self.generation_proe_files())
        for _ in range(2):
            files_list.append(self.generation_normal_file())
        return files_list



class Test(TestCase):
    def test_get_cwd_file(self):
        from os import getcwd
        from os import listdir
        file_list = listdir(getcwd())
        self.assertCountEqual(file_list, get_cwd_file())

    def test_file_list_get_proe_files_1(self):
        test_l=['picture.jpg','12n3.g']
        result_l=[]
        r = file_list_get_proe_files(test_l)
        self.assertCountEqual(r, result_l)
    def test_file_list_get_proe_files_2(self):
        test_l = [
            'af54a6f.prt.23',
            'af54a6f.prt.48',
            '.prt.2',
            '43748.prt.23',
            'efaf.txt',
            'picture.jpg',
            'top.asm.73'
        ]
        result_l = [
            'af54a6f.prt.23',
            'af54a6f.prt.48',
            '.prt.2',
            '43748.prt.23',
            'top.asm.73'
        ]
        self.assertCountEqual(file_list_get_proe_files(test_l), result_l)

    def test_get_old_file_1(self):
        orgin_l = [
            '1.txt.1',
            '1.txt.22',
            '1.txt.3',
            'sfa.txt.3',
            'sfa.txt.11',
            'oiaoif.fa1233.jpg.1',
            'oiaoif.fa1233.jpg.10'
        ]
        answer_L = [
            '1.txt.1',
            '1.txt.3',
            'sfa.txt.3',
            'oiaoif.fa1233.jpg.1'
        ]
        result_L=get_older_file(orgin_l)
        self.assertCountEqual(result_L, answer_L)

    def test_get_old_file_auto(self):
        L = RandomFileGeneration()
        orgin_l = L.generation_test_file_list()
        answer_L = list(set(file_list_get_proe_files(orgin_l))-set(L.lastest_proe_file_list()))
        result_L = get_older_file(orgin_l)
        self.assertCountEqual(result_L, answer_L)
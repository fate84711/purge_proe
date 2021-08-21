'''
author:Louis
update:2020/08/21
'''

def get_cwd_file():
    from os import getcwd
    from os import listdir
    file_list = listdir(getcwd())
    return file_list

def get_older_file(proe_file_list=[]):
    if proe_file_list == []:return []
    proe_file_list = sorted(proe_file_list,reverse=True)
    removed_file_list = []
    last_f, last_num = '',''
    for file in proe_file_list:
        now_f, now_num = file.rsplit('.',1)
        if now_f == last_f:
            removed_file_list.append(now_f+ '.'+ min(now_num, last_num, key=int))
        else:
            last_f, last_num = now_f, now_num
    return removed_file_list

def remove_file_list_in_cwd(remove_file_list):
    from os import remove
    for file in remove_file_list:
        remove(file)

if __name__ == "__main__":
    file_list_in_dir = get_cwd_file()
    remove_file_list = get_older_file(file_list_in_dir)
    remove_file_list_in_cwd(remove_file_list)











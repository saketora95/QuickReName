import os

ignore_file_list = ['main.py', 'main.exe', 'QuickReName.exe', 'README.md', '.git']
current_directory = os.getcwd() + '\\'
exist_file_list = os.listdir(current_directory)

print('# 渣渣改名程式')
print('- 以下檔案將會被改名: ')
rename_list = []
for file in exist_file_list:
    file_path = current_directory + file

    if file not in ignore_file_list and os.path.isfile(file_path):
        rename_list.append(file)
        print('  - ' + file_path)

print('')
add_text = input('# 你想要在檔案名字後面加上：')
print('- 收到你的輸入，將為檔案追加 [ {} ] 的字串。\n'.format(add_text))

print('# 開始更改名稱')
for file in rename_list:
    base_name, extension_name = os.path.splitext(file)
    new_name = '{0}{1}{2}'.format(base_name, add_text, extension_name)

    os.rename(
        current_directory + file,
        current_directory + new_name
    )
    print('  - 檔案 [ {0} ] 更名為 [ {1} ]'.format(file, new_name))

print('')
print('# 程式到此結束.\n')
os.system('pause')
    
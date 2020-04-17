import os

source = str(input('enter full source directory (format: /home/adam/*.txt): '))
path = str(input('enter full target directory (format: /home/adam/*.txt): '))
extension = str(input('enter new file extension (format: .ext): '))

source_list = os.listdir(source)
Num_Starting_Files = len(source_list)

print('Beginning File Move and Extension Change')
print('')

while len(source_list) > 0:
    i = 0
    file = str(source_list[i])
    pre, ext = os.path.splitext(file)
    os.rename(str(source + '/' + file), str(path + '/' + pre + extension))
    source_list = os.listdir(source)
    print(len(source_list))
    if len(source_list) == 0:
        print('File Move Complete')
        print('')
        break

path_list = os.listdir(path)
print('Starting Number of Source Files: ', Num_Starting_Files)
print('Source Directory Should Be Empty: ', source_list)
print('Source of Number of Files Should be 0: ', len(source_list))
print('Path Directory Should should have files: ', path_list)
print('Number of Files in Path Should = Starting Source: ', len(path_list))

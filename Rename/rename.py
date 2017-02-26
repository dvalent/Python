import os

path = '/Users/xxx/Desktop/'  # path here

for file in os.listdir(path):
    filepath = os.path.join(path,file)
    print filepath
    #if file.startswith('Video'):

        #os.rename(filepath,filepath[47:])

class FileOp:
    def savedata(self, file_name, data):
        try:
            selected_file = open(file_name, "a")
            selected_file.write(data + '\n')
            selected_file.close()
        except Exception as error:
            print("could not save data")
            print(error)

    def getData(self, file_name):
        try:
            data = []
            selected_file = open(file_name)
            return selected_file.readlines()
        except Exception as error:
            print("could not read data")
            print(error)

fileOp = FileOp()


         
            

     
         
                

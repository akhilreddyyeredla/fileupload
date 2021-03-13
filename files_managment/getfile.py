import database_conn
class FileManagment:
    def __init__(self):
        pass

    def search_table(self,search_string):
        conn = database_conn.connection()
        try:
            cur = conn.cursor()
            sql = "select * from image_storage where active=0 and image_name like '%"+str(search_string)+"%'"
            cur.execute(sql)
            output = cur.fetchall()
            return output
        except Exception as e:
            print(e)
            return 404

    def getfilename(self,search_string):
        search_data = self.search_table(search_string)
        if (search_data == 400):
            response = {"status": "Failed", "code": 400,
                        "message": "API Failed while fetching data from database"
                        }

            return response
        elif(len(search_data)==0):
            response = {"status": "success", "code": 404,
                        "message": "No data found",
                        "data": {

                        }
                        }
            return response
        else:
            search_data_list = []
            for data in search_data:
                search_data_dic = {}
                search_data_dic['id'] = data[0]
                search_data_dic['image_name'] = data[1]
                search_data_dic['image_url'] = data[2]
                search_data_list.append(search_data_dic)
            response = {"status": "success", "code": 200,
                        "message": "Data fetched Sucessfully",
                        "data": {
                            "image_path": search_data_list
                        }
                        }
            return response







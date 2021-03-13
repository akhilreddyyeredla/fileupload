import config
import database_conn
import boto3
class upload_class:
    def __init__(self):
        pass
    def Check_file(self,file_name):
        conn = database_conn.connection()
        cur = conn.cursor()
        sql = "select * from image_storage where active=0 and image_name='" + str(file_name) + "'"
        cur.execute(sql)
        output = cur.fetchall()
        return len(output)

    def Insert_to_DB(self,file_name,path):
        conn = database_conn.connection()
        try:
            cur = conn.cursor()
            sql = "insert into image_storage (image_name,image_path,active) values ('"+str(file_name)+"','"+str(path)+"','"+str(0)+"')"
            cur.execute(sql)
            conn.commit()
            return 200
        except Exception as e:
            print(e)
            return 400
    def upload_file(self,file_path,file_name):
        try:
            #file_name = file_path.split('/')[-1]
            if(self.Check_file(file_name)!=0):
                response = {"status": "Sucess", "code": 400,
                            "message": "File with name "+str(file_name)+" already exist"
                            }

                return response
            else:
                s3 = boto3.resource('s3')
                s3.meta.client.upload_file(file_path, config.bucket_name , file_name)
                path = config.s3_path+str(file_name)
                database_response = self.Insert_to_DB(file_name,path)
                if(database_response==200):
                    response = { "status": "success","code": 200,
                                    "message": "Data Updated Sucessfully",
                                    "data": {
                                                "image_path": path
                                            }
                                   }
                    return response
                if(database_response==400):
                    response = {"status": "Failed", "code": 400,
                                "message": "API Failed while inserting to database"
                                }


                    return response
        except:
            response = {"status": "Failed", "code": 400,
                        "message": "API Failed while uploading file"
                        }
            return response



import database_conn
import boto3
import config
class Filedestory:
    def __init__(self):
        pass

    def delete_from_table(self,file_id):
        conn = database_conn.connection()
        try:
            cur = conn.cursor()
            sql = "UPDATE image_storage SET active="+str(1)+" where id="+str(file_id)

            cur.execute(sql)
            conn.commit()
            response = {"status": "success", "code": 200,
                        "message": "Image Deleted Sucessfully",

                        }
            return response
        except Exception as e:
            response = {"status": "Failed", "code": 400,
                        "message": "API Failed while updated to database"
                        }
            return response

    def delete_from_s3(self,file_id):
        try:
            conn = database_conn.connection()
            cur = conn.cursor()
            sql = "select * from image_storage where id="+str(file_id)+" and active=0"
            cur.execute(sql)
            output = cur.fetchall()
            if(len(output)==0):
                response = {"status": "Sucess", "code": 400,
                            "message": "File with Id "+str(file_id)+" not found"
                            }
                return response
            else:
                file_key = output[0][1]

                print(file_key)
                s3 = boto3.resource("s3")
                obj = s3.Object(config.bucket_name, file_key)
                obj.delete()
                table_response = self.delete_from_table(file_id)
                return table_response
        except:
            response = {"status": "Failed", "code": 400,
                        "message": "API Failed while deleting file"
                        }
            return response



    def delete_file(self,id):
        file_response = self.delete_from_s3(id)
        return file_response







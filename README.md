# File Structure
**app/views.py ->** will have the routes 


**files_managment ->** All the core code which are in different files according to the features


**config.py ->** database credentials and other access keys for the cloud


**database_conn.py ->** MYSQL connection class which returns the connection object


**run.py ->** Flask start point


**requriments.py ->** all the librarys which are used accross the project

# End Points


**Image Upload [POST]**
End point -> localhost:5000/upload-file?file_name="name of the Image along with Image extension"


payload -> upload as a file with a key name **"**image**"**

**Get File Info [GET]**
End point -> localhost:5000/get-file-data?file_name="search string"


**Delete Image [GET]**
End point -> localhost:5000/delete-file?file_id="file ID"


# Create Table in MYSQL

CREATE TABLE `image_storage` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `image_name` VARCHAR(45) NOT NULL,
  `image_path` VARCHAR(45) NOT NULL,
  `active` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));

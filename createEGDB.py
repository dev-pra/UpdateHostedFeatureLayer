import arcpy

def createEGDB():
    database_platform = "SQL_Server"
    instance_name = "localhost"
    database_name = "edmar_test"
    account_authentication = "DATABASE_AUTH"
    database_admin = "sa"
    database_admin_password = "Password_01"
    sde_schema = "DBO_SCHEMA"
    authorization_file = r"C:\tempgis\pgtest\keycodes"

    arcpy.CreateEnterpriseGeodatabase_management(database_platform,instance_name,database_name,account_authentication,database_admin,database_admin_password,sde_schema,None,None,None,authorization_file)

def createEGDBConnectionFile():
    print("Creating connection file in the local directory")
    out_folder_path = "."
    out_name = "sa_connection_to_edmar_test"
    database_platform = "SQL_SERVER"
    instance = "localhost"
    account_authentication = "DATABASE_AUTH"
    username = "sa"
    password = "Password_01"
    save_user_pass = "SAVE_USERNAME"
    database = "edmar_test"
    
    arcpy.CreateDatabaseConnection_management(out_folder_path,out_name,database_platform,instance,account_authentication,username,password,save_user_pass,database)

if __name__ == '__main__':
    createEGDB()
    createEGDBConnectionFile()
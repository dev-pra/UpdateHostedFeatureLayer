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


if __name__ == '__main__':
    createEGDB()
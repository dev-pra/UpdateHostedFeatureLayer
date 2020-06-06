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

def createCapitalFC():
    print("Creating Capitals Feature Class")
    #Create feature class
    out_path = "sa_connection_to_edmar_test.sde"
    out_name = "capitals"
    geometry_type = "POINT"
    template = None
    has_m = "DISABLED"
    has_z = "DISABLED"
    spatial_ref = arcpy.SpatialReference(3857)
    arcpy.CreateFeatureclass_management(out_path,out_name,geometry_type,template,has_m,has_z,spatial_ref)

    #Add fields
    arcpy.AddField_management(out_path + "\\" + out_name, field_name="country", field_type="TEXT", field_precision="", field_scale="", field_length="50", field_alias="Country", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(out_path + "\\" + out_name, field_name="capital", field_type="TEXT", field_precision="", field_scale="", field_length="50", field_alias="Capital", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(out_path + "\\" + out_name, field_name="latitude", field_type="DOUBLE", field_precision="", field_scale="", field_length="", field_alias="Latitude", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    arcpy.AddField_management(out_path + "\\" + out_name, field_name="longitude", field_type="DOUBLE", field_precision="", field_scale="", field_length="", field_alias="Longitude", field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="")
    


if __name__ == '__main__':
    createEGDB()
    createEGDBConnectionFile()
    createCapitalFC()

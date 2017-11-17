import sys


import arcpy

# Using NAD 83 as coordinate system
spatial_ref = arcpy.SpatialReference(4269)
directory = sys.path[0]


def convert_to_points():
    """Parses query results from CRIS and converts to GIS point format. Exports feature classes for each year of TXDoT
    data."""
    workspace = '{0}\\DWIBexar.gdb'.format(directory)
    data_years = range(2010, 2018)
    if arcpy.Exists(workspace):
        pass
    else:
        arcpy.CreateFileGDB_management(directory, "DWIBexar")
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = True

    for year in data_years:
        print directory
        csv = '{0}\\CSV\\CRIS{1}.csv'.format(directory, year)
        table = 'tbl{0}'.format(year)
        # Prep CSV by converting lat long to float and removing NaN

        arcpy.TableToTable_conversion(in_rows=csv,
                                      out_path=workspace,
                                      out_name=table, where_clause="",
                                      field_mapping="Crash_ID 'Crash_ID' true true false 4 Long 0 0 ,First,#," + csv + ",Crash ID,-1,-1;Agency 'Agency' true true false 8000 Text 0 0 ,First,#," + csv + ",Agency,-1,-1;Average_Daily_Traffic_Amount 'Average_Daily_Traffic_Amount' true true false 30 Text 0 0 ,First,#," + csv + ",Average Daily Traffic Amount,-1,-1;Construction_Zone_Flag 'Construction_Zone_Flag' true true false 8000 Text 0 0 ,First,#," + csv + ",Construction Zone Flag,-1,-1;Crash_Death_Count 'Crash_Death_Count' true true false 4 Long 0 0 ,First,#," + csv + ",Crash Death Count,-1,-1;Crash_Severity 'Crash_Severity' true true false 8000 Text 0 0 ,First,#," + csv + ",Crash Severity,-1,-1;Crash_Time 'Crash_Time' true true false 4 Long 0 0 ,First,#," + csv + ",Crash Time,-1,-1;Crash_Year 'Crash_Year' true true false 4 Long 0 0 ,First,#," + csv + ",Crash Year,-1,-1;Day_of_Week 'Day_of_Week' true true false 8000 Text 0 0 ,First,#," + csv + ",Day of Week,-1,-1;Latitude 'Latitude' true true false 20 Text 0 0 ,First,#," + csv + ",Latitude,-1,-1;Longitude 'Longitude' true true false 30 Text 0 0 ,First,#," + csv + ",Longitude,-1,-1;Charge 'Charge' true true false 8000 Text 0 0 ,First,#," + csv + ",Charge,-1,-1")

        arcpy.TableToTable_conversion(in_rows=table,
                                      out_path=workspace,
                                      out_name="{0}_".format(table), where_clause="Latitude <> 'No Data' AND Longitude <> 'No Data' ",
                                      field_mapping="Crash_ID 'Crash_ID' true true false 4 Long 0 0 ,First,#," + table + ",Crash_ID,-1,-1;Agency 'Agency' true true false 8000 Text 0 0 ,First,#," + table + ",Agency,-1,-1;Average_Daily_Traffic_Amount 'Average_Daily_Traffic_Amount' true true false 30 Text 0 0 ,First,#," + table + ",Average_Daily_Traffic_Amount,-1,-1;Construction_Zone_Flag 'Construction_Zone_Flag' true true false 8000 Text 0 0 ,First,#," + table + ",Construction_Zone_Flag,-1,-1;Crash_Death_Count 'Crash_Death_Count' true true false 4 Long 0 0 ,First,#," + table + ",Crash_Death_Count,-1,-1;Crash_Severity 'Crash_Severity' true true false 8000 Text 0 0 ,First,#," + table + ",Crash_Severity,-1,-1;Crash_Time 'Crash_Time' true true false 4 Long 0 0 ,First,#," + table + ",Crash_Time,-1,-1;Crash_Year 'Crash_Year' true true false 4 Long 0 0 ,First,#," + table + ",Crash_Year,-1,-1;Day_of_Week 'Day_of_Week' true true false 8000 Text 0 0 ,First,#," + table + ",Day_of_Week,-1,-1;Latitude 'Latitude' true true false 8 Float 0 0 ,First,#," + table + ",Latitude,-1,-1;Longitude 'Longitude' true true false 8 Float 0 0 ,First,#," + table + ",Longitude,-1,-1;Charge 'Charge' true true false 8000 Text 0 0 ,First,#," + table + ",Charge,-1,-1")

        # Convert to XY points
        arcpy.MakeXYEventLayer_management("{0}_".format(table), "Longitude", "Latitude", "DWI_{0}".format(year),
                                          spatial_ref)
        arcpy.FeatureClassToFeatureClass_conversion("DWI_{0}".format(year), workspace, "DWIpoints_{0}".format(year))

        # Create master point fc
        if year == 2010:
            arcpy.CreateFeatureclass_management(workspace, "Master_DWIpoints", "POINT", "DWIpoints_{0}".format(year),
                                                spatial_reference=spatial_ref)
            arcpy.Append_management("DWIpoints_{0}".format(year), "Master_DWIpoints", "NO_TEST")
        else:
            arcpy.Append_management("DWIpoints_{0}".format(year), "Master_DWIpoints", "NO_TEST")
        # Delete records with duplicate CrashID
        arcpy.DeleteIdentical_management(in_dataset="Master_DWIpoints", fields="Crash_ID")

        arcpy.Delete_management("DWIpoints_{0}".format(year))
        # Clean up geodatabase
        arcpy.Delete_management(table)
        arcpy.Delete_management("{0}_".format(table))


convert_to_points()

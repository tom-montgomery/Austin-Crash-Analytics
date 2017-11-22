"""Prepares CRIS crash data extracts for use in GIS"""
import sys


import arcpy

# Using NAD 83 as coordinate system
spatial_ref = arcpy.SpatialReference(4269)
# Change data_years if you want to adjust scope of study
data_years = range(2010, 2018)

directory = sys.path[0]
arcpy.env.overwriteOutput = True
workspace = '{0}\\AustinCA.gdb'.format(directory)


def convert_to_points():
    """Parses query results from CRIS and converts to GIS point format. Exports single feature class for each year of TXDoT
    data."""

    # Creates geodatabase workspace if already does not exist
    if arcpy.Exists(workspace):
        pass
    else:
        arcpy.CreateFileGDB_management(directory, "AustinCA")
    arcpy.env.workspace = workspace

    for year in data_years:
        print "Prepping {0} data".format(year)
        csv = '{0}\\csv\\Travis{1}Crashes.csv'.format(directory, year)
        table = 'tbl{0}'.format(year)

        # Prep CSV by converting lat long to float and mapping fields. 
        # Remove fields from final output to omit.
        arcpy.TableToTable_conversion(in_rows=csv,
                                      out_path=workspace,
                                      out_name=table, where_clause="",
                                      field_mapping="Crash_ID 'Crash_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Crash_ID,-1,-1;Crash_Fatal_Fl 'Crash_Fatal_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Crash_Fatal_Fl,-1,-1;Cmv_Involv_Fl 'Cmv_Involv_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Cmv_Involv_Fl,-1,-1;Schl_Bus_Fl 'Schl_Bus_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Schl_Bus_Fl,-1,-1;Rr_Relat_Fl 'Rr_Relat_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rr_Relat_Fl,-1,-1;Medical_Advisory_Fl 'Medical_Advisory_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Medical_Advisory_Fl,-1,-1;Amend_Supp_Fl 'Amend_Supp_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Amend_Supp_Fl,-1,-1;Active_School_Zone_Fl 'Active_School_Zone_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Active_School_Zone_Fl,-1,-1;Crash_Date 'Crash_Date' true true false 8 Date 0 0 ,First,#," + csv +
                                                    ",Crash_Date,-1,-1;Crash_Time 'Crash_Time' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Crash_Time,-1,-1;Case_ID 'Case_ID' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Case_ID,-1,-1;Local_Use 'Local_Use' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Local_Use,-1,-1;Rpt_CRIS_Cnty_ID 'Rpt_CRIS_Cnty_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Rpt_CRIS_Cnty_ID,-1,-1;Rpt_City_ID 'Rpt_City_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Rpt_City_ID,-1,-1;Rpt_Outside_City_Limit_Fl 'Rpt_Outside_City_Limit_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Outside_City_Limit_Fl,-1,-1;Thousand_Damage_Fl 'Thousand_Damage_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Thousand_Damage_Fl,-1,-1;Rpt_Latitude 'Rpt_Latitude' true true false 8 Double 0 0 ,First,#," + csv +
                                                    ",Rpt_Latitude,-1,-1;Rpt_Longitude 'Rpt_Longitude' true true false 8 Double 0 0 ,First,#," + csv +
                                                    ",Rpt_Longitude,-1,-1;Rpt_Rdwy_Sys_ID 'Rpt_Rdwy_Sys_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Rpt_Rdwy_Sys_ID,-1,-1;Rpt_Hwy_Num 'Rpt_Hwy_Num' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Hwy_Num,-1,-1;Rpt_Hwy_Sfx 'Rpt_Hwy_Sfx' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Hwy_Sfx,-1,-1;Rpt_Road_Part_ID 'Rpt_Road_Part_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Rpt_Road_Part_ID,-1,-1;Rpt_Block_Num 'Rpt_Block_Num' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Block_Num,-1,-1;Rpt_Street_Pfx 'Rpt_Street_Pfx' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Street_Pfx,-1,-1;Rpt_Street_Name 'Rpt_Street_Name' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Street_Name,-1,-1;Rpt_Street_Sfx 'Rpt_Street_Sfx' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Street_Sfx,-1,-1;Private_Dr_Fl 'Private_Dr_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Private_Dr_Fl,-1,-1;Toll_Road_Fl 'Toll_Road_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Toll_Road_Fl,-1,-1;Crash_Speed_Limit 'Crash_Speed_Limit' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Crash_Speed_Limit,-1,-1;Road_Constr_Zone_Fl 'Road_Constr_Zone_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Road_Constr_Zone_Fl,-1,-1;Road_Constr_Zone_Wrkr_Fl 'Road_Constr_Zone_Wrkr_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Road_Constr_Zone_Wrkr_Fl,-1,-1;Rpt_Street_Desc 'Rpt_Street_Desc' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Street_Desc,-1,-1;At_Intrsct_Fl 'At_Intrsct_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",At_Intrsct_Fl,-1,-1;Rpt_Sec_Rdwy_Sys_ID 'Rpt_Sec_Rdwy_Sys_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Rpt_Sec_Rdwy_Sys_ID,-1,-1;Rpt_Sec_Hwy_Num 'Rpt_Sec_Hwy_Num' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Sec_Hwy_Num,-1,-1;Rpt_Sec_Hwy_Sfx 'Rpt_Sec_Hwy_Sfx' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Sec_Hwy_Sfx,-1,-1;Rpt_Sec_Road_Part_ID 'Rpt_Sec_Road_Part_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Rpt_Sec_Road_Part_ID,-1,-1;Rpt_Sec_Block_Num 'Rpt_Sec_Block_Num' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Sec_Block_Num,-1,-1;Rpt_Sec_Street_Pfx 'Rpt_Sec_Street_Pfx' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Sec_Street_Pfx,-1,-1;Rpt_Sec_Street_Name 'Rpt_Sec_Street_Name' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Sec_Street_Name,-1,-1;Rpt_Sec_Street_Sfx 'Rpt_Sec_Street_Sfx' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Sec_Street_Sfx,-1,-1;Rpt_Ref_Mark_Offset_Amt 'Rpt_Ref_Mark_Offset_Amt' true true false 8 Double 0 0 ,First,#," + csv +
                                                    ",Rpt_Ref_Mark_Offset_Amt,-1,-1;Rpt_Ref_Mark_Dist_Uom 'Rpt_Ref_Mark_Dist_Uom' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Ref_Mark_Dist_Uom,-1,-1;Rpt_Ref_Mark_Dir 'Rpt_Ref_Mark_Dir' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Ref_Mark_Dir,-1,-1;Rpt_Ref_Mark_Nbr 'Rpt_Ref_Mark_Nbr' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Ref_Mark_Nbr,-1,-1;Rpt_Sec_Street_Desc 'Rpt_Sec_Street_Desc' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_Sec_Street_Desc,-1,-1;Rpt_CrossingNumber 'Rpt_CrossingNumber' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Rpt_CrossingNumber,-1,-1;Wthr_Cond_ID 'Wthr_Cond_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Wthr_Cond_ID,-1,-1;Light_Cond_ID 'Light_Cond_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Light_Cond_ID,-1,-1;Entr_Road_ID 'Entr_Road_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Entr_Road_ID,-1,-1;Road_Type_ID 'Road_Type_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Road_Type_ID,-1,-1;Road_Algn_ID 'Road_Algn_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Road_Algn_ID,-1,-1;Surf_Cond_ID 'Surf_Cond_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Surf_Cond_ID,-1,-1;Traffic_Cntl_ID 'Traffic_Cntl_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Traffic_Cntl_ID,-1,-1;Investigat_Notify_Time 'Investigat_Notify_Time' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Investigat_Notify_Time,-1,-1;Investigat_Notify_Meth 'Investigat_Notify_Meth' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Investigat_Notify_Meth,-1,-1;Investigat_Arrv_Time 'Investigat_Arrv_Time' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Investigat_Arrv_Time,-1,-1;Report_Date 'Report_Date' true true false 8 Date 0 0 ,First,#," + csv +
                                                    ",Report_Date,-1,-1;Investigat_Comp_Fl 'Investigat_Comp_Fl' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Investigat_Comp_Fl,-1,-1;Investigator_Name 'Investigator_Name' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Investigator_Name,-1,-1;ID_Number 'ID_Number' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",ID_Number,-1,-1;ORI_Number 'ORI_Number' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",ORI_Number,-1,-1;Investigat_Agency_ID 'Investigat_Agency_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Investigat_Agency_ID,-1,-1;Investigat_Area_ID 'Investigat_Area_ID' true true false 4 Long 0 0 ,First,#," + csv +
                                                    ",Investigat_Area_ID,-1,-1;Investigat_District_ID 'Investigat_District_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Investigat_District_ID,-1,-1;Investigat_Region_ID 'Investigat_Region_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Investigat_Region_ID,-1,-1;Bridge_Detail_ID 'Bridge_Detail_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Bridge_Detail_ID,-1,-1;Harm_Evnt_ID 'Harm_Evnt_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Harm_Evnt_ID,-1,-1;Intrsct_Relat_ID 'Intrsct_Relat_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Intrsct_Relat_ID,-1,-1;FHE_Collsn_ID 'FHE_Collsn_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",FHE_Collsn_ID,-1,-1;Obj_Struck_ID 'Obj_Struck_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Obj_Struck_ID,-1,-1;Othr_Factr_ID 'Othr_Factr_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Othr_Factr_ID,-1,-1;Road_Part_Adj_ID 'Road_Part_Adj_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Road_Part_Adj_ID,-1,-1;Road_Cls_ID 'Road_Cls_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Road_Cls_ID,-1,-1;Road_Relat_ID 'Road_Relat_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Road_Relat_ID,-1,-1;Phys_Featr_1_ID 'Phys_Featr_1_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Phys_Featr_1_ID,-1,-1;Phys_Featr_2_ID 'Phys_Featr_2_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Phys_Featr_2_ID,-1,-1;Cnty_ID 'Cnty_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Cnty_ID,-1,-1;City_ID 'City_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",City_ID,-1,-1;Latitude 'Latitude' true true false 8 Float 0 0 ,First,#," + csv +
                                                    ",Latitude,-1,-1;Longitude 'Longitude' true true false 8 Float 0 0 ,First,#," + csv + 
                                                    ",Longitude,-1,-1;Hwy_Sys 'Hwy_Sys' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Hwy_Sys,-1,-1;Hwy_Nbr 'Hwy_Nbr' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Hwy_Nbr,-1,-1;Hwy_Sfx 'Hwy_Sfx' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Hwy_Sfx,-1,-1;Dfo 'Dfo' true true false 8 Double 0 0 ,First,#," + csv + 
                                                    ",Dfo,-1,-1;Street_Name 'Street_Name' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Street_Name,-1,-1;Street_Nbr 'Street_Nbr' true true false 250 Text 0 0 ,First,#," + csv +
                                                    ",Street_Nbr,-1,-1;Control 'Control' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Control,-1,-1;Section 'Section' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Section,-1,-1;Milepoint 'Milepoint' true true false 8 Double 0 0 ,First,#," + csv + 
                                                    ",Milepoint,-1,-1;Ref_Mark_Nbr 'Ref_Mark_Nbr' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Ref_Mark_Nbr,-1,-1;Ref_Mark_Displ 'Ref_Mark_Displ' true true false 8 Double 0 0 ,First,#," + csv + 
                                                    ",Ref_Mark_Displ,-1,-1;Hwy_Sys_2 'Hwy_Sys_2' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Hwy_Sys_2,-1,-1;Hwy_Nbr_2 'Hwy_Nbr_2' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Hwy_Nbr_2,-1,-1;Hwy_Sfx_2 'Hwy_Sfx_2' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Hwy_Sfx_2,-1,-1;Street_Name_2 'Street_Name_2' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Street_Name_2,-1,-1;Street_Nbr_2 'Street_Nbr_2' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Street_Nbr_2,-1,-1;Control_2 'Control_2' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Control_2,-1,-1;Section_2 'Section_2' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Section_2,-1,-1;Milepoint_2 'Milepoint_2' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Milepoint_2,-1,-1;Txdot_Rptable_Fl 'Txdot_Rptable_Fl' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Txdot_Rptable_Fl,-1,-1;Onsys_Fl 'Onsys_Fl' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Onsys_Fl,-1,-1;Rural_Fl 'Rural_Fl' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Rural_Fl,-1,-1;Crash_Sev_ID 'Crash_Sev_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Crash_Sev_ID,-1,-1;Pop_Group_ID 'Pop_Group_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Pop_Group_ID,-1,-1;Located_Fl 'Located_Fl' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Located_Fl,-1,-1;Day_of_Week 'Day_of_Week' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Day_of_Week,-1,-1;Hwy_Dsgn_Lane_ID 'Hwy_Dsgn_Lane_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Hwy_Dsgn_Lane_ID,-1,-1;Hwy_Dsgn_Hrt_ID 'Hwy_Dsgn_Hrt_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Hwy_Dsgn_Hrt_ID,-1,-1;Hp_Shldr_Left 'Hp_Shldr_Left' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Hp_Shldr_Left,-1,-1;Hp_Shldr_Right 'Hp_Shldr_Right' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Hp_Shldr_Right,-1,-1;Hp_Median_Width 'Hp_Median_Width' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Hp_Median_Width,-1,-1;Base_Type_ID 'Base_Type_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Base_Type_ID,-1,-1;Nbr_Of_Lane 'Nbr_Of_Lane' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Nbr_Of_Lane,-1,-1;Row_Width_Usual 'Row_Width_Usual' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Row_Width_Usual,-1,-1;Roadbed_Width 'Roadbed_Width' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Roadbed_Width,-1,-1;Surf_Width 'Surf_Width' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Surf_Width,-1,-1;Surf_Type_ID 'Surf_Type_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Surf_Type_ID,-1,-1;Curb_Type_Left_ID 'Curb_Type_Left_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Curb_Type_Left_ID,-1,-1;Curb_Type_Right_ID 'Curb_Type_Right_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Curb_Type_Right_ID,-1,-1;Shldr_Type_Left_ID 'Shldr_Type_Left_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Shldr_Type_Left_ID,-1,-1;Shldr_Width_Left 'Shldr_Width_Left' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Shldr_Width_Left,-1,-1;Shldr_Use_Left_ID 'Shldr_Use_Left_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Shldr_Use_Left_ID,-1,-1;Shldr_Type_Right_ID 'Shldr_Type_Right_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Shldr_Type_Right_ID,-1,-1;Shldr_Width_Right 'Shldr_Width_Right' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Shldr_Width_Right,-1,-1;Shldr_Use_Right_ID 'Shldr_Use_Right_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Shldr_Use_Right_ID,-1,-1;Median_Type_ID 'Median_Type_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Median_Type_ID,-1,-1;Median_Width 'Median_Width' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Median_Width,-1,-1;Rural_Urban_Type_ID 'Rural_Urban_Type_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Rural_Urban_Type_ID,-1,-1;Func_Sys_ID 'Func_Sys_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Func_Sys_ID,-1,-1;Adt_Curnt_Amt 'Adt_Curnt_Amt' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Adt_Curnt_Amt,-1,-1;Adt_Curnt_Year 'Adt_Curnt_Year' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Adt_Curnt_Year,-1,-1;Adt_Adj_Curnt_Amt 'Adt_Adj_Curnt_Amt' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Adt_Adj_Curnt_Amt,-1,-1;Pct_Single_Trk_Adt 'Pct_Single_Trk_Adt' true true false 8 Double 0 0 ,First,#," + csv + 
                                                    ",Pct_Single_Trk_Adt,-1,-1;Pct_Combo_Trk_Adt 'Pct_Combo_Trk_Adt' true true false 8 Double 0 0 ,First,#," + csv + 
                                                    ",Pct_Combo_Trk_Adt,-1,-1;Trk_Aadt_Pct 'Trk_Aadt_Pct' true true false 8 Double 0 0 ,First,#," + csv + 
                                                    ",Trk_Aadt_Pct,-1,-1;Curve_Type_ID 'Curve_Type_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Curve_Type_ID,-1,-1;Curve_Lngth 'Curve_Lngth' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Curve_Lngth,-1,-1;Cd_Degr 'Cd_Degr' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Cd_Degr,-1,-1;Delta_Left_Right_ID 'Delta_Left_Right_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Delta_Left_Right_ID,-1,-1;Dd_Degr 'Dd_Degr' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Dd_Degr,-1,-1;Feature_Crossed 'Feature_Crossed' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Feature_Crossed,-1,-1;Structure_Number 'Structure_Number' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Structure_Number,-1,-1;I_R_Min_Vert_Clear 'I_R_Min_Vert_Clear' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",I_R_Min_Vert_Clear,-1,-1;Approach_Width 'Approach_Width' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Approach_Width,-1,-1;Bridge_Median_ID 'Bridge_Median_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Bridge_Median_ID,-1,-1;Bridge_Loading_Type_ID 'Bridge_Loading_Type_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Bridge_Loading_Type_ID,-1,-1;Bridge_Loading_In_1000_Lbs 'Bridge_Loading_In_1000_Lbs' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Bridge_Loading_In_1000_Lbs,-1,-1;Bridge_Srvc_Type_On_ID 'Bridge_Srvc_Type_On_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Bridge_Srvc_Type_On_ID,-1,-1;Bridge_Srvc_Type_Under_ID 'Bridge_Srvc_Type_Under_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Bridge_Srvc_Type_Under_ID,-1,-1;Culvert_Type_ID 'Culvert_Type_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Culvert_Type_ID,-1,-1;Roadway_Width 'Roadway_Width' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Roadway_Width,-1,-1;Deck_Width 'Deck_Width' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Deck_Width,-1,-1;Bridge_Dir_Of_Traffic_ID 'Bridge_Dir_Of_Traffic_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Bridge_Dir_Of_Traffic_ID,-1,-1;Bridge_Rte_Struct_Func_ID 'Bridge_Rte_Struct_Func_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Bridge_Rte_Struct_Func_ID,-1,-1;Bridge_IR_Struct_Func_ID 'Bridge_IR_Struct_Func_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Bridge_IR_Struct_Func_ID,-1,-1;CrossingNumber 'CrossingNumber' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",CrossingNumber,-1,-1;RRCo 'RRCo' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",RRCo,-1,-1;Poscrossing_ID 'Poscrossing_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Poscrossing_ID,-1,-1;WDCode_ID 'WDCode_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",WDCode_ID,-1,-1;Standstop 'Standstop' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Standstop,-1,-1;Yield 'Yield' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Yield,-1,-1;Incap_Injry_Cnt 'Incap_Injry_Cnt' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Incap_Injry_Cnt,-1,-1;Nonincap_Injry_Cnt 'Nonincap_Injry_Cnt' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Nonincap_Injry_Cnt,-1,-1;Poss_Injry_Cnt 'Poss_Injry_Cnt' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Poss_Injry_Cnt,-1,-1;Non_Injry_Cnt 'Non_Injry_Cnt' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Non_Injry_Cnt,-1,-1;Unkn_Injry_Cnt 'Unkn_Injry_Cnt' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Unkn_Injry_Cnt,-1,-1;Tot_Injry_Cnt 'Tot_Injry_Cnt' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Tot_Injry_Cnt,-1,-1;Death_Cnt 'Death_Cnt' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",Death_Cnt,-1,-1;MPO_ID 'MPO_ID' true true false 4 Long 0 0 ,First,#," + csv + 
                                                    ",MPO_ID,-1,-1;Investigat_Service_ID 'Investigat_Service_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Investigat_Service_ID,-1,-1;Investigat_DA_ID 'Investigat_DA_ID' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Investigat_DA_ID,-1,-1;Investigator_Narrative 'Investigator_Narrative' true true false 250 Text 0 0 ,First,#," + csv + 
                                                    ",Investigator_Narrative,-1,-1")

        # Convert to XY points
        arcpy.MakeXYEventLayer_management("{0}".format(table), "Longitude", "Latitude", "Crash_{0}".format(year),
                                          spatial_ref)
        arcpy.FeatureClassToFeatureClass_conversion("Crash_{0}".format(year), workspace, "CrashPoints_{0}".format(year))

        # Create master point fc
        if year == 2010:
            arcpy.CreateFeatureclass_management(workspace, "CrashPointsMaster", "POINT", "CrashPoints_{0}".format(year),
                                                spatial_reference=spatial_ref)
            arcpy.Append_management("CrashPoints_{0}".format(year), "CrashPointsMaster", "NO_TEST")
        else:
            arcpy.Append_management("CrashPoints_{0}".format(year), "CrashPointsMaster", "NO_TEST")
        # Delete records with duplicate CrashID
        arcpy.DeleteIdentical_management(in_dataset="CrashPointsMaster", fields="Crash_ID")

        arcpy.Delete_management("CrashPoints_{0}".format(year))

        # Clean up geodatabase
        arcpy.Delete_management(table)
        arcpy.Delete_management("{0}_".format(table))


def clean_fields():
    """Removes unwanted fields from GIS point data. If all CRIS fields are desired in output do not use this function.
    Use wanted_fields list to select which fields are wanted in final output. ObjectID and Shape must be included."""
    wanted_fields = ['Crash_ID',
                     'Crash_Date',
                     'Crash_Time',
                     'Latitude',
                     'Longitude',
                     'Wthr_Cond_ID',
                     'Death_Cnt',
                     'Crash_Sev_ID',
                     'Crash_Speed_Limit',
                     'Tot_Injry_Cnt',
                     'OBJECTID',
                     'Shape']

    fields = arcpy.ListFields("CrashPointsMaster")
    for field in fields:
        if field.name in wanted_fields:
            pass
        else:
            print "Removing {0}".format(field.name)
            arcpy.DeleteField_management("CrashPointsMaster", field.name)


convert_to_points()
clean_fields()
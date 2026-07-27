from UWG import UWG
from PostProcess2Serial import PostProcess2Serial
import os

# Define the .epw, .uwg filenames to create an UWG object.
# UWG will look for the .epw file in the UWG/resources/epw folder,
# and the .uwg file in the UWG/resources/parameters folder.

epw_filename = "ERA5_Toronto_2022"
param_filename_1 = "initialize_Toronto_Base_1.uwg"         # .uwg file name
param_filename_2 = "initialize_Toronto_Base_2.uwg"         # .uwg file name
param_filename_3 = "initialize_Toronto_Base_3.uwg"         # .uwg file name
param_filename_4 = "initialize_Toronto_Base_4.uwg"         # .uwg file name
param_filename_5 = "initialize_Toronto_Base_5.uwg"         # .uwg file name
param_filename_6 = "initialize_Toronto_Base_6.uwg"         # .uwg file name
param_filename_7 = "initialize_Toronto_Base_7.uwg"         # .uwg file name
param_filename_8 = "initialize_Toronto_Base_8.uwg"         # .uwg file name
param_filename_9 = "initialize_Toronto_Base_9.uwg"         # .uwg file name
param_filename_10 = "initialize_Toronto_Base_10.uwg"         # .uwg file name
param_filename_11 = "initialize_Toronto_Base_11.uwg"         # .uwg file name
param_filename_12 = "initialize_Toronto_Base_12.uwg"         # .uwg file name

case_name = "Toronto_Base_2022"

# Initialize the UWG object and run the simulation

uwg = UWG(epw_filename, param_filename_1,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-Jan.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-Jan.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-Jan.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-Jan.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-Jan.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-Jan.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-Jan.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-Jan.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-Jan.txt")

uwg = UWG(epw_filename, param_filename_2,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-Feb.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-Feb.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-Feb.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-Feb.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-Feb.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-Feb.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-Feb.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-Feb.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-Feb.txt")

uwg = UWG(epw_filename, param_filename_3,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-Mar.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-Mar.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-Mar.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-Mar.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-Mar.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-Mar.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-Mar.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-Mar.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-Mar.txt")

uwg = UWG(epw_filename, param_filename_4,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-Apr.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-Apr.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-Apr.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-Apr.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-Apr.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-Apr.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-Apr.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-Apr.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-Apr.txt")

uwg = UWG(epw_filename, param_filename_5,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-May.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-May.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-May.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-May.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-May.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-May.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-May.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-May.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-May.txt")

uwg = UWG(epw_filename, param_filename_6,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-Jun.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-Jun.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-Jun.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-Jun.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-Jun.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-Jun.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-Jun.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-Jun.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-Jun.txt")

uwg = UWG(epw_filename, param_filename_7,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-Jul.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-Jul.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-Jul.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-Jul.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-Jul.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-Jul.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-Jul.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-Jul.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-Jul.txt")

uwg = UWG(epw_filename, param_filename_8,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-Aug.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-Aug.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-Aug.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-Aug.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-Aug.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-Aug.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-Aug.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-Aug.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-Aug.txt")

uwg = UWG(epw_filename, param_filename_9,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-Sep.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-Sep.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-Sep.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-Sep.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-Sep.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-Sep.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-Sep.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-Sep.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-Sep.txt")

uwg = UWG(epw_filename, param_filename_10,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-Oct.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-Oct.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-Oct.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-Oct.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-Oct.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-Oct.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-Oct.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-Oct.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-Oct.txt")

uwg = UWG(epw_filename, param_filename_11,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-Nov.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-Nov.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-Nov.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-Nov.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-Nov.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-Nov.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-Nov.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-Nov.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-Nov.txt")

uwg = UWG(epw_filename, param_filename_12,'','','','')
uwg.run()
PostProcess2Serial(2, "Output/Perf-Metrics-"+case_name+"-Dec.txt")
os.rename("Output/BEM_hourly.txt", "Output/BEM_hourly-"+case_name+"-Dec.txt")
os.rename("Output/q_profiles_hourly.txt", "Output/q_profiles_hourly-"+case_name+"-Dec.txt")
os.rename("Output/Tepw_hourly.txt", "Output/Tepw_hourly-"+case_name+"-Dec.txt")
os.rename("Output/TKE_profiles_hourly.txt", "Output/TKE_profiles_hourly-"+case_name+"-Dec.txt")
os.rename("Output/Tr_profiles_hourly.txt", "Output/Tr_profiles_hourly-"+case_name+"-Dec.txt")
os.rename("Output/Tu_profiles_hourly.txt", "Output/Tu_profiles_hourly-"+case_name+"-Dec.txt")
os.rename("Output/U_profiles_hourly.txt", "Output/U_profiles_hourly-"+case_name+"-Dec.txt")
os.rename("Output/V_profiles_hourly.txt", "Output/V_profiles_hourly-"+case_name+"-Dec.txt")




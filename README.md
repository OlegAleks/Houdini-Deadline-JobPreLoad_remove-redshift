# Houdini-Deadline-JobPreLoad_remove-redshift
Was made for PostPro18 studio by Oleg Alekseev 15 Junuary 2019

1. Copy "JobPreLoad.py" to your DeadlineRepo/plugins/Houdini/
2. Copy "remove_redshift_nodes.py" to script folder, make sure it is visible from $HOUDINI_SCRIPT_PATH variable

Deadline executes "JobPreLoad.py" script on a slave machine. The script opens submitted scene with hython.exe and runs "remove_redshift_nodes.py" 

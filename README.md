# Houdini-Deadline-JobPreLoad_remove-redshift
# Made for PostPro18 studio by Oleg Alekseev 15 Junuary 2019

1. Copy "JobPreLoad.py" to your DeadlineRepo/plugins/Houdini
2. Copy "remove_redshift_nodes.py" to script folder, make sure it visible from $HOUDINI_SCRIPT_PATH variable

"JobPreLoad.py" executes by Deadline on a slave machine. It opens submitted scene with hython.exe and runs "remove_redshift_nodes.py" 

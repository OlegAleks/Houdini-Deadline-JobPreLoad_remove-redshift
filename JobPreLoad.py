from System import *
from System.IO import *
from Deadline.Scripting import *
import os, sys
from subprocess import Popen, PIPE
def __main__(deadlinePlugin):
	job = deadlinePlugin.GetJob()
	slaveName = deadlinePlugin.GetSlaveName()
	cpu_farm = ['RENDER9', 'RENDER10', 'RENDER11', 'RENDER12', 'RENDER13', 'RENDER14', 'RENDER15']
	if slaveName in cpu_farm:
		deadlinePlugin.LogInfo("************START UBERSCRIPT***********")
		hip = deadlinePlugin.GetDataFilename()
		deadlinePlugin.LogInfo("file name: %s" % hip)
		houdiniExeList = deadlinePlugin.GetConfigEntry("Houdini16_5_Hython_Executable")
		hythonExe = ""
		if SystemUtils.IsRunningOnWindows():
			hythonExe = FileUtils.SearchFileListFor64Bit( houdiniExeList )
		if hythonExe == "":
			hythonExe = FileUtils.SearchFileList( houdiniExeList )
		if SystemUtils.IsRunningOnLinux():
			hythonExe = hythonExe.replace( "hython-bin", "hython" )
		deadlinePlugin.LogInfo("hyhtonExe: %s" % hythonExe)
		hython_cmd = "hip = r\"" + hip + "\"\n"
		hython_cmd += "try:\n\thou.hipFile.load(hip)\n"
		hython_cmd += "except:\n\tprint 'skip warnings'\n\n"
		hython_cmd += "import remove_redshift_nodes as a\na.remove()\n"
		hython_cmd += "hou.hipFile.save()"
		h_proc = Popen([hythonExe], stdin=PIPE, stdout=PIPE, stderr=PIPE)
		(out, err) = h_proc.communicate(hython_cmd)
		deadlinePlugin.LogInfo("subprocess out: %s" % out)
		deadlinePlugin.LogInfo("subprocess errors: %s" % err)
		deadlinePlugin.LogInfo("************FINISH UBERSCRIPT***********")
	else:
		deadlinePlugin.LogInfo("************SKIP UBERSCRIPT***********")

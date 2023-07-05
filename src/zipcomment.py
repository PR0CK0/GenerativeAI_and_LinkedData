import zipfile

zipname = "demo.zip"
filename = "hide_data.py"
comment = b"Initial attempt at creating this hack, didn't realize a better interface existed"

with zipfile.ZipFile(zipname, "w") as zfile:
	zfile.write(filename)
	zfile.getinfo(filename).comment = comment

with zipfile.ZipFile(zipname, "r") as zfile:
	assert zfile.getinfo(filename).comment == comment

print("if you got here it worked...")
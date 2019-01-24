# Patcher

import delimlib # Get this from https://github.com/chanonlim/customlibs
import fire

no_patch = ['OriginFile']
__version__ = "v1.0.0"
__author__ = "SuperNiintendo"

class PatchNotIntendedError(Exception):
    pass

def list_exists(index, list):
    try:
        list[index]
    except IndexError:
        return False
    else:
        return True
    
def _make_patch(string1, string2):
    stringlist = string1.split("\n")
    stringlist2 = string2.split("\n")
    output = []
    for (count, i) in enumerate(stringlist2):
        if not list_exists(count, stringlist):
            output.append(str(count + 1) + ": " + i)
            stringlist.insert(count, i)
        if i == stringlist[count]:
            continue
        else:
            output.append(str(count + 1) + ": " + i)
    for (count, i) in enumerate(stringlist):
        if not list_thing_exists(i, stringlist2) and list_thing_exists(i, stringlist):
            output.append(str(count + 1) + ": DEL")
    output[:] = [f for f in output if f != ""]
    return "\n".join(output)

def _patch(filedata, patchdata):
    patchinfo = delimlib.parse(patchdata, ": ")
    filelist = filedata.split("\n")
    for k, v in patchinfo.items():
        if k in no_patch:
            continue
        else:
            if v == "DEL":
                filelist.pop(int(k) - 1)
            else:
                if list_exists(int(k) - 1, filelist):
                    filelist[int(k) - 1] = v
                else:
                    filelist.insert(int(k) - 1, v)
    return "\n".join(filelist)

def make_patch_file(file1, file2, patchfile):
    patchstring = _make_patch(open(file1).read(), open(file2).read()).split("\n")
    patchstring.append("OriginFile: " + file1)
    open(patchfile, 'w+').write("\n".join(patchstring))

def patch(file, patchfile):
    patchdata = open(patchfile).read()
    patchinfo = delimlib.parse(patchdata, ": ")
    if file != patchinfo["OriginFile"]:
        raise PatchNotIntendedError("OriginFile does not match")
    else:
        patched = _patch(open(file).read(), patchdata)
        open(file, 'w+').write(patched)

class CmdTools:
    def patch(this, file, patchfile):
        patch(file, patchfile)
    def make(this, file1, file2, patchfile):
        make_patch_file(file1, file2, patchfile)
    def version(this):
        print(__version__)

if __name__ == "__main__":
    fire.Fire(CmdTools)

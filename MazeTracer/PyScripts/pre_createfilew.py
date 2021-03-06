import ctypes
import json

def pre_analyzer(LPCTSTR_lpFileName,
                 DWORD_dwDesiredAccess,
                 DWORD_dwShareMode,
                 LPSECURITY_ATTRIBUTES_lpSecurityAttributes,
                 DWORD_dwCreationDisposition,
                 DWORD_dwFlagsAndAttributes,
                 HANDLE_hTemplateFile,
                 **kwargs):

    FileName = ctypes.c_wchar_p.from_address(LPCTSTR_lpFileName)
    res = []
    if (FileName and FileName.value):
        result = {'name': 'lpFileName', 'data': FileName.value}
        res.append(result)
    return json.dumps(res)

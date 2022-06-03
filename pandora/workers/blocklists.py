from typing import Tuple

from ..helpers import Status
from ..task import Task
from ..report import Report

from .base import BaseWorker


# list from: https://github.com/CIRCL/PyCIRCLean/blob/main/filecheck/filecheck.py#L74

malicious_exts: Tuple[str, ...] = (
    # Applications
    ".exe", ".pif", ".application", ".gadget", ".msi", ".msp", ".com", ".scr",
    ".hta", ".cpl", ".msc", ".jar",
    # Scripts
    ".bat", ".cmd", ".vb", ".vbs", ".vbe", ".js", ".jse", ".ws", ".wsf",
    ".wsc", ".wsh", ".ps1", ".ps1xml", ".ps2", ".ps2xml", ".psc1", ".psc2",
    ".msh", ".msh1", ".msh2", ".mshxml", ".msh1xml", ".msh2xml",
    # Shortcuts
    ".scf", ".lnk", ".inf",
    # Other
    ".reg", ".dll",
    # Office macro (OOXML with macro enabled)
    ".docm", ".dotm", ".xlsm", ".xltm", ".xlam", ".pptm", ".potm", ".ppam",
    ".ppsm", ".sldm",
    # banned from wirecode
    ".asf", ".asx", ".au", ".htm", ".html", ".mht", ".vbs",
    ".wax", ".wm", ".wma", ".wmd", ".wmv", ".wmx", ".wmz", ".wvx",
    # Google chrome malicious extensions
    ".ad", ".ade", ".adp", ".ah", ".apk", ".app", ".application", ".asp",
    ".asx", ".bas", ".bash", ".bat", ".cfg", ".chi", ".chm", ".class",
    ".cmd", ".com", ".command", ".crt", ".crx", ".csh", ".deb", ".dex",
    ".dll", ".drv", ".exe", ".fxp", ".grp", ".hlp", ".hta", ".htm", ".html",
    ".htt", ".inf", ".ini", ".ins", ".isp", ".jar", ".jnlp", ".user.js",
    ".js", ".jse", ".ksh", ".lnk", ".local", ".mad", ".maf", ".mag", ".mam",
    ".manifest", ".maq", ".mar", ".mas", ".mat", ".mau", ".mav", ".maw",
    ".mda", ".mdb", ".mde", ".mdt", ".mdw", ".mdz", ".mht", ".mhtml", ".mmc",
    ".mof", ".msc", ".msh", ".mshxml", ".msi", ".msp", ".mst", ".ocx", ".ops",
    ".pcd", ".pif", ".pkg", ".pl", ".plg", ".prf", ".prg", ".pst", ".py",
    ".pyc", ".pyw", ".rb", ".reg", ".rpm", ".scf", ".scr", ".sct", ".sh",
    ".shar", ".shb", ".shs", ".shtm", ".shtml", ".spl", ".svg", ".swf", ".sys",
    ".tcsh", ".url", ".vb", ".vbe", ".vbs", ".vsd", ".vsmacros", ".vss",
    ".vst", ".vsw", ".ws", ".wsc", ".wsf", ".wsh", ".xbap", ".xht", ".xhtm",
    ".xhtml", ".xml", ".xsl", ".xslt", ".website", ".msh1", ".msh2", ".msh1xml",
    ".msh2xml", ".ps1", ".ps1xml", ".ps2", ".ps2xml", ".psc1", ".psc2", ".xnk",
    ".appref-ms", ".gadget", ".efi", ".fon", ".partial", ".svg", ".xml",
    ".xrm_ms", ".xsl", ".action", ".bin", ".inx", ".ipa", ".isu", ".job",
    ".out", ".pad", ".paf", ".rgs", ".u3p", ".vbscript", ".workflow", ".001",
    ".ace", ".arc", ".arj", ".b64", ".balz", ".bhx", ".cab", ".cpio", ".fat",
    ".hfs", ".hqx", ".iso", ".lha", ".lpaq1", ".lpaq5", ".lpaq8", ".lzh",
    ".mim", ".ntfs", ".paq8f", ".paq8jd", ".paq8l", ".paq8o", ".pea", ".quad",
    ".r00", ".r01", ".r02", ".r03", ".r04", ".r05", ".r06", ".r07", ".r08",
    ".r09", ".r10", ".r11", ".r12", ".r13", ".r14", ".r15", ".r16", ".r17",
    ".r18", ".r19", ".r20", ".r21", ".r22", ".r23", ".r24", ".r25", ".r26",
    ".r27", ".r28", ".r29", ".squashfs", ".swm", ".tpz", ".txz", ".tz", ".udf",
    ".uu", ".uue", ".vhd", ".vmdk", ".wim", ".wrc", ".xar", ".xxe", ".z",
    ".zipx", ".zpaq", ".cdr", ".dart", ".dc42", ".diskcopy42", ".dmg",
    ".dmgpart", ".dvdr", ".img", ".imgpart", ".ndif", ".smi", ".sparsebundle",
    ".sparseimage", ".toast", ".udif",
)


class Blocklists(BaseWorker):

    def analyse(self, task: Task, report: Report):
        report.status = Status.NOTAPPLICABLE
        ext = task.file.original_filename.rsplit(".", 1)[-1]
        if f'.{ext}' in malicious_exts:
            report.status = Status.ALERT
            report.add_details('Warning', f'The extension {ext} is considered as malicious by default.')

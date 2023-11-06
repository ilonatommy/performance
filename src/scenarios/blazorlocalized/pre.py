'''
pre-command
'''
import sys, os, subprocess
from performance.logger import setup_loggers
from shared import const
from shared.precommands import PreCommands
from test import EXENAME

setup_loggers(True)
precommands = PreCommands()
# For blazor3.2 the linker argument '--dump-dependencies' should be added statically to enable linker dump
# For blazor5.0 the linker argument can be added to the command line as an msbuild property
if precommands.framework == 'net6.0' or precommands.framework == 'net7.0':
    precommands.uninstall_workload("wasm-tools")
else:
    precommands.uninstall_workload("microsoft-net-sdk-blazorwebassembly-aot")
precommands.existing("src", "BlazorLocalized.sln")
# ensure that we don't use relinking
precommands.execute(['-p:WasmNativeWorkload=false'])

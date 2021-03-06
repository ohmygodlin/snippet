import angr
import claripy

def main():
	proj = angr.Project('./baby-re',  load_options={'auto_load_libs': False})

	# let's provide the exact variables received through the scanf so we don't have to worry about parsing stdin into a bunch of ints.
	flag_chars = [claripy.BVS('flag_%d' % i, 32) for i in xrange(13)]
	class my_scanf(angr.SimProcedure):
		def run(self, fmt, ptr):
			if 'scanf_count' not in self.state.globals:
				self.state.globals['scanf_count'] = 0
			c = self.state.globals['scanf_count']
			self.state.mem[ptr].dword = flag_chars[c]
			self.state.globals['scanf_count'] = c + 1
	proj.hook_symbol('__isoc99_scanf', my_scanf(), replace=True)

	sm = proj.factory.simgr()

	# search for just before the printf("%c%c...")
	# If we get to 0x402941, "Wrong" is going to be printed out, so definitely avoid that.
	sm.explore(find=0x4028E9, avoid=0x402941)

	# evaluate each of the flag chars against the constraints on the found state to construct the flag
	flag = ''.join(chr(sm.one_found.solver.eval(c)) for c in flag_chars)
	return flag
  
def main1():
  proj = angr.Project('./baby-re',  load_options={'auto_load_libs': False})
  simgr = proj.factory.simgr()
  simgr.explore(find=0x40294b, avoid=0x402941)
  print simgr.found[0].state.posix.dumps(0)
  return simgr.found[0].state.posix.dumps(1)

def test():
	assert main() == 'Math is hard!'

if __name__ == '__main__':
	print(repr(main()))
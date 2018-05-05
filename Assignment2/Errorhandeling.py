# Error Handeling
import testmain
import time

start = time.time()
testmain.test('mrdoesnotexit',2)
end = time.time()

print(end-start)

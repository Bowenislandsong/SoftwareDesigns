# stress Test
import testmain
import time

start = time.time()
testmain.test('etcwilde',50)
end = time.time()
print(end-start)

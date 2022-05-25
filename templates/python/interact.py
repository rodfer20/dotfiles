import interact


process = interact.Process()
data = process.readuntil("data to stop reading at")
process.sendline("send data")



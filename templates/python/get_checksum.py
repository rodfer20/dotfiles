def get_md5sum(filename)
    cmd = f"md5sum {filename} | cut -b -32".split(" ")
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output = proc.stdout.read()
    return output


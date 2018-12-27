import subprocess as s


result = s.run(
    ["python", "../trans_punc.py"],
    input="，。；“”‘’—？！《》".encode('gbk'),
    stdout=s.PIPE
)

assert result.stdout.decode() == ',.;""\'\'--?!<>'

import os
from datetime import datetime

images = ['gab_sq.jpg']

styles = ['xmas_pointillism.jpeg', 'monet_sq.jpg']

images = [os.path.join('images', 'input', i) for i in images]
styles = [os.path.join('images', 'style', s) for s in styles]

for i in images:
    assert os.path.isfile(i)

for s in styles:
    assert os.path.isfile(s)

settings = [
    ["--iterations", str(2000)],
    ["--iterations", str(3000)],
    ["--iterations", str(4000)],
    ["--iterations", str(2000), "--content-weight-blend", str(0.1)],
    ["--iterations", str(2000), "--content-weight-blend", str(0.5)],
    ["--iterations", str(2000), "--content-weight-blend", str(0.9)],
    ["--iterations", str(2000), "--style-layer-weight-exp", str(0.2)],
    ["--iterations", str(2000), "--style-layer-weight-exp", str(1.0)],
    ["--iterations", str(2000), "--style-layer-weight-exp", str(2.0)],
    ["--iterations", str(3000), "--content-weight-blend", str(0.1)],
    ["--iterations", str(3000), "--content-weight-blend", str(0.5)],
    ["--iterations", str(3000), "--content-weight-blend", str(0.9)],
    ["--iterations", str(3000), "--style-layer-weight-exp", str(0.2)],
    ["--iterations", str(3000), "--style-layer-weight-exp", str(1.0)],
    ["--iterations", str(3000), "--style-layer-weight-exp", str(2.0)]
]

idx = 0

for i in images:

    for s in styles:

        idx += 1

        for sett in settings:

            timestamp = datetime.timestamp(datetime.now())
            outfile = 'images/output/' + str(timestamp) + "_" + str(idx) + '.jpg'
            command = ['python', 'neural_style.py', '--content', i, '--output', outfile]
            ssstyles = ['--styles'] + [s]
            comm_string = ' '.join(command + sett + ssstyles)
            print(comm_string)
            os.system(comm_string)

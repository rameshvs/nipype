# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino.convert import Shredder

def test_Shredder_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    chunksize=dict(argstr='%d',
    position=2,
    units='NA',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='< %s',
    mandatory=True,
    position=-2,
    ),
    offset=dict(argstr='%d',
    position=1,
    units='NA',
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    space=dict(argstr='%d',
    position=3,
    units='NA',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = Shredder.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Shredder_outputs():
    output_map = dict(shredded=dict(),
    )
    outputs = Shredder.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value


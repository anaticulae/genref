# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import genex
import power

import genref


def test_generator_run(td):
    power.setup(genref.ROOT)
    files = [
        power.TECH019_PDF,
    ]
    genex.extract(
        files=files,
        dest=td.tmpdir,
        full=True,
    )

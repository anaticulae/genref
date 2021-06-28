# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import genex
import power

import genref


def test_generator_run(testdir):
    power.setup(genref.ROOT)
    files = [power.TECH019_PDF, power.REPOSITORY]
    genex.extract(
        files=files,
        destination=testdir.tmpdir,
        full=True,
    )

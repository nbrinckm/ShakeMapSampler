#!/usr/bin/env python3

# Copyright © 2021-2022 Helmholtz Centre Potsdam GFZ German Research Centre for
# Geosciences, Potsdam, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""
This is the Shakemap-Sampler-Service.

"""

import argparse
import glob
import os

import sampler



def main():
    """
    Runs the main method, which reads from
    the files,
    updates each exposure cell individually
    and prints out all of the updated exposure cells.
    """
    argparser = argparse.ArgumentParser(
        description="Computes one random sample of ground motion "

    )
    argparser.add_argument(
        "--intensity_file",
        help="File with hazard intensities, for example a shakemap",
    )
    argparser.add_argument("--intensity_output_file", help="Output file with the randomly sampled ground motion")
    argparser.add_argument(
        "--random_seed",
        help="The random seed, for reproducibility",
    )
   
    current_dir = os.path.dirname(os.path.realpath(__file__))


    args = argparser.parse_args()



    sampler.generate_random_shakemap_uncorrelated(args.intensity_file, args.intensity_output_file, args.random_seed)




if __name__ == "__main__":
    main()

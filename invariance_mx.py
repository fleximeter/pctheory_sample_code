"""
File: invariance_mx.py
Author: Jeff Martin
Description: A sample program for generating invariance matrices using pctheory

Copyright © 2022 by Jeff Martin. All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import pctheory.pcseg as pcseg
import pctheory.pcset as pcset
import pctheory.pitch as pitch
import pctheory.transformations as transformations

if __name__ == "__main__":
    # Gets all row operators. This is often a useful thing to do at the start of a 
    # program that involves working with ordered pitch-classes.
    ro = transformations.get_otos12()

    # An array with each of the twelve pitch-classes; the pitch-class numbers
    # align with the index in the array. A convenient way to refer to any pitch-class.
    pc = [pitch.PitchClass12(i) for i in range(12)]

    # Create a random twelve-tone row. This is a twelve-note nonduplicative pcseg.
    # We will arbitrarily use 0 for the starting pitch.
    row1 = pcseg.generate_random_pcseg12(12, True, 0)

    # Out of curiosity, we'll go ahead and output the row, as well as its interval succession
    # and a list of imbricated trichords. We'll also get the set-classes of the two hexachords 
    # that make up the row.
    print(f"Row: {row1}")
    print(f"Intervals: {pcseg.get_intervals(row1)}")
    print(f"Imbricated trichords: {pcseg.imb_n(row1, 3)}")
    sc = [pcset.SetClass12(pcset=set(row1[:6])), pcset.SetClass12(pcset=set(row1[6:]))]
    print(f"Hexachords: {sc[0].name_morris}, {sc[1].name_morris}")

    # Create two invariance matrices - T and I.
    imx = {
        'T': pcseg.InvarianceMatrix('T', row1, row1),
        'I': pcseg.InvarianceMatrix('I', row1, row1)
    }

    # We can print an entire invariance matrix - this may be only of limited use.
    print(f"\n\n{imx['T']}")

    # It's much more useful to just print the index that we are interested in.
    # We'll choose 6 for each of the invariance matrices.
    # Also, we'll print the row and the transformation so you can compare
    # them with the matrix
    print(f"\n\nInvariance matrix type: 'T'\n")
    imx['T'].print([pc[6]])
    print(f"\nRow: {row1}\nT6:  {ro['T6'].transform(row1)}")
    print(f"\n\nInvariance matrix type: 'I'\n")
    imx['I'].print([pc[6]])
    print(f"\nRow: {row1}\nT6I: {ro['T6I'].transform(row1)}")

"""
File: set_complex.py
Author: Jeff Martin
Description: A sample program for generating set-complexes using pctheory

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

import pctheory.pcset as pcset
import pctheory.pitch as pitch
import pctheory.set_complex as set_complex
import pctheory.transformations as transformations

if __name__ == "__main__":
    # An array with each of the twelve pitch-classes; the pitch-class numbers
    # align with the index in the array. A convenient way to refer to any pitch-class.
    pc = [pitch.PitchClass12(i) for i in range(12)]

    # Time to choose a nexus set. We'll go with the all-trichord hexachord, set-class
    # 6-Z17.
    nexus = pcset.SetClass12()
    nexus.load_from_name("6-Z17")  # we could have used the prime-form name, [012478] instead

    # Is it an all-trichord hexachord? We'll prove it by listing all of the abstract
    # set-classes included in this set-class.
    subsets = nexus.get_abstract_subset_classes()
    subsets3 = []
    for subset in subsets:
        if len(subset) == 3:
            subsets3.append(subset)
    print(f"There are {len(subsets3)} trichordal subset-classes in the ATH. " \
        "There are 12 trichordal subset-classes total.")
    print(subsets3)

    # Now it's time to get the complexes.
    k = set_complex.get_k12(nexus)
    kh = set_complex.get_kh12(nexus)

    # Finally, we'll print both complexes.
    print(f"Set-complex K about nexus set {nexus.name_morris}: \n")
    for set_class in k:
        print(set_class.name_morris)
    print(f"\n\nSet-complex Kh about nexus set {nexus.name_morris}: \n")
    for set_class in kh:
        print(set_class.name_morris)
    
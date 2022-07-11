"""
File: pcsets.py
Author: Jeff Martin
Description: A sample program for working with pcsets using pctheory

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
import pctheory.transformations as transformations

if __name__ == "__main__":
    # Gets all TTOs. This is often a useful thing to do at the start of a 
    # program that involves working with pitch-classes.
    tto = transformations.get_utos12()

    # An array with each of the twelve pitch-classes; the pitch-class numbers
    # align with the index in the array. A convenient way to refer to any pitch-class.
    pc = [pitch.PitchClass12(i) for i in range(12)]

    # First of all, we'll create several pcsets. We could make these by creating 
    # an empty set variable and filling it with PitchClass12 objects, but this way
    # is more convenient.
    pcset1 = pcset.make_pcset12(5, 8, 1, 0)
    pcset2 = pcset.make_pcset12(4, 3, 9, 6, 2)
    pcset3 = pcset.make_pcset12(10, 1, 5, 6, 11, 4)

    # What set-classes do these pcsets belong to?
    sc1 = pcset.SetClass12(pcset1)
    sc2 = pcset.SetClass12(pcset2)
    sc3 = pcset.SetClass12(pcset3)
    print("Set-classes:")
    print(sc1.name_prime)  # we could have chosen the Forte, Carter, or Morris name instead
    print(sc2.name_prime)
    print(sc3.name_prime)

    # What about ic vectors?
    print("\nic vectors:")
    print(sc1.ic_vector_str)
    print(sc2.ic_vector_str)
    print(sc3.ic_vector_str)

    # Suppose we want to know what set-classes are abstractly contained within sc3.
    subsc3 = sc3.get_abstract_subset_classes()
    print(f"\nAbstract subset-classes of {sc3.name_prime}:")
    for sc in subsc3:
        print(f"Prime form: {sc.name_prime}")
    
    # What would happen if we take the union of two of the original pcsets and put 
    # them into a set-class?
    pcset4 = pcset1.union(pcset3)
    sc4 = pcset.SetClass12(pcset4)
    print("\nUnion of two pcsets:")
    print(f"Prime form: {sc4.name_prime}")
    print(f"ic vector: {sc4.ic_vector_str}")

    # And finally, we'll transform the pcsets in some interesting ways.
    print("\nSome transformations:")
    print(tto["T5"].transform(pcset2))
    print(tto["T8I"].transform(sc3.pcset))
    print(tto["T1"].transform(pcset4))
    print(tto["T11I"].transform(pcset1))

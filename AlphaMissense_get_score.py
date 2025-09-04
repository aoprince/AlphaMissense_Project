import requests
import pandas as pd
import pytest


#Query API and print to screen

def amdb_req(chrom, pos, ref, alt):
    r = requests.get("https://api.amdb.co.uk/v1/variant?chrom=chr" + chrom + "&pos=" + pos 
                     + "&ref_allele=" + ref + "&alt_allele=" + alt + "&genome=hg38")
    print(r.json())

#user feedback that they would like to input all at once
nomen = input('variant in chr-position-ref-alt and hg38 format= ')

#split nomen by - to get chrom pos ref and alt
x = nomen.split('-')
chrom2, pos2, ref2, alt2 = x

#query API
amdb_req(chrom2, pos2, ref2, alt2)

#example variant 19-51353229-G-A

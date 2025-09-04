import requests
import pandas as pd
import pytest


#Query API and print to screen

def amdb_req(chrom, pos, ref, alt):
    r = requests.get("https://api.amdb.co.uk/v1/variant?chrom=chr" + chrom + "&pos=" + pos 
                     + "&ref_allele=" + ref + "&alt_allele=" + alt + "&genome=hg38")
    print(r.json())


#example variant 19-51353229-G-A

def test_answer():
    amdb_req('19', '51353229', 'G', 'A')
    assert {'chrom': 'chr19', 'pos': 51353229, 'ref': 'G', 'alt': 'A', 'genome': 'hg38', 'uniprot_id': 'P38117',
             'transcript_id': 'ENST00000309244.8', 'protein_variant': 'P93L', 'am_pathogenicity': 0.0785, 'am_class': 'likely_benign'}
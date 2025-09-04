import csv
import requests
import json
import pandas as pd


# personal preference, makes code easier to read if long text strings are variables
input_file = "PATH/project_variants_no_vus_unlimited_count_split_nodel.csv"

# open all needed files at the same time to save indentation
with open(input_file, "r") as csv_f, \
     open("try.csv", "w", newline='') as f1:

    reader_obj = csv.reader(csv_f)

    writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
    nested_dict = {}
    n = 0
    for row in reader_obj:
        chrom = row[0]
        pos = row[1]
        ref = row[2]
        alt = row[3]
        request_url = "https://api.amdb.co.uk/v1/variant?chrom=chr" + chrom + "&pos=" + pos + "&ref_allele=" + ref + "&alt_allele=" + alt + "&genome=hg38"
        r = requests.get(request_url)
        response = json.loads(r.text)

        if response:
            nested_dict[n] = response
            n += 1
        else:
            nested_dict[n] = {'chrom': chrom, 'pos': pos, 'ref': ref, 'alt': alt, 'genome': 'hg38', 'uniprot_id': 'na', 'transcript_id': 'na', 'protein_variant': 'na', 'am_pathogenicity': 0, 'am_class': 'na'}
            n += 1

output_df = pd.DataFrame.from_dict(nested_dict, orient='index')
output_df.to_csv('try.csv')
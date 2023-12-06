import click
import mygene
import pandas as pd
from pyliftover import LiftOver

def ensembl_to_hgnc(ensembl_ids):
    mg = mygene.MyGeneInfo()
    result = mg.querymany(ensembl_ids, scopes='ensembl.gene', fields='symbol,genomic_pos', species='mouse')
    return {item['query']: (item['symbol'], item.get('genomic_pos', {})) for item in result if 'symbol' in item}

@click.command()
@click.option('-i', '--input_file', prompt='Input file', help='The input file containing the ENSEMBL IDs.')
@click.option('-o', '--output_file',prompt='Output file', help='The output file to write the HGNC symbols.')
@click.option('-l', '--liftover', is_flag=True, help='Use this flag to lift over the genomic positions to the mm10 assembly.')
def process_file(input_file, output_file, liftover):
    # Read the input file
    df = pd.read_csv(input_file, sep='\t')

    # Get the ENSEMBL IDs from the file
    ensembl_ids = df['ensembl'].tolist()

    # Get the HGNC symbols and genomic positions
    hgnc_symbols_and_positions = ensembl_to_hgnc(ensembl_ids)

    # Add the HGNC symbols and genomic positions to the dataframe
    df['hgnc'] = df['ensembl'].map(lambda x: hgnc_symbols_and_positions[x][0] if x in hgnc_symbols_and_positions else None)
    df['chromosome'] = df['ensembl'].map(lambda x: hgnc_symbols_and_positions[x][1].get('chr') if x in hgnc_symbols_and_positions and 'chr' in hgnc_symbols_and_positions[x][1] else None)
    df['start'] = df['ensembl'].map(lambda x: hgnc_symbols_and_positions[x][1].get('start') if x in hgnc_symbols_and_positions and 'start' in hgnc_symbols_and_positions[x][1] else None)
    df['end'] = df['ensembl'].map(lambda x: hgnc_symbols_and_positions[x][1].get('end') if x in hgnc_symbols_and_positions and 'end' in hgnc_symbols_and_positions[x][1] else None)

    # If the liftover flag is set, lift over the genomic positions to the mm10 assembly
    if liftover:
        lo = LiftOver('mm39', 'mm10')
        df['chromosome'] = df['chromosome'].map(lambda x: 'chr' + x if pd.notnull(x) else x)
        df['start'] = df.apply(lambda row: lo.convert_coordinate(row['chromosome'], row['start'])[0][1] if pd.notnull(row['start']) else None, axis=1)
        df['end'] = df.apply(lambda row: lo.convert_coordinate(row['chromosome'], row['end'])[0][1] if pd.notnull(row['end']) else None, axis=1)

    # Reorder the columns
    df = df[['chromosome', 'start', 'end', 'hgnc', 'ensembl']]

    # Write the dataframe to the output file
    df.to_csv(output_file, sep='\t', index=False)

if __name__ == '__main__':
    process_file()


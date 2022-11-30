import argparse
from data.db import Session
from utilities import plot_gc_ratio
from data.base_classes import convert_dna_to_rna, convert_rna_to_protein


# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-dna", "--DnaToRna", help="convert DNA to RNA")
parser.add_argument("-rna", "--RnaToProtein", help="Convert RNA to protein")
parser.add_argument("-p", "--PlotGcRatio", help="open image")
parser.add_argument("-s", "--Step", help="denoting a width of a bin")

# Read arguments from command line
args = parser.parse_args()

if args.DnaToRna:
    print(f"Displaying DnaToRna as: {args.DnaToRna}")
    print(convert_dna_to_rna(Session(), args.DnaToRna))

if args.RnaToProtein:
    print(f"Displaying RnaToProtein as: {args.RnaToProtein}")
    print(convert_rna_to_protein(Session(), args.RnaToProtein))

if args.PlotGcRatio and args.Step:
    print(f"Displaying PlotGcRatio as: {args.PlotGcRatio}, step: {args.Step}")
    if plot_gc_ratio(args.PlotGcRatio, int(args.Step)):
        print("True")
    else:
        print("False")

elif args.PlotGcRatio:
    print(f"Displaying PlotGcRatio as: {args.PlotGcRatio}")
    if plot_gc_ratio(args.PlotGcRatio):
        print("True")
    else:
        print("False")

import getopt
import sys
import argparse
# from utilities import plot_gc_ratio
# from data.base_classes import convert_dna_to_rna, convert_rna_to_protein

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-dna", "--DnaToRna", help="convert DNA to RNA")
parser.add_argument("-rna", "--RnaToProtein", help="Convert RNA to protein")
parser.add_argument("-p", "--PlotGcRatio", help="open image")

# Read arguments from command line
args = parser.parse_args()

if args.DnaToRna:
    print("Displaying DnaToRna as: % s" % args.DnaToRna)

if args.RnaToProtein:
    print("Displaying RnaToProtein as: % s" % args.RnaToProtein)

if args.PlotGcRatio:
    print("Displaying PlotGcRatio as: % s" % args.PlotGcRatio)


# cloud_ai_assessment

# !/usr/bin/env python 3

import argparse
import sys
import os
import csv
# from pathlib import Path
import pandas as pd

def read_file(filepath):
	if not os.path.exists(filepath):
		print(f"Error: File '{filepath}' not found'")
		sys.exit(1)

	ext = os.path.splittext(filepath)[1].lower()

	if ext == ".csv":
		with open(filepath,"r",encoding="utf-8") as f:
			reader = csv.reader(f)
			for now in reader:
				print(",".join(row))
	else:
		with open(filepath,"r",encoding="utf-8") as f:
			print(f.read())
	
	# try:
	# 	content = file_path.read_text(encoding ="utf-8")
	# 	return content
	# except FileNotFoundError:
	# 	print(f"Error: file not found:{file_path}", file=sys.stderr)
	# 	return None
	# except PermissionError:
	# 	print(f"Error: Permission denied:{file_path}", file=sys.stderr)
	# 	return None
	# except FUnicodeDecodeError:
	# 	print(f"Error: file is not valid:{file_path}", file=sys.stderr)
	# 	return None

def load_dataframe(filepath):
	if not os.path.exists(filepath):
		print(f"Error: File '{filepath}' not found'")
		sys.exit(1)
	ext = os.path.splittext(filepath)[1].lower()

	try:
		if ext == "csv":
			df = pd.read_csv(filepath,parse_dates = True)
		elif ext in (".xlsx",".xls"):
			df = pd.read_excel(filepath,parse_dates = True)
		else:
			print(f"Error: Unsupported file")
			sys.exit(1)
	except Exception as e:
		print("Error loading file")	

def cad_analyze(args):
"""Display Dataframe info: shape, types, head, describe."""
	df = load_dataframe(args. filepath)
	print("=" * 60)
	print (f"ANALYSIS: {args.filepath}")
	print("="* 60)

	print(f"\nShape: {df.shape[0]} rows x {df.shape[1]} columns")
	print (f"\nColumn Types:")
	for col in df.columns:
		print(f" {col:20s} {str(df[col].dtype):15s} "
			  f" ({df[col].notna() -sum()}/{len(df)} non-null")
	print(f"\nFirst 5 rows:")
	print(df.head().to_string (index=True))

	print (f"\nMissing values:")
	missing = df.isna() -sum()
	missing_cols = missing[missing > 0]
	if len(missing_cols) == 0:
		print(" No missing values")
	else:
		for col, count in missing_cols.items():
			print(f" {col}: {count} missing")
	print(f"\nNumeric Sumary:")
	numeric_df = df.select_dtypes (include=" number")
	if not numeric_df.empty:
		print (numeric_df.describe().to_string())
	else:
		print(" No numeric columns found")

# def parse_arguments() -> argparse.Namespace:
# 	parser =argparse.ArgumentParser(
# 		description = "Analyze text and CSV files",
# 		epilog = "Example: python3 sample.csv -v",
# 	)
# 	parser.add_argument(
# 		"input_file",
# 		type = Path,
# 		help = "Path to the file to analyze (txt or CSV)",
# 	)
# 	parser.add_argument(
# 		"--output-dir",
# 		type = Path,
# 		default=None,
# 		help = "Directory to write result files",
# 	)
# 	parser.add_argument(
# 		"-v","--verbose",
# 		action = "store_true",
# 		help = "Enable verbose output with detailed processing information",
# 	)
# 	return parser.parse_args()
def cmd_read(args):
	content = read_file(args.filepath)
	if content is not None:
		print(content)

def main() -> int:
	# args = parse_arguments()
	# content = read_file(args.input_file)
	
	# if content is None:
	# 	return 1
	# print(f"Successfully read {args.input_file}")
	# print(f"File size: {len(content)} characters")

	# """
	# print(f"Input file: {args.input_file}")
	# print(f"Output dir: {args.output_dir}")
	# print(f"Verbose :   {args.verbose}")
	# """
	# return 0

	parser = argparse.ArgumentParser(
		description = "Data processing tool for CSV and Excel files"

		subparsers = parser.add_subparsers(
			dest = "command",
			help = "Available commadns"
		)

		read_parser = subparsers.add_parser(
			"read", help= "Read and display file contents"
		)
		read_parser.add_argument("filepath",help="Path to file")
		read_parser.set_defaults(func=cmd_read)

		args = parser.parse_args()

		if args.command is None:
			parser.print_help()
			sys.exit(1)
		args.func(args)
	)

if __name__ == "__main__":
	sys.exit(main())